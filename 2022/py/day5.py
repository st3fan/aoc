#!/usr/bin/env python


from dataclasses import dataclass
from enum import IntEnum
from typing import List, NewType, Self, Tuple


class MoveStyle(IntEnum):
    CRATE_MOVER_9000 = 9000
    CRATE_MOVER_9001 = 9001


CrateID = NewType("CrateID", str)


@dataclass
class Move:
    num: int
    src: int
    dst: int

    @classmethod
    def from_str(cls, s: str) -> Self:
        c = s.split()
        return cls(int(c[1]), int(c[3]), int(c[5]))


@dataclass
class Stack:
    crates: list[CrateID]

    def top(self) -> CrateID:
        return self.crates[-1]

    def pop(self) -> CrateID:
        return self.crates.pop()

    def push(self, crate: CrateID) -> None:
        self.crates.append(crate)


@dataclass
class Supplies:
    stacks: List[Stack]

    def move(self, move: Move, move_style: MoveStyle) -> None:
        match move_style:
            case MoveStyle.CRATE_MOVER_9000:
                for _ in range(move.num):
                    crate = self.stacks[move.src - 1].pop()
                    self.stacks[move.dst - 1].push(crate)
            case MoveStyle.CRATE_MOVER_9001:
                stack = Stack([])
                for _ in range(move.num):
                    crate = self.stacks[move.src - 1].pop()
                    stack.push(crate)
                for _ in range(move.num):
                    crate = stack.pop()
                    self.stacks[move.dst - 1].push(crate)

    @classmethod
    def from_str(cls, s: str) -> Self:
        lines = s.split("\n")[:-1]
        lines.reverse()

        num_stacks = (len(lines[0]) + 1) // 4
        stacks: List[Stack] = [Stack([]) for _ in range(num_stacks)]

        for line in lines:
            for i in range(num_stacks):
                p = (i * 4) + 1
                if p < len(line) and line[p] != " ":
                    stacks[i].push(CrateID(line[p]))

        return cls(stacks)


def read_input() -> Tuple[Supplies, List[Move]]:
    supplies, moves = open("day5.txt").read().split("\n\n")
    return Supplies.from_str(supplies.strip()), [Move.from_str(move) for move in moves.strip().split("\n")]


def part1() -> str:
    supplies, moves = read_input()
    for move in moves:
        supplies.move(move, move_style=MoveStyle.CRATE_MOVER_9000)
    return "".join([stack.top() for stack in supplies.stacks])


def part2() -> str:
    supplies, moves = read_input()
    for move in moves:
        supplies.move(move, move_style=MoveStyle.CRATE_MOVER_9001)
    return "".join([stack.top() for stack in supplies.stacks])


if __name__ == "__main__":
    print("Part1:", part1())
    print("Part2:", part2())
