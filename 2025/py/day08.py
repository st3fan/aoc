#!/usr/bin/env python3

import math
from dataclasses import dataclass
from itertools import combinations
from typing import Self


@dataclass(frozen=True)
class Pos:
    x: int
    y: int
    z: int

    @classmethod
    def from_str(cls, s) -> Self:
        c = s.split(",")
        return cls(x=int(c[0]), y=int(c[1]), z=int(c[2]))


def distance(p1: Pos, p2: Pos) -> float:
    return math.dist((p1.x, p1.y, p1.z), (p2.x, p2.y, p2.z))


def merge_overlapping_sets(sets):
    merged = []
    for s in sets:
        connected = []
        for m in merged:
            if s & m:
                s = s | m
            else:
                connected.append(m)
        connected.append(s)
        merged = connected
    return merged


def part1(input: list[Pos], n: int) -> int:
    # Make a list with ((p1,p2),distance)
    distances = []
    for p1, p2 in combinations(input, 2):
        distances.append(((p1, p2), distance(p1, p2)))

    # Take the top N closest
    distances.sort(key=lambda e: e[1])
    closest = [set(list(e[0])) for e in distances[:n]]

    # Merge the (p1,p2) pairs
    merged = merge_overlapping_sets(closest)

    # Find the largest clusters
    larges_sizes = [len(m) for m in merged]
    larges_sizes.sort(key=lambda e: e, reverse=True)

    return math.prod(larges_sizes[:3])


#


def merge_all(sets: list[set[Pos]], n: int):
    merged = []
    for s in sets:
        f = s.copy()
        connected = []
        for m in merged:
            if s & m:  # overlap exists
                s = s | m
            else:
                connected.append(m)
        connected.append(s)
        merged = connected
        # If there is now one cluster and it contains n items
        if len(merged) == 1 and len(list(merged)[0]) == n:
            items = list(f)
            return items[0].x * items[1].x

    raise Exception("Could not find a solution?")


def part2(input: list[Pos]) -> int:
    # Make a list with ((p1,p2),distance)
    distances = []
    for p1, p2 in combinations(input, 2):
        distances.append(((p1, p2), distance(p1, p2)))

    # Take them all
    distances.sort(key=lambda e: e[1])
    closest = [set(list(e[0])) for e in distances]

    # Merge all and return the last merged
    return merge_all(closest, len(input))


def read_input(path: str) -> list[Pos]:
    with open(path) as fp:
        return [Pos.from_str(line.strip()) for line in fp.readlines()]


if __name__ == "__main__":
    input = read_input("day08_input.txt")
    print("Part 1:", part1(input, 1000))
    print("Part 2:", part2(input))
