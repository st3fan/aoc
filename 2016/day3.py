#!/usr/bin/env python3


from dataclasses import dataclass
from itertools import chain
from typing import List


@dataclass
class Triangle:
    a: int
    b: int
    c: int

    @classmethod
    def from_str(cls, s: str) -> "Triangle":
        e = s.split()
        return Triangle(int(e[0]), int(e[1]), int(e[2]))

    @property
    def is_valid(self) -> bool:
        return (self.a+self.b) > self.c and (self.b+self.c) > self.a and (self.a+self.c) > self.b


def read_input1() -> List[Triangle]:
    return [Triangle.from_str(s.strip()) for s in open("day3.input").readlines()]


def read_input2() -> List[Triangle]:
    # Horrible!
    values = list(chain.from_iterable([int(s) for s in line.strip().split()] for line in open("day3.input").readlines()))
    result = []
    for i in range(0, len(values)-1, 9):
        result.append(Triangle(values[i+0], values[i+3], values[i+6]))
        result.append(Triangle(values[i+1], values[i+4], values[i+7]))
        result.append(Triangle(values[i+2], values[i+5], values[i+8]))
    return result


def part1():
    return sum(t.is_valid for t in read_input1())


def part2():
    return sum(t.is_valid for t in read_input2())


if __name__ == "__main__":
    print("Part one:", part1())
    print("Part two:", part2())
