#!/usr/bin/env python3


from collections import Counter
from dataclasses import dataclass
import operator
import re


@dataclass
class Room:
    name: str
    sector: int
    hash: str

    def valid(self):
        counts = Counter(c for c in self.name if c.isalpha()).most_common()
        #print(counts)
        counts = sorted(counts, key=lambda e: (-e[1], e[0]))
        #print(counts)
        expected_hash = "".join([e[0] for e in counts])[:5]
        return self.hash == expected_hash

    def decrypt(self):
        result = ""
        for c in self.name:
            if c == "-":
                result += " "
            else:
                result += chr(ord("a") + (ord(c) - ord("a") + self.sector) % 26)
        return result


    @classmethod
    def from_string(cls, s):
        """Create a Room from a string. Including decoys."""
        if m := re.match(r"(.+)-(\d+)\[(.+)\]", s):
            name, sector, hash = m.group(1), m.group(2), m.group(3)
            return cls(name, int(sector), hash)


def part1():
    rooms = [Room.from_string(line) for line in open("day4.input").readlines()]
    return sum([r.sector for r in rooms if r.valid()])


def part2():
    rooms = [Room.from_string(line) for line in open("day4.input").readlines()]
    for r in rooms:
        if r.valid() and r.decrypt() == "northpole object storage":
            return r.sector


if __name__ == "__main__":
    print("Part one:", part1())
    print("Part two:", part2())

