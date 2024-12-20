#!/usr/bin/env python


from __future__ import annotations

import networkx as nx

from aoc import Grid, Position


def read_input(path: str) -> tuple[nx.DiGraph, Position, Position]:
    g = nx.DiGraph()
    grid = Grid.from_file(path, lambda c: c)
    for x in range(grid.width):
        for y in range(grid.height):
            p = Position(x, y)
            if grid.get(p) in (".", "S", "E"):
                for neighbour in grid.neighbours(p):
                    if grid.get(neighbour) in (".", "S", "E"):
                        g.add_edge((p.x, p.y), (neighbour.x, neighbour.y), weight=50)
    return g, grid.find("S"), grid.find("E")  # pyright: ignore


def score1(path: list[tuple[int, int]]) -> int:
    return len(path) - 1


def part1() -> int:
    graph, start, end = read_input("day16.txt")

    nx.all_simple_paths

    # for p in nx.all_shortest_paths(graph, (start.x, start.y), (end.x, end.y), weight="weight", method="bellman-ford"):
    #     print(len(list(p)))

    for p in nx.all_simple_edge_paths(graph, (start.x, start.y), (end.x, end.y)):
        print(len(list(p)))

    return 0


if __name__ == "__main__":
    print("Part1:", part1())
