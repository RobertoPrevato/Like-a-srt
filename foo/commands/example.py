import click

from foo.logs import get_app_logger

logger = get_app_logger()


def foo() -> str:
    return "foo"


@click.command(name="example")
def example_command():
    logger.debug("Called foo")
    logger.info("Info")
    try:
        print("Example")
    except KeyboardInterrupt:
        logger.info("[*] User interrupted")
        exit(1)
