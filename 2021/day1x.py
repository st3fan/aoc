#!/usr/bin/env python3


# Optimized version after looking at the spoiler thread on reddit.


from more_itertools import windowed


def load():
    return [int(line.strip()) for line in open("day1.input").readlines()]


def count(n):
    return sum(l[-1] > l[0] for l in windowed(load(), n))


if __name__ == "__main__":
    print("Part one:", count(2))
    print("Part two:", count(4))

