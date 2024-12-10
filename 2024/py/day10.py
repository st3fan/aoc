#!/usr/bin/env python3

from itertools import product

import networkx as nx


def load_points(path: str) -> dict[tuple[int, int], int]:
    points = {}
    with open(path) as fp:
        for y, line in enumerate(fp):
            for x, c in enumerate(line.strip()):
                points[(x, y)] = int(c)
        return points


def build_graph(points: dict[tuple[int, int], int]) -> nx.Graph:
    w = max(p[0] for p in points.keys())
    h = max(p[1] for p in points.keys())

    g = nx.DiGraph()
    for x1, y1, x2, y2 in product(*[range(w + 1), range(h + 1), range(w + 1), range(h + 1)]):
        if (x1, y1) != (x2, y2) and (abs(x1 - x2) + abs(y1 - y2)) == 1:
            if points[(x2, y2)] == (points[(x1, y1)] + 1):
                g.add_edge((x1, y1), (x2, y2))
    return g


def part1(path: str) -> int:
    points = load_points(path)
    graph = build_graph(points)
    unique = set()
    for start in [k for k, v in points.items() if v == 0]:
        for end in [k for k, v in points.items() if v == 9]:
            if any(nx.all_simple_paths(graph, start, end)):
                unique.add((start, end))
    return len(unique)


def part2(path: str) -> int:
    points = load_points(path)
    graph = build_graph(points)
    total = 0
    for start in [k for k, v in points.items() if v == 0]:
        for end in [k for k, v in points.items() if v == 9]:
            total += len(list(nx.all_simple_paths(graph, start, end)))
    return total


if __name__ == "__main__":
    print("Part1", part1("day10.txt"))
    print("Part2", part2("day10.txt"))
