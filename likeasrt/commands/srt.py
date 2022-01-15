import click
from dotenv import load_dotenv

from likeasrt.commands import run
from likeasrt.domain.azurespeech import generate_srt_from_file
from likeasrt.logs import get_app_logger

load_dotenv()

logger = get_app_logger()


@click.command(name="gen")
@click.option("--source", "-s", help="source audio file", required=True)
@click.option(
    "--language",
    "-l",
    help="source audio file language",
    default="en-US",
    required=True,
)
@click.option(
    "--write-transcript",
    "-t",
    help="if specified, a transcript file is generated from the extracted information",
    default=False,
    required=False,
    is_flag=True,
)
@click.option(
    "--write-json",
    "-j",
    default=False,
    help=(
        "if specified, it writes JSON output of each "
        "Azure Speech recognition event on disk."
    ),
    is_flag=True,
)
def generate_srt_command(
    source: str, language: str, write_transcript: bool, write_json: bool
):
    """
    Given an input audio file, it obtains a transcript using Azure Speech, then
    generates a subtitles file having a name equal to the one of the input audio file,
    but ".srt" extension.
    """
    run(lambda: generate_srt_from_file(source, language, write_transcript, write_json))
