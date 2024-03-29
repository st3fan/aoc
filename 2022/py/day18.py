#!/usr/bin/env python


from typing import List, Set, Tuple, TypeAlias

import numpy as np
from scipy import ndimage

Cube: TypeAlias = Tuple[int, int, int]


def adjecents(cube: Cube) -> List[Cube]:
    return [
        (cube[0] - 1, cube[1] + 0, cube[2] + 0),
        (cube[0] + 1, cube[1] + 0, cube[2] + 0),
        (cube[0] + 0, cube[1] - 1, cube[2] + 0),
        (cube[0] + 0, cube[1] + 1, cube[2] + 0),
        (cube[0] + 0, cube[1] + 0, cube[2] - 1),
        (cube[0] + 0, cube[1] + 0, cube[2] + 1),
    ]


def read_input() -> Set[Cube]:
    def _parse_cube(s: str) -> Cube:
        c = s.split(",")
        return (int(c[0]), int(c[1]), int(c[2]))

    return set(_parse_cube(line) for line in open("day18.txt").readlines())


def outer_surface(cubes: Set[Cube]) -> int:
    return sum(sum(adj not in cubes for adj in adjecents(cube)) for cube in cubes)


def part1() -> int:
    return outer_surface(read_input())


def part2() -> int:
    all_cubes: Set[Cube] = read_input()

    droplet = np.zeros((100, 100, 100), dtype=int)
    for cube in all_cubes:
        droplet[cube] = 1

    pockets = ndimage.binary_fill_holes(droplet) - droplet
    inside_cubes: Set[Cube] = set([i for i, v in np.ndenumerate(pockets) if v != 0])

    return outer_surface(all_cubes) - outer_surface(inside_cubes)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
