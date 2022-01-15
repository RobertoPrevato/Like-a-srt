"""
Functions and methods that are specific to SubRip .srt format.
https://en.wikipedia.org/wiki/SubRip
"""
from pathlib import Path
from typing import Iterable, Union

from essentials.folders import split_path

from .core import Segment


def write_time(seconds: float) -> str:
    hours, milliseconds = divmod(seconds * 1000, 3600000)
    minutes, milliseconds = divmod(milliseconds, 60000)
    seconds = float(milliseconds) / 1000
    return ("%02i:%02i:%06.3f" % (hours, minutes, seconds)).replace(".", ",")


def write_segment(segment: Segment) -> str:
    """
    Example:
        00:00:00,240 --> 00:00:03,580
        Hello! How are you?
    """
    return (
        f"{write_time(segment.start_time)} --> {write_time(segment.end_time)}\n"
        + segment.text
        + "\n"
    )


def write_segments(segments: Iterable[Segment]) -> Iterable[str]:
    for index, segment in enumerate(segments):
        yield str(index) + "\n"
        yield write_segment(segment) + "\n"


def get_related_file_name(
    original_file_path: Union[str, Path], suffix: str = ".srt"
) -> str:
    """
    Returns a new file name, starting from an original file and applying the given
    suffix. The suffix is supposed to contain the result file extension!
    """
    _, file_name, _ = split_path(str(original_file_path))
    return file_name + suffix
