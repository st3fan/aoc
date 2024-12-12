#!/usr/bin/env python

from functools import cache
from itertools import batched
from math import floor, log10

INPUT = (92, 0, 286041, 8034, 34394, 795, 8, 2051489)

ROUNDS1 = 25
ROUNDS2 = 75


def transform_list(numbers: list[int]) -> list[int]:
    result = []
    for n in numbers:
        if n == 0:
            result.append(1)
        else:
            digits = floor(log10(n)) + 1
            if digits % 2 == 0:
                div = 10 ** (digits // 2)
                first, second = divmod(n, div)
                result += [first, second]
            else:
                result.append(n * 2024)
    return result


@cache
def blink(numbers: tuple[int], max_depth: int, current_depth: int) -> int:
    if current_depth >= max_depth:
        return len(numbers)

    # Why do we get the best results with batch size 1?! Does that
    # mean all the slowness is really in transform_list?

    total = 0
    for batch in batched(numbers, 1):
        total += blink(tuple(transform_list(list(batch))), max_depth, current_depth + 1)

    return total


if __name__ == "__main__":
    print("Part1", blink(INPUT, max_depth=ROUNDS1, current_depth=0))
    print("Part2", blink(INPUT, max_depth=ROUNDS2, current_depth=0))
