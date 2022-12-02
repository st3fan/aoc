#!/usr/bin/env python


from enum import Enum, IntEnum
from typing import Generator, Tuple


class Shape(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @staticmethod
    def from_string(c: str) -> "Shape":
        match c:
            case "A" | "X":
                return Shape.ROCK
            case "B" | "Y":
                return Shape.PAPER
            case "C" | "Z":
                return Shape.SCISSORS
        raise ValueError("invalid shape name")


class State(Enum):
    LOSE = "LOSE"
    DRAW = "DRAW"
    WIN = "WIN"

    @staticmethod
    def from_string(c: str) -> "State":
        match c:
            case "X":
                return State.LOSE
            case "Y":
                return State.DRAW
            case "Z":
                return State.WIN
        raise ValueError(f"invalid state {c}")


def read_input1() -> Generator[Tuple[Shape, Shape], None, None]:
    with open("day2.txt") as f:
        for line in f.readlines():
            yield (Shape.from_string(line[0]), Shape.from_string(line[2]))


def score1(opponent: Shape, player: Shape) -> int:
    if opponent == player:
        return player + 3
    if (player, opponent) in {(Shape.ROCK, Shape.SCISSORS), (Shape.SCISSORS, Shape.PAPER), (Shape.PAPER, Shape.ROCK)}:
        return player + 6
    return player


def read_input2() -> Generator[Tuple[Shape, State], None, None]:
    with open("day2.txt") as f:
        for line in f.readlines():
            yield (Shape.from_string(line[0]), State.from_string(line[2]))


def score2(opponent: Shape, state: State) -> int:
    LOSING_MOVES = {
        Shape.ROCK: Shape.SCISSORS,
        Shape.SCISSORS: Shape.PAPER,
        Shape.PAPER: Shape.ROCK,
    }

    WINNING_MOVES = {
        Shape.ROCK: Shape.PAPER,
        Shape.SCISSORS: Shape.ROCK,
        Shape.PAPER: Shape.SCISSORS,
    }

    match state:
        case State.WIN:
            return score1(opponent, WINNING_MOVES[opponent])
        case State.LOSE:
            return score1(opponent, LOSING_MOVES[opponent])
        case State.DRAW:
            return score1(opponent, opponent)


def part1() -> int:
    return sum(score1(opponent, player) for (opponent, player) in read_input1())


def part2() -> int:
    return sum(score2(opponent, state) for (opponent, state) in read_input2())


if __name__ == "__main__":
    print("Part1:", part1())
    print("Part2:", part2())
