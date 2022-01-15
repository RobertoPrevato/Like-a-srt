import pytest

from likeasrt.domain.srt import get_related_file_name, write_time


@pytest.mark.parametrize(
    "value,expected_result",
    [
        (0, "00:00:00,000"),
        (2.50, "00:00:02,500"),
        (66.00, "00:01:06,000"),
        (99.00, "00:01:39,000"),
        (125.56, "00:02:05,560"),
    ],
)
def test_write_time(value, expected_result):
    result = write_time(value)
    assert result == expected_result


@pytest.mark.parametrize(
    "original_file_path,suffix,expected_result",
    [
        ["foo.wav", ".srt", "foo.srt"],
        ["foo.wav", "-transcript.txt", "foo-transcript.txt"],
        ["foo.wav", "-evt-1.json", "foo-evt-1.json"],
        ["foo.wav", "", "foo"],
        ["/home/user/foo.wav", ".srt", "foo.srt"],
    ],
)
def test_related_file_name(original_file_path, suffix, expected_result):
    result = get_related_file_name(original_file_path, suffix)
    assert result == expected_result
