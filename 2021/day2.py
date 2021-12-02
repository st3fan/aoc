#!/usr/bin/env python3


def load(path):
    with open(path) as fp:
        for line in fp.readlines():
            c = line.split()
            yield c[0], int(c[1])


def part1():
    h, d = 0, 0
    for i in load("day2.input"):
        match i:
            case ["forward", int(distance)]:
                h += distance
            case ["up", int(distance)]:
                d -= distance
            case ["down", int(distance)]:
                d += distance
    return h*d


def part2():
    h, d, aim = 0, 0, 0
    for i in load("day2.input"):
        match i:
            case ["forward", int(x)]:
                h += x
                d += aim*x
            case ["up", int(x)]:
                aim -= x
            case ["down", int(x)]:
                aim += x
    return h*d


if __name__ == "__main__":
    print("Part one:", part1())
    print("Part two:", part2())

