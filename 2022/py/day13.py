#!/usr/bin/env python


import json
import re

from dataclasses import dataclass
from typing import Any, Generator, List, Self
from more_itertools import padded


def _parse_list(s: str) -> List[Any]:
    # return json.loads(re.sub(r"(\d+)", r"[\1]", s))
    return json.loads(s)


# def test_parse_list():
#     assert _parse_list("[]") == []
#     assert _parse_list("[1]") == [[1]]
#     assert _parse_list("[1,2]") == [[1], [2]]
#     assert _parse_list("[1,[], 3]") == [[1], [], [3]]
#     assert _parse_list("[[], 2, 3]") == [[], [2], [3]]
#     assert _parse_list("[[8, 7, 6]]") == [[[8], [7], [6]]]


def _compare_listsx(l: List[Any], r: List[Any]) -> bool:
    # print("COMPARING", l, r)
    for left, right in zip(padded(l, None, max(len(l), len(r))), padded(r, None, max(len(l), len(r)))):
        match (left, right):
            case (int(left), int(right)):
                if left > right:
                    return False
            case (None, int(right)):
                return True
            case (int(left), None):
                return False
            case (list(ll), list(rl)):
                if not _compare_lists(ll, rl):
                    return False
            case (list(ll), int(ri)):
                if not _compare_lists(ll, [ri]):
                    return False
            case (int(li), list(rl)):
                if not _compare_lists([li], rl):
                    return False
            case _:
                raise Exception(f"Don't know how to compare {left} vs {right}")
    return True


def _compare_lists(left: List[Any] | int, right: List[Any] | int) -> bool:
    # print("COMPARING", left, "WITH", right)
    if isinstance(left, list) and isinstance(right, list):
        for i in range(max(len(left), len(right))):
            # If the left list ran out of items, we're good
            if len(left) < len(right) and i == len(left):
                return True
            # If the right list ran out of items, we're not good
            elif len(right) < len(left) and i == len(right):
                return False
            # If both items are integers then the lower should come first
            elif isinstance(left[i], int) and isinstance(right[i], int):
                if left[i] < right[i]:
                    return True
                elif left[i] > right[i]:
                    return False
            # If one item is an int and the other is a list ...
            elif isinstance(left[i], int) and isinstance(right[i], list):
                return _compare_lists([left[i]], right[i])
            elif isinstance(left[i], list) and isinstance(right[i], int):
                return _compare_lists(left[i], [right[i]])

    return False


def test_compare_lists1():
    assert _compare_lists([1, 1, 3, 1, 1], [1, 1, 5, 1, 1])


def test_compare_lists2():
    assert _compare_lists([[1], [2, 3, 4]], [[1], 4])


def test_compare_lists3():
    assert _compare_lists([9], [[8, 7, 6]]) == False


def test_compare_lists4():
    assert _compare_lists([[4, 4], 4, 4], [[4, 4], 4, 4, 4])


def test_compare_lists5():
    assert _compare_lists([7, 7, 7, 7], [7, 7, 7]) == False


def test_compare_lists6():
    assert _compare_lists([], [3])


def test_compare_lists7():
    assert _compare_lists([[[]]], [[]]) == False


def test_compare_lists8():
    assert _compare_lists([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]) == False


@dataclass
class Pair:
    left: List[Any]
    right: List[Any]

    def correct(self) -> bool:
        return _compare_lists(self.left, self.right)

    @classmethod
    def from_str(cls, s: str) -> Self:
        left, right = s.split("\n")
        return cls(_parse_list(left), _parse_list(right))


def read_input() -> Generator[Pair, None, None]:
    for packet in open("day13.txt").read().split("\n\n"):
        yield Pair.from_str(packet)


def part1() -> int:
    return sum(i for i, pair in enumerate(read_input(), start=1) if _compare_lists(pair.left, pair.right))


def part2() -> int:
    return 0


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
