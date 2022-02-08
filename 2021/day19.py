#!/usr/bin/env python3


from dataclasses import dataclass
from typing import List

from more_itertools import split_at


@dataclass
class Beacon:
    x: int
    y: int
    z: int

    @classmethod
    def from_string(cls, s):
        [x, y, z] = [int(e) for e in s.split(",")]
        return cls(x, y, z)


@dataclass
class Scanner:
    id: int
    beacons: List[Beacon]

    @classmethod
    def from_string(cls, s):
        lines = s.split("\n")
        id = int(lines[0].split(" ")[2])
        return cls(id, [Beacon.from_string(line.strip()) for line in lines[1:]])


def load():
    return [Scanner.from_string(chunk.strip()) for chunk in open("day19.input").read().split("\n\n")]


if __name__ == "__main__":
    print(load())


