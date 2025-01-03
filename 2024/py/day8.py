#!/usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations


@dataclass(frozen=True)
class Vector:
    x: int
    y: int


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __sub__(self, other: Point) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, v) -> Point:
        if isinstance(v, Vector):
            return Point(self.x + v.x, self.y + v.y)
        raise TypeError(f"unsupported operand type(s) for +: '{self.__class__}' and '{v.__class__}'")


@dataclass(frozen=True)
class Antenna:
    f: str
    p: Point


def read_input(path) -> tuple[int, int, list[Antenna]]:
    """Return map width, height and antennas"""
    with open(path) as fp:
        antennas = []
        map = [list(line.strip()) for line in fp]
        for y, row in enumerate(map):
            for x, c in enumerate(row):
                if c != ".":
                    antennas.append(Antenna(c, Point(x, y)))
        return len(map[0]), len(map), antennas


def part1(width: int, height: int, antennas: list[Antenna]) -> int:
    antinodes: set[Point] = set()
    for f in {a.f for a in antennas}:
        for a, b in permutations([a.p for a in antennas if a.f == f], r=2):
            p = a + (a - b)
            if 0 <= p.x < width and 0 <= p.y < height:
                antinodes.add(p)
    return len(antinodes)


def part2(width: int, height: int, antennas: list[Antenna]) -> int:
    antinodes = {a.p for a in antennas}
    for f in {a.f for a in antennas}:
        for a, b in permutations([a.p for a in antennas if a.f == f], r=2):
            v = a - b
            while (a := a + v) and 0 <= a.x < width and 0 <= a.y < height:
                antinodes.add(a)
    return len(antinodes)


if __name__ == "__main__":
    width, height, antennas = read_input("day8.txt")
    print("Part1:", part1(width, height, antennas))
    print("Part2:", part2(width, height, antennas))
