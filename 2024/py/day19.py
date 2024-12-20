#!/usr/bin/env python


from functools import cache
from pathlib import Path


def read_input(path: str) -> tuple[list[str], list[str]]:
    patterns, designs = Path(path).read_text().split("\n\n")
    return patterns.strip().split(", "), designs.strip().split("\n")


#


def test1(design: str, patterns: list[str]) -> bool:
    def _test1(design: str) -> bool:
        if design == "":
            return True

        return any(_test1(design[len(p) :]) for p in patterns if design.startswith(p))

    return _test1(design)


def part1(patterns: list[str], designs: list[str]) -> int:
    return sum(test1(design, patterns) for design in designs)


#


def test2(design: str, patterns: list[str]) -> int:
    @cache
    def _test2(design: str) -> int:
        if design == "":
            return 1
        return sum(_test2(design[len(p) :]) for p in patterns if design.startswith(p))

    return _test2(design)


def part2(patterns: list[str], designs: list[str]) -> int:
    return sum(test2(design, patterns) for design in designs)


#


if __name__ == "__main__":
    patterns, designs = read_input("day19.txt")
    print("Part1:", part1(patterns, designs))
    print("Part2:", part2(patterns, designs))
