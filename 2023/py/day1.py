#!/usr/bin/env python


import re
from typing import Generator, List


def read_input1() -> Generator[List[str], None, None]:
    for line in open("day1.txt").read().strip().split("\n"):
        yield [c for c in line if c.isdigit()]


def part1() -> int:
    return sum([int(digits[0] + digits[-1]) for digits in read_input1()])


def read_input2() -> List[str]:
    return open("day1.txt").read().strip().split("\n")


# I could not get a replacement function to work so I did the dumbest thing instead :-/

def first_number(line: str) -> int:
    numbers = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    for p in re.split(r"(one|two|three|four|five|six|seven|eight|nine|\d)", line):
        if p.isdigit():
            return int(p)
        if p in numbers:
            return numbers.index(p)+1
    return 0


def last_number(line: str) -> int:
    line = "".join(reversed(line))
    numbers = ("eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin")
    for p in re.split(r"(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)", line):
        if p.isdigit():
            return int(p)
        if p in numbers:
            return numbers.index(p)+1
    return 0


def part2() -> int:
    return sum(10 * first_number(line) + last_number(line) for line in read_input2())


if __name__ == "__main__":
    print("Part1:", part1())
    print("Part2:", part2())
