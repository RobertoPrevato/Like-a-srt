import json
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import List, Union

import azure.cognitiveservices.speech as speechsdk
from essentials.folders import ensure_folder, get_file_extension

from likeasrt.domain.core import SpokenWord, get_segments
from likeasrt.domain.srt import get_related_file_name, write_segments
from likeasrt.errors import (
    InputFileNotFoundError,
    InvalidInputError,
    MissingEnvVariableError,
)
from likeasrt.logs import get_app_logger

logger = get_app_logger()


class RecognitionError(Exception):
    def __init__(self) -> None:
        super().__init__("A portion was not recognized. Cannot continue the process.")


@dataclass
class SpeechSettings:
    speech_subscription: str
    speed_endpoint: str

    @classmethod
    def from_env(cls):
        try:
            return cls(os.environ["SPEECH_SUBSCRIPTION"], os.environ["SPEECH_ENDPOINT"])
        except KeyError as key_error:
            raise MissingEnvVariableError(key_error.args[0]) from key_error


def tick_to_seconds(value: int) -> float:
    # A single tick represents one hundred nanoseconds or one ten-millionth of a second.
    # See: https://bit.ly/3talWxK
    return value / 1e7


def parse_result(raw_details: str) -> dict:
    return json.loads(raw_details)


def _eng_transform(display_text: str) -> str:
    return display_text.replace("i'm", "I'm")


def get_words(raw_details: str) -> List[SpokenWord]:
    details = parse_result(raw_details)
    n_best = details["NBest"]
    best_result = n_best[0]

    words = []

    display = _eng_transform(best_result.get("Display", ""))
    display_words_with_punctuation: List[str] = display.split(" ")

    for index, word in enumerate(best_result.get("Words", [])):
        # Offset and Duration are expressed in ticks, each tick is 100 nanoseconds
        start_time_in_seconds = tick_to_seconds(word["Offset"])
        end_time_in_seconds = start_time_in_seconds + tick_to_seconds(word["Duration"])

        text = word["Word"]
        # try to restore punctuation
        if display_words_with_punctuation:
            try:
                corresponding_display_word = display_words_with_punctuation[index]

                if text.lower() in corresponding_display_word.lower():
                    text = corresponding_display_word
            except IndexError:
                pass

        words.append(
            SpokenWord(
                start_time=start_time_in_seconds,
                end_time=end_time_in_seconds,
                text=text,
            )
        )

    return words


def extract_recognition(
    file_path: Union[str, Path], language: str = "en-US"
) -> List[speechsdk.SpeechRecognitionEventArgs]:
    settings = SpeechSettings.from_env()

    speech_config = speechsdk.SpeechConfig(
        subscription=settings.speech_subscription,
        endpoint=settings.speed_endpoint,
    )

    # necessary to generate .srt
    speech_config.request_word_level_timestamps()

    audio_input = speechsdk.AudioConfig(filename=str(file_path))
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_input, language=language
    )

    speech_recognizer.start_continuous_recognition()

    done = False

    events = []

    def on_recognized(evt):
        if evt.result.reason != speechsdk.ResultReason.RecognizedSpeech:
            raise RecognitionError()

        logger.info("RECOGNIZED: %s", evt)
        events.append(evt)

    def stop_cb(evt):
        logger.info("Recognition process complete...")
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True

    speech_recognizer.recognized.connect(on_recognized)
    speech_recognizer.session_stopped.connect(stop_cb)

    while not done:
        time.sleep(0.5)

    return events


def generate_from_events(
    events: List[speechsdk.SpeechRecognitionEventArgs], output_file_name: str
) -> None:
    all_words = []

    for evt in events:
        all_words += get_words(evt.result.json)

    segments = get_segments(all_words)
    srt = "".join(write_segments(segments))

    logger.info("Writing output file %s", output_file_name)
    with open(output_file_name, mode="wt", encoding="utf8") as output_srt_file:
        output_srt_file.write(srt)


def write_transcript_file(
    events: List[speechsdk.SpeechRecognitionEventArgs],
    output_file_name: str = "transcript.txt",
) -> None:
    with open(output_file_name, mode="wt", encoding="utf8") as output_file:
        for evt in events:
            output_file.write(evt.result.text + "\n")


def write_events_data(
    events: List[speechsdk.SpeechRecognitionEventArgs], file_names_prefix: str = ""
) -> None:
    """
    Writes detailed event data
    """
    out_folder = Path("out")
    ensure_folder("out")

    for index, evt in enumerate(events):
        with open(
            out_folder / f"{file_names_prefix}-evt-{index}.json",
            encoding="utf8",
            mode="wt",
        ) as evt_file:
            evt_file.write(
                json.dumps(json.loads(evt.result.json), ensure_ascii=False, indent=4)
            )


def validate_audio_file_path(file_path: Union[str, Path]) -> None:
    source_file = Path(file_path)

    extension = get_file_extension(source_file)

    if extension.lower() != ".wav":
        raise InvalidInputError(
            "The source file must be of type wav. Refer to the documentation for a "
            "reference on how to convert audio files using ffmpeg."
        )

    if not source_file.exists():
        raise InputFileNotFoundError(file_path)


def generate_srt_from_file(
    file_path: Union[str, Path],
    language: str = "en-US",
    write_transcript: bool = False,
    write_json: bool = False,
) -> None:
    validate_audio_file_path(file_path)
    output_file_name = get_related_file_name(file_path, ".srt")

    logger.info("Obtaining data from Azure Speech...")
    events = extract_recognition(file_path, language)

    if write_transcript:
        logger.info("Writing a transcript file: %s", output_file_name)
        transcript_file = get_related_file_name(file_path, "-transcript.txt")
        write_transcript_file(events, transcript_file)

    if write_json:
        logger.info(
            "Writing detailed JSON output from Azure Speech on disk, in 'out' folder."
        )
        write_events_data(events, get_related_file_name(file_path, ""))

    logger.debug("Writing the .srt output file: %s", output_file_name)
    generate_from_events(events, output_file_name)
