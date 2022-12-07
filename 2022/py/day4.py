#!/usr/bin/env python3.11


from dataclasses import dataclass
from typing import Generator, Self


@dataclass(frozen=True)
class Range:
    start: int
    end: int

    def contains(self: Self, o: Self) -> bool:
        return self.start >= o.start and self.end <= o.end or o.start >= self.start and o.end <= self.end

    def intersects(self: Self, o: Self) -> bool:
        return (
            self.start <= o.start <= self.end
            or self.start <= o.end <= self.end
            or o.start <= self.start <= o.end
            or o.start <= self.end <= o.end
        )

    @classmethod
    def from_string(cls, s: str) -> Self:
        start, end = s.split("-")
        return cls(int(start), int(end))


@dataclass(frozen=True)
class Pair:
    a: Range
    b: Range

    @classmethod
    def from_string(cls, s: str) -> Self:
        left, right = s.strip().split(",")
        return cls(Range.from_string(left), Range.from_string(right))


def read_input() -> Generator[Pair, None, None]:
    with open("day4.txt") as file:
        for line in file.readlines():
            yield Pair.from_string(line)


def part1() -> int:
    return sum(pair.a.contains(pair.b) or pair.b.contains(pair.a) for pair in read_input())


def part2() -> int:
    return sum(pair.a.intersects(pair.b) for pair in read_input())


if __name__ == "__main__":
    print("Part1:", part1())
    print("Part2:", part2())
