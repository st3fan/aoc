#!/usr/bin/env python


from dataclasses import dataclass
from typing import Generator, Tuple


@dataclass(frozen=True)
class Range:
    start: int
    end: int

    def contains(self, o: "Range") -> bool:
        return self.start >= o.start and self.end <= o.end \
            or o.start >= self.start and o.end <= self.end

    def intersects(self, o: "Range") -> bool:
        return self.start <= o.start <= self.end or self.start <= o.end <= self.end \
            or o.start <= self.start <= o.end or o.start <= self.end <= o.end

    @staticmethod
    def from_string(s: str) -> "Range":
        start, end = s.split("-")
        return Range(int(start), int(end))


@dataclass(frozen=True)
class Pair:
    a: Range
    b: Range

    @staticmethod
    def from_string(s: str) -> "Pair":
        left, right = s.strip().split(",")
        return Pair(Range.from_string(left), Range.from_string(right))


def read_input() -> Generator[Pair, None, None]:
    with open("day4.txt") as f:
        for line in f.readlines():
            yield Pair.from_string(line)


def part1() -> int:
    return sum(
        pair.a.contains(pair.b) or pair.b.contains(pair.a) for pair in read_input()
    )


def part2() -> int:
    return sum(
        pair.a.intersects(pair.b) for pair in read_input()
    )


if __name__ == "__main__":
    print("Part1:", part1())
    print("Part2:", part2())
