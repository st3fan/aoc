#!/usr/bin/env python


import json

from dataclasses import dataclass
from functools import cmp_to_key
from typing import Any, Generator, List, Self


def _compare_lists(left: List[Any], right: List[Any]) -> int:
    print("COMPARING", left, "WITH", right)
    for i in range(max(len(left), len(right))):
        # If the left list ran out of items, we're good
        if len(left) < len(right) and i == len(left):
            return 1
        # If the right list ran out of items, we're not good
        if len(right) < len(left) and i == len(right):
            return -1
        # If both items are integers then the lower should come first
        if isinstance(left[i], int) and isinstance(right[i], int):
            if right[i] != left[i]:
                return right[i] - left[i]
        else:
            # If one item is an int and the other is a list ...
            l = left[i] if isinstance(left[i], list) else [left[i]]
            r = right[i] if isinstance(right[i], list) else [right[i]]
            if (result := _compare_lists(l, r)) != 0:
                return result
    return 0


@dataclass
class Pair:
    left: List[Any]
    right: List[Any]

    def correct(self) -> bool:
        return _compare_lists(self.left, self.right) == True

    @classmethod
    def from_str(cls, s: str) -> Self:
        left, right = s.split("\n")
        return cls(json.loads(left), json.loads(right))


def read_input() -> Generator[Pair, None, None]:
    for packet in open("day13.txt").read().split("\n\n"):
        yield Pair.from_str(packet)


def part1() -> int:
    return sum(i for i, pair in enumerate(read_input(), start=1) if _compare_lists(pair.left, pair.right) > 0)


def part2() -> int:
    packets = [[[2]], [[6]]]
    for packet in read_input():
        packets.append(packet.left)
        packets.append(packet.right)

    packets = sorted(packets, key=cmp_to_key(_compare_lists), reverse=True)

    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
