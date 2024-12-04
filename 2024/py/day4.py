#!/usr/bin/env python3

from aoc import Grid, Position


VECTORS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


def check_xmas1(grid: Grid[str], x: int, y: int, v: tuple[int, int]) -> bool:
    word = ""
    for _ in range(4):
        if x >= 0 and y >= 0:
            if x < grid.width and y < grid.height:
                word += grid.get(Position(x, y))
                x += v[0]
                y += v[1]
    return word == "XMAS"


if __name__ == "__main__":
    grid = Grid.from_file("day4.txt", lambda v: v)

    total = 0
    for x in range(grid.width):
        for y in range(grid.height):
            for v in VECTORS:
                if check_xmas1(grid, x, y, v):
                    total += 1
    print("Part1:", total)
