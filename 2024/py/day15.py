#!/usr/bin/env python


from enum import IntEnum, StrEnum
from pathlib import Path

from aoc import Grid, Position


class Object(StrEnum):
    WALL = "#"
    BOX = "O"
    ROBOT = "@"
    SPACE = "."
    BOX_LEFT = "["
    BOX_RIGHT = "]"


class Movement(IntEnum):
    UP = ord("^")
    DOWN = ord("v")
    LEFT = ord("<")
    RIGHT = ord(">")


def read_map1(path: str) -> Grid[Object]:
    return Grid.from_file(str(Path(path)), lambda c: Object(c))


def read_map2(path: str) -> Grid[Object]:
    grid_data = Path(path).read_text().strip()
    for o, n in {"#": "##", "O": "[]", ".": "..", "@": "@."}.items():
        grid_data = grid_data.replace(o, n)
    return Grid.from_str(grid_data, lambda c: Object(c))


def read_movements(path: str) -> list[Movement]:
    return [Movement(ord(c)) for c in Path(path).read_text() if ord(c) in Movement]


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


def part1(map: Grid[Object], movements: list[Movement]) -> int:
    if rp := map.find(Object.ROBOT):
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

    total = 0
    for y in range(map.height):
        for x in range(map.width):
            if map.get(Position(x, y)) == Object.BOX:
                total += y * 100 + x
    return total


def find_boxes(map: Grid[Object], p: Position, dy: int) -> set[Position]:
    points: set[Position] = set()

    def dfs(p: Position):
        if p in points or map.get(p) in (Object.SPACE, Object.WALL):
            return
        points.add(p)
        match map.get(p):
            case Object.BOX_LEFT:
                dfs(Position(p.x + 1, p.y))
                dfs(Position(p.x + 1, p.y - dy))
            case Object.BOX_RIGHT:
                dfs(Position(p.x - 1, p.y))
                dfs(Position(p.x - 1, p.y - dy))

    dfs(p)

    return points


def test_boxes(map: Grid[Object], boxes: set[Position], dy: int):
    for p in sorted(boxes, key=lambda p: p.y, reverse=(dy == 1)):
        np = Position(p.x, p.y + dy)
        if np not in boxes and map.get(np) != Object.SPACE:
            return False
    return True


def push_boxes(map: Grid[Object], boxes: set[Position], dy: int):
    for p in sorted(boxes, key=lambda p: p.y, reverse=(dy == 1)):
        map.swap(p, Position(p.x, p.y + dy))


def part2(map: Grid[Object], movements: list[Movement]) -> int:
    if rp := map.find(Object.ROBOT):
        for move in movements:
            match move:
                case Movement.UP:
                    p = Position(rp.x, rp.y - 1)
                    match map.get(p):
                        case Object.SPACE:
                            map.swap(rp, p)
                            rp = p
                        case Object.BOX_LEFT | Object.BOX_RIGHT:
                            boxes = find_boxes(map, p, 1)
                            if test_boxes(map, boxes, -1):
                                push_boxes(map, boxes, -1)
                                map.swap(rp, p)
                                rp = p

                case Movement.DOWN:
                    p = Position(rp.x, rp.y + 1)
                    match map.get(p):
                        case Object.SPACE:
                            map.swap(rp, p)
                            rp = p
                        case Object.BOX_LEFT | Object.BOX_RIGHT:
                            boxes = find_boxes(map, p, -1)
                            if test_boxes(map, boxes, 1):
                                push_boxes(map, boxes, 1)
                                map.swap(rp, p)
                                rp = p

                case Movement.LEFT:
                    if fp := has_left_space(map, rp):
                        rp = push_left(map, rp, fp)
                case Movement.RIGHT:
                    if fp := has_right_space(map, rp):
                        rp = push_right(map, rp, fp)

    total = 0
    for y in range(map.height):
        for x in range(map.width):
            if map.get(Position(x, y)) == Object.BOX_LEFT:
                total += y * 100 + x
    return total


if __name__ == "__main__":
    print("Part1", part1(read_map1("day15_map_test.txt"), read_movements("day15_movements.txt")))
    print("Part2", part2(read_map2("day15_map.txt"), read_movements("day15_movements.txt")))
