#!/usr/bin/env python3


from typing import List
from aoc import CartesianDirection, Position


def read_input() -> List[CartesianDirection]:
    return [CartesianDirection.from_str(i) for i in open("day2.input").read().split()]



def part1() -> str:
    keypad = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]

    position = Position(1, 1)
    code = []

    for line in open("day2.input").readlines():
        for direction in line:
            match direction:
                case "R":
                    if position.x != 2:
                        position = position.translate(1, 0)
                case "L":
                    if position.x > 0:
                        position = position.translate(-1, 0)
                case "U":
                    if position.y != 0:
                        position = position.translate(0, -1)
                case "D":
                    if position.y != 2:
                        position = position.translate(0, 1)
        code.append(keypad[position.y][position.x])

    return "".join(code)


def part2():
    keypad = [
        ["0", "0", "1", "0", "0"],
        ["0", "2", "3", "4", "0"],
        ["5", "6", "7", "8", "9"],
        ["0", "A", "B", "C", "0"],
        ["0", "0", "D", "0", "0"]
    ]

    position = Position(2, 2)
    code = []

    for line in open("day2.input").readlines():
        for direction in line:
            match direction:
                case "R":
                    if position.x != 4 and keypad[position.y][position.x+1] != "0":
                        position = position.translate(1, 0)
                case "L":
                    if position.x > 0 and keypad[position.y][position.x-1] != "0":
                        position = position.translate(-1, 0)
                case "U":
                    if position.y != 0 and keypad[position.y-1][position.x] != "0":
                        position = position.translate(0, -1)
                case "D":
                    if position.y != 4 and keypad[position.y+1][position.x] != "0":
                        position = position.translate(0, 1)
        code.append(keypad[position.y][position.x])

    return "".join(code)


if __name__ == "__main__":
    print("Part one:", part1())
    print("Part two:", part2())
