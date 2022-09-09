#!/usr/bin/env python3


from dataclasses import dataclass
from enum import Enum
from typing import List, Iterator

from aoc import CardinalDirection, CartesianDirection, Position


@dataclass
class Instruction:
    direction: CartesianDirection
    blocks: int

    @classmethod
    def from_str(cls, s) -> "Instruction":
        return Instruction(CartesianDirection.from_str(s[0]), int(s[1:]))


def read_input() -> List[Instruction]:
    return [Instruction.from_str(i) for i in open("day1.input").read().split(", ")]


class Santa:
    def __init__(self):
        self._direction: CardinalDirection = CardinalDirection.N
        self._position: Position = Position(0, 0)
    def turn(self, direction: CartesianDirection):
        self._direction = self._direction.turn(direction)
    def move(self, blocks: int):
        match self._direction:
            case CardinalDirection.N:
                self._position = self._position.translate(0, blocks)
            case CardinalDirection.E:
                self._position = self._position.translate(blocks, 0)
            case CardinalDirection.S:
                self._position = self._position.translate(0, -blocks)
            case CardinalDirection.W:
                self._position = self._position.translate(-blocks, 0)
    def imove(self, blocks: int) -> Iterator[Position]:
        match self._direction:
            case CardinalDirection.N:
                for _ in range(0, blocks):
                    self._position = self._position.translate(0, 1)
                    yield self._position
            case CardinalDirection.E:
                for _ in range(0, blocks):
                    self._position = self._position.translate(1, 0)
                    yield self._position
            case CardinalDirection.S:
                for _ in range(0, blocks):
                    self._position = self._position.translate(0, -1)
                    yield self._position
            case CardinalDirection.W:
                for _ in range(0, blocks):
                    self._position = self._position.translate(-1, 0)
                    yield self._position

    @property
    def position(self) -> Position:
        return self._position


def part1():
    santa = Santa()
    for instruction in read_input():
        santa.turn(instruction.direction)
        santa.move(instruction.blocks)
    return santa.position.manhattan_distance


def part2():
    santa = Santa()
    visited = set()
    for instruction in read_input():
        santa.turn(instruction.direction)
        for position in santa.imove(instruction.blocks):
            if position in visited:
                return position.manhattan_distance
            visited.add(position)
    raise Exception('santa is supposed to visit a position multiple times')


if __name__ == "__main__":
    print("Part 1", part1())
    print("Part 2", part2())