import sys

from likeasrt.errors import CLIError, InvalidInputError
from likeasrt.logs import get_app_logger

logger = get_app_logger()


def run(function):
    """
    Runs a function for a command, handling common exceptions such as KeyboardInterrupt,
    CLI errors, invalid input, etc.
    """
    try:
        function()
    except InvalidInputError as invalid_input:
        logger.error("Error: %s", invalid_input)
        sys.exit(1)
    except CLIError as cli_error:
        logger.error(cli_error)
        sys.exit(2)
    except KeyboardInterrupt:
        logger.info("[*] User interrupted")
        sys.exit(1)
