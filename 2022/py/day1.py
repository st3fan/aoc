#!/usr/bin/env python


from typing import Generator, List


def read_input() -> Generator[List[int], None, None]:
    for group in open("day1.txt").read().split("\n\n"):
        yield [int(line) for line in group.strip().split("\n")]


def part1() -> int:
    return max(sum(group) for group in read_input())


def part2() -> int:
    return sum(sorted((sum(group) for group in read_input()), reverse=True)[:3])


if __name__ == "__main__":
    print("Part1:", part1())
    print("Part2:", part2())
