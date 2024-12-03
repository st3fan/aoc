#!/usr/bin/env python3


from itertools import pairwise


def read_input(path):
    with open(path) as fp:
        for line in fp.readlines():
            yield [int(v) for v in line.split()]


def check(report) -> bool:
    if report[0] == report[1]:
        return False

    if report[0] > report[1]:
        for a, b in pairwise(report):
            if a <= b:
                return False
            d = abs(a - b)
            if d < 1 or d > 3:
                return False

    if report[0] < report[1]:
        for a, b in pairwise(report):
            if a >= b:
                return False
            d = abs(a - b)
            if d < 1 or d > 3:
                return False

    return True


def dampened_check(report):
    if check(report):
        return True
    for i in range(0, len(report)):
        c = report.copy()
        del c[i]
        if check(c):
            return True
    return False


if __name__ == "__main__":
    print("Part1:", sum(check(report) for report in read_input("day2.txt")))
    print("Part2:", sum(dampened_check(report) for report in read_input("day2.txt")))
