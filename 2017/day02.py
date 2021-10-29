#!/usr/bin/env python3


from itertools import permutations


def read_input():
    with open("day02.input") as f:
        return [[int(e) for e in line.split()] for line in f.readlines()]


def foo(values):
    for a,b in permutations(values, 2):
        if a % b == 0:
            return a // b


if __name__ == "__main__":

    sheet = read_input()

    checksum = sum(max(line) - min(line) for line in sheet)
    print("Part one:", checksum)

    checksum = sum(foo(line) for line in sheet)
    print("Part two:", checksum)
