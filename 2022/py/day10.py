#!/usr/bin/env python


from itertools import cycle
from more_itertools import take, chunked
from typing import Generator, List


def read_input() -> List[None | int]:
    def _parse_line(line: str) -> None | int:
        if line.startswith("addx "):
            return int(line[5:])

    return [_parse_line(line.strip()) for line in open("day10.txt").readlines()]


def beam_cycle_values(instructions: list[None | int]) -> Generator[int, None, None]:
    for instruction in cycle(instructions):
        match instruction:
            case None:
                yield 0
            case int(dx):
                yield 0
                yield dx


def part1() -> int:
    total: int = 0
    x: int = 1
    for cycle, dx in enumerate(take(220, beam_cycle_values(read_input())), start=1):
        if cycle in (20, 60, 100, 140, 180, 220):
            total += cycle * x
        x += dx
    return total


def part2() -> int:
    g = beam_cycle_values(read_input())
    rows = [[" "] * 40 for _ in range(6)]

    sx: int = 1
    for r in range(6):
        for (x, xd) in enumerate(take(40, g)):
            if x in (sx - 1, sx, sx + 1):
                rows[r][x] = "#"
            sx += xd

    for r in rows:
        line = ""
        for segment in chunked(r, 5):
            line += "".join(segment) + "   "
        print(line)

    return 0


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
