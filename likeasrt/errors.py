from typing import List


class CLIError(Exception):
    """
    Base class for all exception risen by the CLI.
    """


class InvalidInputError(CLIError):
    """
    Generic exception type for invalid input.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


class InputFileNotFoundError(InvalidInputError):
    """
    Exception risen when an expected input file is not found.
    """

    def __init__(self) -> None:
        super().__init__("File not found")


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
