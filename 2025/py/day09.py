#!/usr/bin/env python3


from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
from typing import Self


@dataclass(frozen=True)
class Pos:
    x: int
    y: int
    # z: int

    @classmethod
    def from_str(cls, s) -> Self:
        c = s.split(",")
        return cls(x=int(c[0]), y=int(c[1]))


def read_input(path: str) -> list[Pos]:
    with open(path) as fp:
        return [Pos.from_str(line.strip()) for line in fp.readlines()]


def size(p1: Pos, p2: Pos) -> int:
    width = abs(p1.x - p2.x)
    height = abs(p1.y - p2.y)
    return (width + 1) * (height + 1)


def part1(input: list[Pos]) -> int:
    return max(size(p1, p2) for p1, p2 in combinations(input, 2))


def rectangle_points(p1: Pos, p2: Pos) -> set[Pos]:
    min_x, max_x = sorted([p1.x, p2.x])
    min_y, max_y = sorted([p1.y, p2.y])

    return {Pos(x, y) for x in range(min_x, max_x + 1) for y in range(min_y, max_y + 1)}


@dataclass(frozen=True)
class Range:
    s: int
    e: int


def box_scanlines(p1: Pos, p2: Pos) -> dict[int, list[Range]]:
    min_x, max_x = sorted([p1.x, p2.x])
    min_y, max_y = sorted([p1.y, p2.y])
    x_range = Range(min_x, max_x)
    return {y: [x_range] for y in range(min_y, max_y + 1)}


# returns map of y ranges to
def all_scanlines(input: list[Pos]) -> dict[int, list[Range]]:
    all = {}
    for p1, p2 in combinations(input, 2):
        scanlines = box_scanlines(p1, p2)
        # TODO Merge
        all |= scanlines
    return all


def corners(p1: Pos, p2: Pos) -> list[Pos]:
    min_x, max_x = sorted([p1.x, p2.x])
    min_y, max_y = sorted([p1.y, p2.y])

    return [
        Pos(min_x, min_y),
        Pos(max_x, min_y),
        Pos(min_x, max_y),
        Pos(max_x, max_y),
    ]


def create_scanlines(input: list[Pos]) -> dict[int, list[int]]:
    x = defaultdict(list)
    for p in input:
        x[p.y].append(p.x)
    for v in x.values():
        v.sort()
    return x


def in_thing(p: Pos, scanlines: dict[int, list[int]]) -> bool:
    if range := scanlines.get(p.y):
        return p.x >= range[0] and p.x <= range[1]
    return False


def part2(input: list[Pos]) -> int: ...


if __name__ == "__main__":
    input = read_input("day09_test.txt")
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
