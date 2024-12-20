#!/usr/bin/env python


from collections import Counter
from pprint import pprint

import networkx as nx

from aoc import Grid, Position


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
            source = (start.x, start.y)
            target = (end.x, end.y)
            for x in range(1, grid.width - 1):
                for y in range(1, grid.height - 1):
                    p = Position(x, y)

                    if grid.get(p) == "#":
                        new_edges = []
                        for n in grid.neighbours(p):
                            if grid.get(n) in (".", "S", "E"):
                                e = ((p.x, p.y), (n.x, n.y))
                                new_edges.append(e)
                                g.add_edge(e[0], e[1])

                        steps.update([len(nx.shortest_path(g, source=source, target=target)) - 1])

                        for e in new_edges:
                            g.remove_edge(e[0], e[1])

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
