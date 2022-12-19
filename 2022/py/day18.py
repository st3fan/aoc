#!/usr/bin/env python


from typing import List, Set, Tuple

import numpy as np
from scipy import ndimage


def adjecents(cube: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
    return [
        (cube[0] - 1, cube[1] + 0, cube[2] + 0),
        (cube[0] + 1, cube[1] + 0, cube[2] + 0),
        (cube[0] + 0, cube[1] - 1, cube[2] + 0),
        (cube[0] + 0, cube[1] + 1, cube[2] + 0),
        (cube[0] + 0, cube[1] + 0, cube[2] - 1),
        (cube[0] + 0, cube[1] + 0, cube[2] + 1),
    ]


def read_input() -> Set[Tuple[int, int, int]]:
    def _parse_cube(s: str) -> Tuple[int, int, int]:
        c = s.split(",")
        return (int(c[0]), int(c[1]), int(c[2]))

    return set(_parse_cube(line) for line in open("day18.txt").readlines())


def outer_surface(cubes: Set[Tuple[int, int, int]]) -> int:
    return sum(sum(1 for adj in adjecents(cube) if adj not in cubes) for cube in cubes)


def part1() -> int:
    return outer_surface(read_input())


def part2() -> int:
    cubes: Set[Tuple[int, int, int]] = read_input()

    mx = max(c[0] for c in cubes) + 1
    my = max(c[1] for c in cubes) + 1
    mz = max(c[2] for c in cubes) + 1

    array = np.zeros((mx, my, mz), dtype=int)
    for cube in cubes:
        array[cube] = 1

    inside = ndimage.binary_fill_holes(array) - array
    inside_cubes = set([i for i, v in np.ndenumerate(inside) if v != 0])

    return part1() - outer_surface(inside_cubes)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
