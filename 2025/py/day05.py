#!/usr/bin/env python

from pathlib import Path
from typing import NamedTuple


class Range(NamedTuple):
    min: int
    max: int


def read_input(path: Path) -> tuple[list[Range], list[int]]:
    def _parse_range(s: str) -> Range:
        c = s.split("-")
        return Range(int(c[0]), int(c[1]))

    contents = path.read_text()
    ranges, ingredients = contents.split("\n\n")

    return (
        [_parse_range(range) for range in ranges.strip().split()],
        [int(s) for s in ingredients.strip().split()],
    )


def _match_range(range: Range, ingredient: int) -> bool:
    return ingredient >= range.min and ingredient <= range.max


def day1(ranges: list[Range], ingredients: list[int]) -> int:
    return sum(any(_match_range(r, i) for r in ranges) for i in ingredients)


def _merge_ranges(ranges: list[Range]) -> list[Range]:
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged_ranges = [sorted_ranges[0]]
    for r in sorted_ranges[1:]:
        d = merged_ranges[-1]
        if r[0] >= d[0] and r[0] <= d[1]:
            merged_ranges[-1] = Range(d.min, max(r.max, d.max))
        else:
            merged_ranges.append(r)
    return merged_ranges


def day2(ranges: list[Range]) -> int:
    merged_ranges = _merge_ranges(ranges)
    return sum(1 + r.max - r.min for r in merged_ranges)


if __name__ == "__main__":
    ranges, ingredients = read_input(Path("day05_input.txt"))
    print("Day 1:", day1(ranges, ingredients))
    print("Day 2:", day2(ranges))
