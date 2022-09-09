#!/usr/bin/env python3


from collections import Counter


def read_messages():
    return [line.strip() for line in open("day6.input").readlines()];


def part1():
    counters = [Counter() for _ in range(8)]
    for m in read_messages():
        for i, c in enumerate(m):
            counters[i][c] += 1
    return "".join([c.most_common(1)[0][0] for c in counters])


def part2():
    counters = [Counter() for _ in range(8)]
    for m in read_messages():
        for i, c in enumerate(m):
            counters[i][c] += 1
    return "".join([c.most_common(27)[-1][0] for c in counters])


if __name__ == "__main__":
    print("Part one:", part1())
    print("Part two:", part2())
