#!/usr/bin/env python


from dataclasses import dataclass
from itertools import chain
from typing import Generator, List, Set
from functools import reduce
from more_itertools import chunked


def item_id(s: str) -> int:
    if ord(s) >= ord('a') and ord(s) <= ord('z'):
        return ord(s) - ord('a') + 1
    return ord(s) - ord('A') + 27


@dataclass
class Rucksack:
    left: List[int]
    right: List[int]

    def all_items(self) -> Set[int]:
        return set(self.left) | set(self.right)

    def unique_items(self) -> Set[int]:
        return set(self.left) & set(self.right)

    @staticmethod
    def from_string(s: str) -> "Rucksack":
        mid = len(s) // 2
        return Rucksack([item_id(i) for i in s[:mid]], [item_id(i) for i in s[mid:]])


def read_input() -> Generator[Rucksack, None, None]:
    with open("day3.txt") as f:
        for line in f.readlines():
            yield Rucksack.from_string(line.strip())


def part1() -> int:
    return sum(
        chain.from_iterable(
            rucksack.unique_items() for rucksack in read_input()
        )
    )


def part2() -> int:
    return sum(
        chain.from_iterable(
            [reduce(lambda a, b: a & b, [rucksack.all_items() for rucksack in group])
                for group in chunked(read_input(), 3)]
        )
    )


if __name__ == "__main__":
    print("Part1:", part1())
    print("Part2:", part2())
