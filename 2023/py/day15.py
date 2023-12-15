#!/usr/bin/env python


import re

from collections import OrderedDict
from dataclasses import dataclass, field
from functools import reduce
from typing import List, OrderedDict


def read_input() -> List[str]:
    return open("day15.txt").read().strip().split(",")


def hash_string(s: str) -> int:
    return reduce(lambda a, c: ((a + ord(c)) * 17) % 256, s, 0)


def part1() -> int:
    return sum(hash_string(s) for s in read_input())


@dataclass
class Box:
    id: int
    lenses: OrderedDict[str, int] = field(default_factory=OrderedDict)

    def focal_power(self) -> int:
        return sum(
            (self.id + 1) * slot * focal_length
            for slot, focal_length in enumerate(self.lenses.values(), 1)
        )

    def add_lens(self, label: str, focal_length: int):
        self.lenses[label] = focal_length

    def remove_lens(self, label: str):
        if label in self.lenses:
            del self.lenses[label]


def part2() -> int:
    boxes = [Box(i) for i in range(0, 256)]
    for s in read_input():
        match re.findall(r"(\w+|-|=)", s):
            case [label, "-"]:
                boxes[hash_string(label)].remove_lens(label)
            case [label, "=", focal_length]:
                boxes[hash_string(label)].add_lens(label, int(focal_length))
    return sum(box.focal_power() for box in boxes)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
