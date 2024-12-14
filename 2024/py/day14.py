#!/usr/bin/env python

from __future__ import annotations

from dataclasses import dataclass
from typing import NamedTuple


@dataclass
class Robot:
    px: int
    py: int
    vx: int
    vy: int

    def move(self, w: int, h: int):
        self.px = self.px + self.vx
        if self.px > (w - 1):
            self.px = self.px % w
        if self.px < 0:
            self.px += w

        self.py = self.py + self.vy
        if self.py > (h - 1):
            self.py = self.py % h
        if self.py < 0:
            self.py += h

    @classmethod
    def from_str(cls, s: str) -> Robot:
        return cls(
            int(s.split()[0][2:].split(",")[0]),
            int(s.split()[0][2:].split(",")[1]),
            int(s.split()[1][2:].split(",")[0]),
            int(s.split()[1][2:].split(",")[1]),
        )


def read_input(path: str) -> list[Robot]:
    with open(path) as fp:
        return [Robot.from_str(line.strip()) for line in fp.readlines()]


def safety_factor(robots: list[Robot], w: int, h: int) -> int:
    q1 = 0
    for r in robots:
        if r.px < w // 2 and r.py < h // 2:
            q1 += 1

    q2 = 0
    for r in robots:
        if r.px > w // 2 and r.py < h // 2:
            q2 += 1

    q3 = 0
    for r in robots:
        if r.px < w // 2 and r.py > h // 2:
            q3 += 1

    q4 = 0
    for r in robots:
        if r.px > w // 2 and r.py > h // 2:
            q4 += 1

    return q1 * q2 * q3 * q4


def calculate(robots: list[Robot], w: int, h: int, n: int) -> int:
    for _ in range(n):
        for r in robots:
            r.move(w, h)
    return safety_factor(robots, w, h)


def is_tree(robots: list[Robot], w: int, h: int) -> bool:
    q1 = 0
    for r in robots:
        if r.px < w // 2 and r.py < h // 2:
            q1 += 1

    q2 = 0
    for r in robots:
        if r.px > w // 2 and r.py < h // 2:
            q2 += 1

    q3 = 0
    for r in robots:
        if r.px < w // 2 and r.py > h // 2:
            q3 += 1

    q4 = 0
    for r in robots:
        if r.px > w // 2 and r.py > h // 2:
            q4 += 1

    return (q1 + q3) == (q2 + q4)


def has_neighbours(grid, x, y):
    for vx, vy in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)):
        if grid[y + vy][x + vx] != " ":
            return True


class Point(NamedTuple):
    x: int
    y: int


def expand_region(grid: list[list[str]], w: int, h: int, p: Point) -> set[Point]:
    points: set[Point] = set()

    def on_map(p: Point, w: int, h: int):
        return p.x >= 0 and p.x < w and p.y >= 0 and p.y < h

    def dfs(p: Point):
        if p in points or (not on_map(p, w, h) or grid[p.y][p.x] != "*"):
            return
        points.add(p)
        for v in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)):
            dfs(Point(x=p.x + v[0], y=p.y + v[1]))

    dfs(p)

    return points


def is_empty(grid: list[list[str]]) -> bool:
    for line in grid:
        for c in line:
            if c == "*":
                return False
    return True


def dump(robots: list[Robot], w: int, h: int):
    grid = [[" "] * w for _ in range(h)]
    for r in robots:
        if r.px > 0 and r.px < (w - 1) and r.py > 0 and r.py < (h - 1):
            grid[r.py][r.px] = "*"
    # # Remove points with no neighbours
    # for x in range(w):
    #     for y in range(h):
    #         if grid[y][x] == "*" and not has_neighbours(grid, x, y):
    #             grid[y][x] = " "

    # Remove small point clusters

    MIN_ROBOTS = 50

    for x in range(w):
        for y in range(h):
            points = expand_region(grid, w, h, Point(x, y))
            if len(points) < MIN_ROBOTS:
                for p in points:
                    grid[p.y][p.x] = " "

    if not is_empty(grid):
        for line in grid:
            print("".join(line))
        return True


def detect_tree(robots: list[Robot], w: int, h: int) -> int:
    for n in range(1_000_000):
        for r in robots:
            r.move(w, h)
        if dump(robots, w, h):
            print("This was is iteration", n + 1)
    return 0


if __name__ == "__main__":
    print("Part1:", calculate(read_input("day14.txt"), 101, 103, 100))
    print("Part2:", detect_tree(read_input("day14.txt"), 101, 103))