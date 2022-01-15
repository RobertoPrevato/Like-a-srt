from pathlib import Path
from typing import List, Union


class CLIError(Exception):
    """
    Base class for all exception risen by the CLI.
    """


class InvalidInputError(CLIError):
    """
    Generic exception type for invalid input.
    """


class InputFileNotFoundError(InvalidInputError):
    """
    Exception risen when an expected input file is not found.
    """

    def __init__(self, file_path: Union[str, Path]) -> None:
        super().__init__(f"File {file_path} not found")


class MissingEnvVariableError(CLIError):
    """
    Exception risen when an expected environmental variable is not configured.
    """

    def __init__(self, name: str) -> None:
        super().__init__(f"Missing ENV variable: {name}")


class MissingEnvVariablesError(CLIError):
    """
    Exception risen when expected environmental variables are not configured.
    """

    def __init__(self, names: List[str]) -> None:
        super().__init__(f"Missing ENV variables: {', '.join(names)}")
