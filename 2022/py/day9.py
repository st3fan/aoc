#!/usr/bin/env python3.11


from dataclasses import dataclass
from enum import Enum
from typing import Generator, Self, Set, Tuple


class Direction(Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"

    @classmethod
    def from_str(cls, s: str) -> Self:
        match s:
            case "U":
                return cls.UP
            case "D":
                return cls.DOWN
            case "L":
                return cls.LEFT
            case "R":
                return cls.RIGHT
            case _:
                raise ValueError("invalid direction")


@dataclass
class Instruction:
    direction: Direction
    distance: int

    @classmethod
    def from_str(cls, s: str) -> Self:
        c = s.split()
        return cls(Direction.from_str(c[0]), int(c[1]))


@dataclass
class Position:
    x: int
    y: int

    @classmethod
    def zero(cls) -> Self:
        return cls(0, 0)


def read_input() -> Generator[Instruction, None, None]:
    for line in open("day9.txt").readlines():
        yield Instruction.from_str(line.strip())


def adjecent(a: Position, b: Position) -> bool:
    return abs(a.x - b.x) in (0, 1) and abs(a.y - b.y) in (0, 1)


def part1() -> int:
    head = Position.zero()
    tail = Position.zero()

    tail_positions: Set[Tuple[int, int]] = set([(tail.x, tail.y)])

    for instruction in read_input():
        for _ in range(instruction.distance):

            # Move the head
            match instruction.direction:
                case Direction.UP:
                    head.y += 1
                case Direction.DOWN:
                    head.y -= 1
                case Direction.LEFT:
                    head.x -= 1
                case Direction.RIGHT:
                    head.x += 1

            # Move the tail if it is not adjecent with the head
            if not adjecent(head, tail):

                if head.x == tail.x or head.y == tail.y:
                    if head.x == tail.x:
                        if head.y == tail.y + 2:
                            tail.y += 1
                        elif head.y == tail.y - 2:
                            tail.y -= 1
                    elif head.y == tail.y:
                        if head.x == tail.x + 2:
                            tail.x += 1
                        elif head.x == tail.x - 2:
                            tail.x -= 1

                else:

                    if head.y > tail.y:
                        if head.x > tail.x:
                            tail.x += 1
                            tail.y += 1
                        else:
                            tail.x -= 1
                            tail.y += 1
                    elif head.y < tail.y:
                        if head.x > tail.x:
                            tail.x += 1
                            tail.y -= 1
                        else:
                            tail.x -= 1
                            tail.y -= 1
                    else:
                        raise Exception("Huh")

            # Remember the tail position
            tail_positions.add((tail.x, tail.y))

    return len(tail_positions)


def part2() -> int:
    knots = [Position.zero() for _ in range(10)]

    tail_positions: Set[Tuple[int, int]] = set([(0, 0)])

    for instruction in read_input():
        for _ in range(instruction.distance):

            # Move the head
            match instruction.direction:
                case Direction.UP:
                    knots[0].y += 1
                case Direction.DOWN:
                    knots[0].y -= 1
                case Direction.LEFT:
                    knots[0].x -= 1
                case Direction.RIGHT:
                    knots[0].x += 1

            for i in range(9):
                head = knots[i]
                tail = knots[i + 1]

                # Move the tails if it is not adjecent with the head
                if not adjecent(head, tail):

                    if head.x == tail.x or head.y == tail.y:
                        if head.x == tail.x:
                            if head.y == tail.y + 2:
                                tail.y += 1
                            elif head.y == tail.y - 2:
                                tail.y -= 1
                        elif head.y == tail.y:
                            if head.x == tail.x + 2:
                                tail.x += 1
                            elif head.x == tail.x - 2:
                                tail.x -= 1

                    else:

                        if head.y > tail.y:
                            if head.x > tail.x:
                                tail.x += 1
                                tail.y += 1
                            else:
                                tail.x -= 1
                                tail.y += 1
                        elif head.y < tail.y:
                            if head.x > tail.x:
                                tail.x += 1
                                tail.y -= 1
                            else:
                                tail.x -= 1
                                tail.y -= 1
                        else:
                            raise Exception("Huh")

            # Remember the tail position
            tail_positions.add((knots[9].x, knots[9].y))

    return len(tail_positions)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
