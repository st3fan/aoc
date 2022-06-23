#!/usr/bin/env python3


def part1():
    measurements = [int(line.strip()) for line in open("day1.input").readlines()]
    n = 0
    for a, b in zip(measurements[:-1], measurements[1:]):
        if b > a:
            n += 1
    print("Part one:", n)


def part2():
    measurements = [int(line.strip()) for line in open("day1.input").readlines()]
    n = 0
    for i in range(len(measurements)-3):
        a = measurements[i:i+3]
        b = measurements[i+1:i+4]
        if sum(b) > sum(a):
            n += 1
    print("Part two:", n)


if __name__ == "__main__":
    part1()
    part2()

