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
    return


def part1(grid: Grid) -> int:
    steps = Counter()

    g = nx.Graph()
    for x in range(grid.width):
        for y in range(grid.height):
            p = Position(x, y)
            if grid.get(p) in (".", "S", "E"):
                for neighbour in grid.neighbours(p):
                    if grid.get(neighbour) in (".", "S", "E"):
                        g.add_edge((p.x, p.y), (neighbour.x, neighbour.y))

    if start := grid.find("S"):
        if end := grid.find("E"):
            for x in range(1, grid.width - 1):
                for y in range(1, grid.height - 1):
                    p = Position(x, y)

                    if grid.get(p) == "#":
                        neighbours = grid.neighbours(p)
                        for n in neighbours:
                            if grid.get(n) in (".", "S", "E"):
                                g.add_edge((p.x, p.y), (n.x, n.y))

                        c = len(nx.shortest_path(g, source=(start.x, start.y), target=(end.x, end.y))) - 1
                        steps.update([c])

                        for n in neighbours:
                            try:
                                g.remove_edge((p.x, p.y), (n.x, n.y))
                            except:
                                pass

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

    t = 0
    for s, n in savings.items():
        if s >= 100:
            t += n

    print("TOTAL", t)

    return t


if __name__ == "__main__":
    grid = Grid.from_file("day20.txt", lambda v: v)
    print("Part1:", part1(grid))
