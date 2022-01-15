from dataclasses import dataclass
from typing import Iterable, List, Optional


@dataclass
class SpokenWord:
    start_time: float
    end_time: float
    text: str


class SegmentWithoutWordsError(TypeError):
    def __init__(self) -> None:
        super().__init__("This segment does not contain any word")


@dataclass
class Segment:
    "Represents a segment in subtitles."
    words: List[SpokenWord]

    def add_word(self, word: SpokenWord) -> None:
        self.words.append(word)

    @property
    def start_time(self) -> float:
        if not self.words:
            raise SegmentWithoutWordsError()
        return self.words[0].start_time

    @property
    def end_time(self) -> float:
        if not self.words:
            raise SegmentWithoutWordsError()
        return self.words[-1].end_time

    @property
    def text(self) -> str:
        return " ".join(word.text for word in self.words)


def get_segments(
    spoken_words: Iterable[SpokenWord], segment_length: float = 3.0
) -> Iterable[Segment]:
    current_segment: Optional[Segment] = None

    for word in spoken_words:
        if current_segment is None:
            current_segment = Segment([word])
        else:
            if word.end_time - current_segment.start_time > segment_length:
                # create a new segment
                yield current_segment
                current_segment = Segment([word])
            else:
                # add the word to the current segment
                current_segment.add_word(word)

    if current_segment is not None:
        yield current_segment
