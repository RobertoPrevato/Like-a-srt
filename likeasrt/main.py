import logging
import sys

import click

from . import VERSION
from .commands.srt import generate_srt_command
from .logs import get_app_logger

sys.path.append(".")


@click.group()
@click.option(
    "--verbose", default=False, help="Whether to display debug output.", is_flag=True
)
@click.version_option(version=VERSION)
def main(verbose):
    """
    CLI to generate subtitles in srt format from audio files, using Azure Speech.

    Roberto Prevato https://github.com/RobertoPrevato/Like-a-srt
    """
    logger = get_app_logger()
    if verbose:
        logger.setLevel(logging.DEBUG)

    logger.debug("Running in --verbose mode")


main.add_command(generate_srt_command)
