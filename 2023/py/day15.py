#!/usr/bin/env python


import re

from collections import OrderedDict
from dataclasses import dataclass, field
from typing import List, OrderedDict


def read_input() -> List[str]:
    return open("day15.txt").read().strip().split(",")


def hash_string(s: str) -> int:
    t = 0
    for c in s:
        t += ord(c)
        t *= 17
        t %= 256
    return t


def part1() -> int:
    # return hash_string("HASH")
    return sum(hash_string(s) for s in read_input())


@dataclass
class Box:
    id: int
    lenses: OrderedDict[str, int] = field(default_factory=OrderedDict)

    def focal_power(self) -> int:
        t = 0
        for slot, (lens_label, focal_length) in enumerate(self.lenses.items(), 1):
            t += (self.id + 1) * slot * focal_length
        return t

    def add_lens(self, label: str, focal_length: int):
        self.lenses[label] = focal_length

    def remove_lens(self, label: str):
        if label in self.lenses:
            del self.lenses[label]
        # if label in self.lenses:
        #     keys = list(self.lenses.keys())
        #     for key in keys[keys.index(label) :]:
        #         del self.lenses[key]


def part2() -> int:
    boxes = [Box(i) for i in range(0, 256)]

    for s in read_input():
        match re.findall(r"(\w+|-|=)", s):
            case [label, "-"]:
                boxes[hash_string(label)].remove_lens(label)
            case [label, "=", focal_length]:
                boxes[hash_string(label)].add_lens(label, int(focal_length))

    # boxes[0].lenses["a"] = 1
    # boxes[0].lenses["b"] = 2
    # boxes[3].lenses["a"] = 7
    # boxes[3].lenses["b"] = 5
    # boxes[3].lenses["c"] = 6

    return sum(box.focal_power() for box in boxes)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
