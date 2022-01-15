from uuid import uuid4

import pytest

from likeasrt.domain.azurespeech import validate_audio_file_path
from likeasrt.errors import InputFileNotFoundError, InvalidInputError


def test_validate_audio_file_raises_for_non_wav():
    with pytest.raises(InvalidInputError):
        validate_audio_file_path("foo.mp4")


def test_validate_audio_file_raises_for_non_existing_file():
    with pytest.raises(InputFileNotFoundError):
        validate_audio_file_path(f"{uuid4()}.wav")
