#!/usr/bin/env python


from enum import IntEnum, StrEnum
from pathlib import Path

from aoc import Grid, Position


class Object(StrEnum):
    WALL = "#"
    OBJECT = "O"
    ROBOT = "@"
    SPACE = "."


class Movement(IntEnum):
    UP = ord("^")
    DOWN = ord("v")
    LEFT = ord("<")
    RIGHT = ord(">")


def read_map(path: str) -> Grid[Object]:
    return Grid.from_file(str(Path(path)), lambda c: Object(c))


# PyRight fails on PathLike[str] although that is correct usage?
def read_movements(path: str) -> list[Movement]:
    return [Movement(ord(c)) for c in Path(path).read_text() if ord(c) in Movement]


#


def score(map: Grid[Object]) -> int:
    total = 0
    for y in range(map.height):
        for x in range(map.width):
            if map.get(Position(x, y)) == Object.OBJECT:
                total += y * 100 + x
    return total


# This is all very naively written


def has_right_space(map: Grid[Object], rp: Position) -> Position | None:
    for x in range(rp.x + 1, map.width):
        p = Position(x, rp.y)
        if map.get(p) == Object.WALL:
            return None
        if map.get(p) == Object.SPACE:
            return p


def has_down_space(map: Grid[Object], rp: Position) -> Position | None:
    for y in range(rp.y + 1, map.height):
        p = Position(rp.x, y)
        if map.get(p) == Object.WALL:
            return None
        if map.get(p) == Object.SPACE:
            return p


def has_left_space(map: Grid[Object], rp: Position) -> Position | None:
    for x in range(rp.x - 1, -1, -1):
        p = Position(x, rp.y)
        if map.get(p) == Object.WALL:
            return None
        if map.get(p) == Object.SPACE:
            return p


def has_up_space(map: Grid[Object], rp: Position) -> Position | None:
    for y in range(rp.y - 1, -1, -1):
        p = Position(rp.x, y)
        if map.get(p) == Object.WALL:
            return None
        if map.get(p) == Object.SPACE:
            return p


def push_right(map: Grid[Object], rp: Position, fp: Position) -> Position:
    for x in range(fp.x, rp.x, -1):
        map.swap(Position(x, rp.y), Position(x - 1, rp.y))
    return Position(rp.x + 1, rp.y)


def push_down(map: Grid[Object], rp: Position, fp: Position) -> Position:
    for y in range(fp.y, rp.y, -1):
        map.swap(Position(rp.x, y), Position(rp.x, y - 1))
    return Position(rp.x, rp.y + 1)


def push_left(map: Grid[Object], rp: Position, fp: Position) -> Position:
    for x in range(fp.x, rp.x):
        map.swap(Position(x, rp.y), Position(x + 1, rp.y))
    return Position(rp.x - 1, rp.y)


def push_up(map: Grid[Object], rp: Position, fp: Position) -> Position:
    for y in range(fp.y, rp.y):
        map.swap(Position(rp.x, y), Position(rp.x, y + 1))
    return Position(rp.x, rp.y - 1)


#


def part1(map: Grid[Object], movements: list[Movement]) -> int:
    if (rp := map.find(Object.ROBOT)) is None:
        raise Exception("Cannot find the robot on the map")

    for move in movements:
        match move:
            case Movement.UP:
                if fp := has_up_space(map, rp):
                    rp = push_up(map, rp, fp)
            case Movement.DOWN:
                if fp := has_down_space(map, rp):
                    rp = push_down(map, rp, fp)
            case Movement.LEFT:
                if fp := has_left_space(map, rp):
                    rp = push_left(map, rp, fp)
            case Movement.RIGHT:
                if fp := has_right_space(map, rp):
                    rp = push_right(map, rp, fp)

    return score(map)


def part2(map: Grid[Object], movements: list[Movement]) -> int:
    return 0


#

if __name__ == "__main__":
    map = read_map("day15_map.txt")
    movements = read_movements("day15_movements.txt")

    print("Part1", part1(map, movements))
    print("Part2", part2(map, movements))
