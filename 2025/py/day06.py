#!/usr/bin/env python3

from dataclasses import dataclass
from itertools import groupby
from math import prod
from pathlib import Path


@dataclass
class Problem:
    numbers: list[int]
    operation: str

    def total(self) -> int:
        match self.operation:
            case "+":
                return sum(self.numbers)
            case "*":
                return prod(self.numbers)
        raise ValueError("Invalid operation")


def read_input1(path: Path) -> list[Problem]:
    lines = path.read_text().strip().split("\n")
    problems = [Problem(numbers=[], operation=operation) for operation in lines[-1].split()]
    for line in lines[:-1]:
        for i, number in enumerate(line.split()):
            problems[i].numbers.append(int(number))
    return problems


def read_input2(path: Path) -> list[Problem]:
    lines = path.read_text().rstrip().split("\n")

    max_len = max(len(line) for line in lines)
    hlines = [line.ljust(max_len) for line in lines[:-1]]

    def _vline(i: int, lines: list[str]) -> str:
        return "".join([line[i] for line in lines])

    vlines = [_vline(i, hlines).strip() for i in range(max_len)]

    # From here on it is a simple problem again
    problems = [Problem(numbers=[], operation=operation) for operation in lines[-1].split()]
    for i, numbers in enumerate([list(g) for k, g in groupby(vlines, key=bool) if k]):
        problems[i].numbers = [int(n) for n in numbers]
    return problems


def part1(problems: list[Problem]) -> int:
    return sum(p.total() for p in problems)


def part2(problems: list[Problem]) -> int:
    return sum(p.total() for p in problems)


def transform(text: str) -> str:
    return text


if __name__ == "__main__":
    print("Part 1: ", part1(read_input1(Path("day06_input.txt"))))
    print("Part 2: ", part2(read_input2(Path("day06_input.txt"))))
