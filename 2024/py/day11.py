#!/usr/bin/env python

from functools import cache
from math import floor, log10

INPUT = (92, 0, 286041, 8034, 34394, 795, 8, 2051489)

ROUNDS1 = 25
ROUNDS2 = 75


@cache
def apply_rules(n: int) -> list[int]:
    if n == 0:
        return [1]
    else:
        digits = floor(log10(n)) + 1
        if digits % 2 == 0:
            div = 10 ** (digits // 2)
            first, second = divmod(n, div)
            return [first, second]
        else:
            return [n * 2024]


@cache
def blink(numbers: tuple[int], max_depth: int, current_depth: int) -> int:
    if current_depth >= max_depth:
        return len(numbers)

    total = 0
    for number in numbers:
        total += blink(tuple(apply_rules(number)), max_depth, current_depth + 1)

    return total


if __name__ == "__main__":
    print("Part1", blink(INPUT, max_depth=ROUNDS1, current_depth=0))
    print("Part2", blink(INPUT, max_depth=ROUNDS2, current_depth=0))
