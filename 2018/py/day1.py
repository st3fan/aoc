#!/usr/bin/env python3


from itertools import cycle


def load():
    return [int(line.strip()) for line in open("day1.input").readlines()]


def part1():
    return sum(load())


def part2():
    frequency = 0
    seen = set()
    for change in cycle(load()):
        frequency += change
        if frequency in seen:
            return frequency
        seen.add(frequency)


if __name__ == "__main__":
    print("Part one:", part1())
    print("Part two:", part2())
