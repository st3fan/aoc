#!/usr/bin/env python3


import re


def read_input(path):
    return open(path).read()


def part1(input):
    return sum(int(m[0]) * int(m[1]) for m in re.findall(r"mul\((\d+),(\d+)\)", input))


def part2(input):
    t = 0
    e = True
    for m in re.findall(r"(mul|do|don't)\((?:(\d+),(\d+))?\)", input):
        match m:
            case ["do", "", ""]:
                e = True
            case ["don't", "", ""]:
                e = False
            case ["mul", a, b]:
                if e:
                    t += int(a) * int(b)
    return t


if __name__ == "__main__":
    print("Part 1:", part1(read_input("day3.txt")))
    print("Part 2:", part2(read_input("day3.txt")))
