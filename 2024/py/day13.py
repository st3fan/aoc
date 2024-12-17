#!/usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Vector:
    x: int
    y: int


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Machine:
    a: Vector
    b: Vector
    p: Point

    @classmethod
    def from_str(cls, s: str) -> Machine:
        # Hackyhacky
        lines = s.split("\n")
        return Machine(
            a=Vector(int(lines[0].split()[2][2:-1]), int(lines[0].split()[3][2:])),
            b=Vector(int(lines[1].split()[2][2:-1]), int(lines[1].split()[3][2:])),
            p=Point(int(lines[2].split()[1][2:-1]), int(lines[2].split()[2][2:])),
        )


def parse_input(path: Path) -> list[Machine]:
    return [Machine.from_str(s) for s in path.read_text().strip().split("\n\n")]


# This was more fun

MAX_MOVES = 100


def brute(m: Machine, add=0):
    x = m.p.x + add
    y = m.p.y + add
    for an in range(1, MAX_MOVES + 1):
        for bn in range(1, MAX_MOVES + 1):
            if an * m.a.x + bn * m.b.x == x:
                if an * m.a.y + bn * m.b.y == y:
                    yield an * 3 + bn


def min_or_zero(it) -> int:
    try:
        return min(it)
    except ValueError:
        return 0


# With some hints from Reddit


def calculate(m: Machine, add: int = 0) -> int:
    a = ((m.p.x + add) * m.b.y - (m.p.y + add) * m.b.x) / (m.a.x * m.b.y - m.a.y * m.b.x)
    b = (m.a.x * (m.p.y + add) - m.a.y * (m.p.x + add)) / (m.a.x * m.b.y - m.a.y * m.b.x)
    if a.is_integer() and b.is_integer():
        return int(a * 3 + b)
    return 0


if __name__ == "__main__":
    machines = parse_input(Path("day13.txt"))
    print("Part1", sum(calculate(m) for m in machines))
    print("Part2", sum(calculate(m, add=10000000000000) for m in machines))
