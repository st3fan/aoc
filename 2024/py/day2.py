#!/usr/bin/env python3


from itertools import pairwise


def read_input(path):
    return [[int(v) for v in line.split()] for line in open(path).readlines()]


def check(report) -> bool:
    return not any(not (1 <= abs(a - b) <= 3) for a, b in pairwise(report)) and not sorted(report, reverse=(report[0] > report[1])) != report


def dampened_check(report):
    return any(check(report[:i] + report[i + 1 :]) for i in range(0, len(report)))


if __name__ == "__main__":
    print("Part1:", sum(check(report) for report in read_input("day2.txt")))
    print("Part2:", sum(check(report) or dampened_check(report) for report in read_input("day2.txt")))
