#!/usr/bin/env python


from itertools import cycle
from more_itertools import nth, take, chunked
from typing import Generator, List, Tuple


def read_input() -> List[None | int]:
    def _parse_line(line: str) -> None | int:
        if line.startswith("addx"):
            return int(line[5:])

    return [_parse_line(line.strip()) for line in open("day10.txt").readlines()]


def signal_generator(instructions: list[None | int]) -> Generator[Tuple[int, int, int], None, None]:
    c: int = 0
    x: int = 1
    for instruction in cycle(instructions):
        match instruction:
            case None:
                c += 1
                yield (c, x, c * x)
            case int(v):
                c += 1
                yield (c, x, c * x)
                c += 1
                yield (c, x, c * x)
                x += v


def beam_movement_generator(instructions: list[None | int]) -> Generator[int | None, None, None]:
    for instruction in cycle(instructions):
        match instruction:
            case None:
                yield None
            case int(dx):
                yield None
                yield dx


def part1() -> int:
    g = signal_generator(read_input())
    return sum(e[2] for e in take(220, g) if e[0] in (20, 60, 100, 140, 180, 220))


def part2() -> int:
    g = beam_movement_generator(read_input())
    rows = [[" "] * 40 for _ in range(6)]

    sx: int = 1
    for r in range(6):
        for (x, xd) in enumerate(take(40, g)):
            if x in (sx - 1, sx, sx + 1):
                rows[r][x] = "#"
            if xd != None:
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
