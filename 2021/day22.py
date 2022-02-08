#!/usr/bin/env python3


import operator
import re
from dataclasses import dataclass, field
from typing import List


@dataclass
class RebootStep:
    on: bool
    xs: int
    xe: int
    ys: int
    ye: int
    zs: int
    ze: int
    v: int = field(init=False)

    @classmethod
    def from_string(cls, s: str):
        if m := re.match(r"^(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)$", s):
            return cls(m[1] == "on", int(m[2]), int(m[3]), int(m[4]), int(m[5]), int(m[6]), int(m[7]))

    def __post_init__(self):
        self.v = (self.xe - self.xs) * (self.ye - self.ys) * (self.ze - self.zs)


def load() -> List[RebootStep]:
    return [RebootStep.from_string(line.strip()) for line in open("day22.example").readlines()]


def part1():
    grid = dict()
    for s in load():
        print(s)
        for x in range(max(s.xs, -50), min(s.xe+1, 51)):
            for y in range(max(s.ys, -50), min(s.ye+1, 51)):
                for z in range(max(s.zs, -50), min(s.ze+1, 51)):
                    grid[(x,y,z)] = s.on
        print(sum(grid.values()))


def part2():
    only_on = [s for s in load() if s.on]
    only_on = sorted(only_on, key=operator.attrgetter("v"), reverse=True)

    b = only_on[0]
    print(b)
    
    for s in only_on[1:]:
        if s.xs < b.xs or s.xe > b.xe:
            print("Nope")


if __name__ == "__main__":
    #print("Part one:", part1())
    print("Part two:", part2())
