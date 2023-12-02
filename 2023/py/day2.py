#!/usr/bin/env python


from dataclasses import dataclass
from typing import Generator, List, Self
import re


@dataclass
class Hand:
    red: int = 0
    green: int = 0
    blue: int = 0

    @classmethod
    def from_string(cls, s: str) -> Self:
        red, green, blue = 0, 0, 0
        for rocks in s.strip().split(","):
            match rocks.strip().split():
                case [n, "red"]:
                    red = int(n)
                case [n, "green"]:
                    green = int(n)
                case [n, "blue"]:
                    blue = int(n)
        return cls(red, green, blue)


@dataclass
class Game:
    id: int
    hands: List[Hand]

    def max_red(self) -> int:
        return max(hand.red for hand in self.hands)

    def max_green(self) -> int:
        return max(hand.green for hand in self.hands)

    def max_blue(self) -> int:
        return max(hand.blue for hand in self.hands)

    def power(self) -> int:
        return self.max_red() * self.max_blue() * self.max_green()

    @classmethod
    def from_string(cls, s: str) -> Self:
        game, hands = s.split(":")
        _, id = game.split()
        return cls(int(id), [Hand.from_string(s) for s in hands.split(";")])


def read_input() -> List[Game]:
    with open("day2.txt") as f:
        return [Game.from_string(line.strip()) for line in f.readlines()]


def part1() -> int:
    def check_game(game: Game) -> bool:
        return game.max_red() <= 12 and game.max_green() <= 13 and game.max_blue() <= 14
    return sum(game.id for game in read_input() if check_game(game))


def part2() -> int:
    return sum(game.power() for game in read_input())


if __name__ == "__main__":
    print("Part1:", part1())
    print("Part2:", part2())
