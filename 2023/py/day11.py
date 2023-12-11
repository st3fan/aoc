#!/usr/bin/env python


from itertools import combinations
from typing import Iterator, List, Set, Tuple


def read_input() -> List[List[str]]:
    return [list(line) for line in open("day11.txt").read().strip().split("\n")]


# Simple approach


def expand(galaxy: List[List[str]], n: int = 1) -> List[List[str]]:
    result = []
    for line in galaxy:
        if all(v == "." for v in line):
            for _ in range(n):
                result.append(line)
        result.append(line)
    galaxy = list(zip(*result[::-1]))

    result = []
    for line in galaxy:
        if all(v == "." for v in line):
            for _ in range(n):
                result.append(line)
        result.append(line)
    galaxy = list(zip(*result[::-1]))

    return galaxy


def planet_locations(galaxy: List[List[str]]) -> Iterator[Tuple[int, int]]:
    result = []
    for y in range(len(galaxy)):
        for x in range(len(galaxy[0])):
            if galaxy[y][x] == "#":
                yield (x, y)


def manhattan_distance1(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve1(galaxy: List[List[str]]) -> int:
    return sum(
        manhattan_distance1(a, b) for a, b in combinations(planet_locations(galaxy), 2)
    )


def part1() -> int:
    return solve1(expand(read_input(), n=1))


# New approach >:-)


def find_spaces(galaxy: List[List[str]]) -> Tuple[Set[int], Set[int]]:
    vspaces = set()
    for i, line in enumerate(galaxy):
        if all(v == "." for v in line):
            vspaces.add(i)

    hspaces = set()
    galaxy = list(zip(*galaxy[::-1]))
    for i, line in enumerate(galaxy):
        if all(v == "." for v in line):
            hspaces.add(i)

    galaxy = list(zip(*galaxy[::-1]))
    return hspaces, vspaces


def manhattan_distance2(
    a: Tuple[int, int],
    b: Tuple[int, int],
    xspaces: Set[int],
    yspaces: Set[int],
    n: int,
) -> int:
    distance = abs(a[0] - b[0]) + abs(a[1] - b[1])

    def _sort(a, b) -> Tuple[int, int]:
        return (a, b) if a < b else (b, a)

    xs, xe = _sort(a[0], b[0])
    xc = len([x for x in xspaces if x > xs and x < xe])

    ys, ye = _sort(a[1], b[1])
    yc = len([y for y in yspaces if y > ys and y < ye])

    return distance + n * (xc + yc)


def part2() -> int:
    galaxy = read_input()
    xspaces, yspaces = find_spaces(galaxy)

    return sum(
        manhattan_distance2(a, b, xspaces, yspaces, 999_999)
        for a, b in combinations(planet_locations(galaxy), 2)
    )


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
