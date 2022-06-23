#!/usr/bin/env python3


def load():
    return [int(e) for e in open("day7.input").readline().split(",")]


def fuel_spent1(start_positions, end_position):
    return sum(abs(p - end_position) for p in start_positions)


def part1():
    start_positions = load()
    return min(fuel_spent1(start_positions, pos) for pos in range(5000))


# See https://en.wikipedia.org/wiki/Summation
def triangle_number(n):
    return ((n * n) + n) // 2


def fuel_spent2(start_positions, end_position):
    total = 0
    for p in start_positions:
        total += triangle_number(abs(p - end_position))
    return total


def part2():
    start_positions = load()
    return min(fuel_spent2(start_positions, pos) for pos in range(5000))


if __name__ == "__main__":
    print("Part one:", part1())
    print("Part two:", part2())

