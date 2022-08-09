#!/usr/bin/env python3


from collections import Counter
from itertools import combinations


def load():
    return [line.strip() for line in open("day2.input").readlines()]


def part1():
    twos = 0
    threes = 0
    for id in load():
        c = Counter(id)
        if 2 in c.values():
            twos += 1
        if 3 in c.values():
            threes += 1
    return twos * threes


def difference(a, b):
    return sum(a != b for a, b in zip(a, b))


def common(a, b):
    return "".join([a for a, b in zip(a, b) if a == b])


def part2():
    for a, b in combinations(load(), 2):
        if difference(a, b) == 1:
            return common(a, b)


if __name__ == "__main__":
    print("Part one", part1())
    print("Part two", part2())
