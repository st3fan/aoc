#!/usr/bin/env python

from functools import cache
from math import floor, log10

INPUT = (92, 0, 286041, 8034, 34394, 795, 8, 2051489)


@cache
def apply_rules(n: int) -> list[int]:
    if n == 0:
        return [1]

    if (digits := floor(log10(n)) + 1) and digits % 2 == 0:
        div = 10 ** (digits // 2)
        first, second = divmod(n, div)
        return [first, second]

    return [n * 2024]


@cache
def blink(numbers: tuple[int], rounds: int) -> int:
    if rounds == 0:
        return len(numbers)

    total = 0
    for number in numbers:
        total += blink(tuple(apply_rules(number)), rounds - 1)
    return total


if __name__ == "__main__":
    print("Part1", blink(INPUT, rounds=25))
    print("Part2", blink(INPUT, rounds=75))
