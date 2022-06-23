#!/usr/bin/env python3


from aoc import InfiniteGrid, Position, Line


def load():
	return [Line.from_string(line.strip()) for line in open("day5.input").readlines()]

#
# I started with the most basic line drawing algorithm, just covering
# straight lines. Can probably be optimized into one case with dx and dy.
#

def grid_line1(grid, line):
    if line.ishorizontal():
        start = min(line.start.x, line.end.x)
        end = max(line.start.x, line.end.x)
        for x in range(start, end+1):
            p = Position(x, line.start.y),
            grid.set(p, grid.get(p, 0) + 1)
    elif line.isvertical():
        start = min(line.start.y, line.end.y)
        end = max(line.start.y, line.end.y)
        for y in range(start, end+1):
            p = Position(line.start.x, y),
            grid.set(p, grid.get(p, 0) + 1)
        

#
# DDA is the simplest line drawing algorithm, which has fine results
# if you only have 45 degree diagonals.
#
# See https://en.wikipedia.org/wiki/Digital_differential_analyzer_(graphics_algorithm)
#

def grid_line2(grid, line):
    dx = line.end.x - line.start.x
    dy = line.end.y - line.start.y

    steps = max(abs(dx), abs(dy))

    xi = dx // steps
    yi = dy // steps

    x = line.start.x
    y = line.start.y

    for _ in range(steps + 1):
        p = Position(x, y)
        grid.set(p, grid.get(p, 0) + 1)
        x += xi
        y += yi


def part1():
    grid = InfiniteGrid()
    for line in load():
        grid_line1(grid, line)
    return sum(v > 1 for v in grid.nodes.values())


def part2():
    grid = InfiniteGrid()
    for line in load():
        grid_line2(grid, line)
    return sum(v > 1 for v in grid.nodes.values())


if __name__ == "__main__":
	print("Part one:", part1())
	print("Part two:", part2())
