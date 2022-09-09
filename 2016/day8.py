#!/usr/bin/env python3


from dataclasses import dataclass
import re
from typing import List

from aoc import Grid, Position

@dataclass
class RectInstruction:
    width: int
    height: int


@dataclass
class RotateRowInstruction:
    row: int
    n: int


@dataclass
class RotateColumnInstruction:
    column: int
    n: int


def parse_line(line: str) -> tuple[str]|None:
    for pattern in (r"(rect) (\d+)x(\d+)", r"(rotate) (row) y=(\d+) by (\d+)", r"(rotate) (column) x=(\d+) by (\d+)"):
        if match := re.match(pattern, line):
            return match.groups()


def read_input() -> List[RectInstruction|RotateRowInstruction|RotateColumnInstruction]:
    instructions = []
    for line in [line.strip() for line in open("day8.input").readlines()]:
        match parse_line(line):
            case ["rect", width, height]:
                instructions.append(RectInstruction(int(width), int(height)))
            case ["rotate", "row", row, n]:
                instructions.append(RotateRowInstruction(int(row), int(n)))
            case ["rotate", "column", column, n]:
                instructions.append(RotateColumnInstruction(int(column), int(n)))
    return instructions


def part1() -> int:
    display = Grid(50, 60, 0)
    for instruction in read_input():
        match instruction:
            case RectInstruction(width, height):
                display.fill(Position(0, 0), width,height, 1)
            case RotateRowInstruction(row, n):
                display.rotate_row(row, n)
            case RotateColumnInstruction(column, n):
                display.rotate_column(column, n)
    return display.count(1)


def part2():
    display = Grid(50, 60, " ")
    for instruction in read_input():
        match instruction:
            case RectInstruction(width, height):
                display.fill(Position(0, 0), width,height, "*")
            case RotateRowInstruction(row, n):
                display.rotate_row(row, n)
            case RotateColumnInstruction(column, n):
                display.rotate_column(column, n)
    display.dump()


if __name__ == "__main__":
    print("Part one", part1())
    part2()
    #print("Part two", part2())
