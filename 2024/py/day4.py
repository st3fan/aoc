#!/usr/bin/env python3

from aoc import Grid, Position


VECTORS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


def check_xmas(grid: Grid[str], x: int, y: int, v: tuple[int, int]) -> bool:
    word = ""
    for _ in range(4):
        if x >= 0 and y >= 0:
            if x < grid.width and y < grid.height:
                word += grid.get(Position(x, y))
                x += v[0]
                y += v[1]
    return word == "XMAS"


def check_shape(grid: Grid[str], x: int, y: int, shape: Grid[str]) -> bool:
    for sx in range(shape.width):
        for sy in range(shape.height):
            c = shape.get(Position(sx, sy))
            if c != "." and grid.get(Position(x + sx, y + sy)) != c:
                return False
    return True


if __name__ == "__main__":
    grid = Grid.from_file("day4.txt", lambda v: v)

    total = 0
    for x in range(grid.width):
        for y in range(grid.height):
            for v in VECTORS:
                if check_xmas(grid, x, y, v):
                    total += 1
    print("Part1:", total)

    shape1 = Grid.from_file("day4_shape1.txt", lambda v: v)
    shape2 = Grid.from_file("day4_shape2.txt", lambda v: v)
    shape3 = Grid.from_file("day4_shape3.txt", lambda v: v)
    shape4 = Grid.from_file("day4_shape4.txt", lambda v: v)

    total = 0
    for x in range(grid.width - 2):
        for y in range(grid.height - 2):
            for shape in (shape1, shape2, shape3, shape4):
                if check_shape(grid, x, y, shape):
                    total += 1
    print("Part2:", total)
