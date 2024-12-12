#!/usr/bin/env python

import math
from itertools import batched

INPUT = [92, 0, 286041, 8034, 34394, 795, 8, 2051489]

ROUNDS1 = 25
ROUNDS2 = 75


def transform_list(numbers: list[int]) -> list[int]:
    result = []
    for n in numbers:
        if n == 0:
            result.append(1)
        else:
            digits = math.floor(math.log10(n)) + 1
            if digits % 2 == 0:
                div = 10 ** (digits // 2)
                first, second = divmod(n, div)
                result += [first, second]
            else:
                result.append(n * 2024)
    return result


CACHE = {}


def blink(numbers: list[int], max_depth: int, current_depth: int):
    if current_depth >= max_depth:
        return len(numbers)

    # Lame this only exists because the functools.cache decorator can't handle lists and arguments to ignore.
    key = ",".join([str(v) for v in numbers]) + ":" + str(current_depth)

    # The caching happens here because we want to avoid recursion and the transform_list function
    if r := CACHE.get(key):
        return r

    # Transform the list
    total = 0
    for batch in batched(numbers, 1):  # Why do we get the best results with batch size 1?!
        total += blink(transform_list(list(batch)), max_depth, current_depth + 1)

    CACHE[key] = total

    return total


if __name__ == "__main__":
    CACHE = {}
    print("Part1", blink(INPUT, max_depth=ROUNDS1, current_depth=0))
    CACHE = {}
    print("Part2", blink(INPUT, max_depth=ROUNDS2, current_depth=0))
