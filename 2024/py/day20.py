#!/usr/bin/env python


from collections import Counter
from pprint import pprint

import networkx as nx

from aoc import Grid, Position


def shortest_path(grid: Grid, start: Position, end: Position) -> int:
    g = nx.Graph()
    for x in range(grid.width):
        for y in range(grid.height):
            p = Position(x, y)
            if grid.get(p) in (".", "S", "E"):
                for neighbour in grid.neighbours(p):
                    if grid.get(neighbour) in (".", "S", "E"):
                        g.add_edge((p.x, p.y), (neighbour.x, neighbour.y))
    return len(nx.shortest_path(g, source=(start.x, start.y), target=(end.x, end.y))) - 1


def part1(grid: Grid) -> int:
    steps = Counter()
    if start := grid.find("S"):
        if end := grid.find("E"):
            for x in range(1, grid.width - 1):
                for y in range(1, grid.height - 1):
                    p = Position(x, y)
                    if grid.get(p) == "#":
                        grid.set(p, ".")
                        c = shortest_path(grid, start, end)
                        steps.update([c])
                        grid.set(p, "#")

                        # for n in grid.neighbours(p):
                        #     o = grid.get(n)
                        #     if o in (".", "E"):
                        #         grid.set(n, ".")
                        #         c = shortest_path(grid, start, end)
                        #         steps.update([c])
                        #         grid.set(n, o)

    # pprint(steps)

    savings = {}
    for s, n in steps.items():
        c = max(steps.keys()) - s
        if c != 0:
            savings[c] = n

    pprint(savings, indent=3)

    return 0


if __name__ == "__main__":
    grid = Grid.from_file("day20_test.txt", lambda v: v)
    print("Part1:", part1(grid))
