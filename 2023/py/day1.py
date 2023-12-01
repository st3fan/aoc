#!/usr/bin/env python


import re
from typing import Generator, List


def read_input1() -> Generator[List[int], None, None]:
    for line in open("day1.txt").read().strip().split("\n"):
        yield [int(c) for c in line if c.isdigit()]


def part1() -> int:
    return sum([10*digits[0] + digits[-1] for digits in read_input1()])


def read_input2() -> List[str]:
    return open("day1.txt").read().strip().split("\n")


DIGITS = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
          "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def first_number(line: str) -> int:
    for n in range(len(line)+1):
        for digit, value in DIGITS.items():
            if line[:n].find(digit) != -1:
                return value
    return 0


def last_number(line: str) -> int:
    for n in range(len(line)-1, -1, -1):
        for digit, value in DIGITS.items():
            if line[n:].find(digit) != -1:
                return value
    return 0


def part2() -> int:
    return sum(10 * first_number(line) + last_number(line) for line in read_input2())


if __name__ == "__main__":
    print("Part1:", part1())
    print("Part2:", part2())
