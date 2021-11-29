#!/usr/bin/env python3


from hashlib import md5
from itertools import count, islice


INPUT = "uqwqemis"


def generate_hashes(prefix):
    for n in count():
        d = md5(bytes(f"{prefix}{n}", "ascii")).hexdigest()
        if d.startswith("00000"):
            yield d


def part1():
    return "".join([h[5] for h in islice(generate_hashes(INPUT), 8)])


def part2():
    result = [None] * 8
    for h in generate_hashes(INPUT):
        position = int(h[5], 16)
        if position < 8 and not result[position]:
            result[position] = h[6]
        if None not in result:
            break
    return "".join(result)


if __name__ == "__main__":
    print("Part one:", part1())
    print("Part two:", part2())
