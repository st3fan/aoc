#!/usr/bin/env python


from itertools import pairwise
from typing import List


def read_input() -> List[List[int]]:
    with open("day9.txt") as f:
        return [[int(v) for v in line.split()] for line in f.readlines()]


def solve(history: List[int]) -> int:
    sequences = [history]
    while sequences[-1].count(0) != len(sequences[-1]):
        sequences.append([b - a for a, b in pairwise(sequences[-1])])
    return sum(s[-1] for s in sequences)


def part1() -> int:
    return sum(solve(history) for history in read_input())


def part2() -> int:
    return sum(solve(list(reversed(history))) for history in read_input())


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
