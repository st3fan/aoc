#!/usr/bin/env python

from networkx import Graph, shortest_path
from networkx.exception import NetworkXNoPath

from aoc import Grid, Position


def read_input(path: str) -> list[Position]:
    with open(path) as fp:
        return [Position.from_string(line.strip()) for line in fp]


def part1(positions: list[Position], width: int, height: int, n: int) -> int:
    grid = Grid(width, height, ["."] * width * height)
    for p in positions[:n]:
        grid.set(p, "#")

    g = Graph()
    for x in range(grid.width):
        for y in range(grid.height):
            p = Position(x, y)
            if grid.get(p) != "#":
                for neighbour in grid.neighbours(p):
                    if grid.get(neighbour) != "#":
                        g.add_edge((p.x, p.y), (neighbour.x, neighbour.y))

    try:
        return len(shortest_path(g, (0, 0), (grid.width - 1, grid.height - 1))) - 1
    except NetworkXNoPath as _:
        return 0


# Completes in less than a minute. Can probably run in seconds if integrated in part1.
def part2(positions: list[Position], width: int, height: int) -> str | None:
    for n in range(len(positions)):
        if part1(positions, width, height, n) == 0:
            return str(positions[n - 1].x) + "," + str(positions[n - 1].y)


if __name__ == "__main__":
    print("Test1:", part1(read_input("day18_test.txt"), 7, 7, 12))
    print("Test2:", part2(read_input("day18_test.txt"), 7, 7))
    print("Part1:", part1(read_input("day18.txt"), 71, 71, 1024))
    print("Part2:", part2(read_input("day18.txt"), 71, 71))
