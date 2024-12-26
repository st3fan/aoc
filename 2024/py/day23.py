#!/usr/bin/env python

import networkx as nx
from more_itertools import last


def read_input(path: str) -> nx.Graph:
    with open(path) as fp:
        g = nx.Graph()
        for line in fp:
            c = line.strip().split("-")
            g.add_edge(c[0], c[1])
        return g


def part1(g: nx.Graph) -> int:
    return sum(len(c) == 3 and any(n[0] == "t" for n in c) for c in nx.enumerate_all_cliques(g))


def part2(g: nx.Graph) -> str:
    return ",".join(sorted(last(nx.enumerate_all_cliques(g))))


if __name__ == "__main__":
    print("Part1:", part1(read_input("day23.txt")))
    print("Part2:", part2(read_input("day23.txt")))
