#!/usr/bin/env python3


from aoc import Grid, Position


def flash(grid: Grid, p: Position, flashed):
    flashed.add(p)
    for n in grid.neighbours(p, diagonal=True):
        grid.set(n, grid.get(n) + 1)


def step(grid: Grid):
    for y in range(grid.height):
        for x in range(grid.width):
            p = Position(x, y)
            grid.set(p, grid.get(p) + 1)

    flashed = set()

    while True:
        c = len(flashed)
        for y in range(grid.height):
            for x in range(grid.width):
                p = Position(x, y)
                if grid.get(p) > 9:
                    if p not in flashed:
                        flash(grid, p, flashed)
        if len(flashed) == c:
            break

    for p in flashed:
        grid.set(p, 0)

    return len(flashed)


def part1():
    grid = Grid.from_file("day11.input", int)
    return sum(step(grid) for _ in range(100))


def part2():
    grid = Grid.from_file("day11.input", int)
    for n in range(1_000_000):
        if step(grid) == (grid.width * grid.height):
            return n+1


if __name__ == "__main__":
    print("Part one:", part1())
    print("Part two:", part2())
