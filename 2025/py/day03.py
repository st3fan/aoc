#!/usr/bin/env python3

from itertools import combinations
from pathlib import Path

type Input = list[list[int]]


def read_input(path: Path) -> Input:
    def _transform(line: str) -> list[int]:
        return [int(s) for s in line]

    return [_transform(line) for line in path.read_text().split()]


def largest_subsequence(digits, n):
    result = 0
    start = 0

    for i in range(n):
        remaining_needed = n - i - 1
        end = len(digits) - remaining_needed

        max_idx = max(range(start, end), key=lambda j: digits[j])
        result = result * 10 + digits[max_idx]
        start = max_idx + 1

    return result


def day1(input: Input) -> int:
    return sum(largest_subsequence(bank, 2) for bank in input)


def day2(input: Input) -> int:
    return sum(largest_subsequence(bank, 12) for bank in input)


if __name__ == "__main__":
    input = read_input(Path("day03_input.txt"))
    print("Day 1:", day1(input))
    print("Day 2:", day2(input))
