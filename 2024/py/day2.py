#!/usr/bin/env python3


from itertools import pairwise


def read_input(path):
    return [[int(v) for v in line.split()] for line in open(path).readlines()]


def check(report) -> bool:
    for a, b in pairwise(report):
        if not (1 <= abs(a - b) <= 3):
            return False
    return not sorted(report, reverse=(report[0] > report[1])) != report


def dampened_check(report):
    for i in range(0, len(report)):
        c = report.copy()
        del c[i]
        if check(c):
            return True
    return False


if __name__ == "__main__":
    print("Part1:", sum(check(report) for report in read_input("day2.txt")))
    print("Part2:", sum(check(report) or dampened_check(report) for report in read_input("day2.txt")))
