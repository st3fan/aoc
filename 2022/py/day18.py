#!/usr/bin/env python


from dataclasses import dataclass
from typing import List, NamedTuple, Self, Set

import numpy as np
from scipy import ndimage

# @dataclass(frozen=True)
# class Cube:
#     x: int
#     y: int
#     z: int

#     @classmethod
#     def from_str(cls, s: str) -> Self:
#         c = s.split(",")
#         return cls(int(c[0]), int(c[1]), int(c[2]))

#     def adjecents(self) -> List[Self]:
#         return [
#             Cube(self.x - 1, self.y, self.z),
#             Cube(self.x + 1, self.y, self.z),
#             Cube(self.x, self.y - 1, self.z),
#             Cube(self.x, self.y + 1, self.z),
#             Cube(self.x, self.y, self.z - 1),
#             Cube(self.x, self.y, self.z + 1),
#         ]


class Cube(NamedTuple):
    x: int
    y: int
    z: int

    @classmethod
    def from_str(cls, s: str) -> Self:
        c = s.split(",")
        return cls(int(c[0]), int(c[1]), int(c[2]))

    def adjecents(self) -> List[Self]:
        return [
            Cube(self.x - 1, self.y, self.z),
            Cube(self.x + 1, self.y, self.z),
            Cube(self.x, self.y - 1, self.z),
            Cube(self.x, self.y + 1, self.z),
            Cube(self.x, self.y, self.z - 1),
            Cube(self.x, self.y, self.z + 1),
        ]


def read_input() -> Set[Cube]:
    return set(Cube.from_str(line.strip()) for line in open("day18.txt").readlines())


def outer_surface(cubes: set[Cube]) -> int:
    total = 0
    for cube in cubes:
        for adj in cube.adjecents():
            if adj not in cubes:
                total += 1
    return total


def part1() -> int:
    return outer_surface(read_input())


def part2() -> int:
    cubes: Set[Cube] = read_input()

    mx = max(c.x for c in cubes) + 1
    my = max(c.y for c in cubes) + 1
    mz = max(c.z for c in cubes) + 1

    array = np.zeros((mx, my, mz), dtype=int)
    for cube in cubes:
        array[cube] = 1

    inside = ndimage.binary_fill_holes(array).astype(int) - array

    inside_cubes: Set[Cube] = set()
    for x in range(mx):
        for y in range(my):
            for z in range(mz):
                if inside[x, y, z] != 0:
                    inside_cubes.add(Cube(x, y, z))

    return part1() - outer_surface(inside_cubes)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
