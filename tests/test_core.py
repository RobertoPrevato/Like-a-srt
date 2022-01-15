import pytest

from likeasrt.domain.core import Segment, SpokenWord, get_segments


@pytest.mark.parametrize(
    "words,expected_first_text,expected_first_start_time,expected_first_end_time",
    [
        (
            [SpokenWord(text="Hello!", start_time=0.0, end_time=0.25)],
            "Hello!",
            0.0,
            0.25,
        ),
        (
            [
                SpokenWord(text="Hello", start_time=0.0, end_time=0.25),
                SpokenWord(text="World!", start_time=0.27, end_time=0.54),
            ],
            "Hello World!",
            0.0,
            0.54,
        ),
        (
            [
                SpokenWord(text="Hello", start_time=0.0, end_time=0.25),
                SpokenWord(text="World!", start_time=0.27, end_time=0.54),
                SpokenWord(text="Something more...", start_time=5.27, end_time=5.74),
            ],
            "Hello World!",
            0.0,
            0.54,
        ),
    ],
)
def test_get_segments_1(
    words, expected_first_text, expected_first_start_time, expected_first_end_time
):
    result = list(get_segments(words))

    first_segment = result[0]
    assert isinstance(first_segment, Segment)
    assert first_segment.text == expected_first_text
    assert first_segment.start_time == expected_first_start_time
    assert first_segment.end_time == expected_first_end_time
