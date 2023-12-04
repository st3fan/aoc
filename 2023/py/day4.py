#!/usr/bin/env python


from dataclasses import dataclass
from pathlib import Path
from typing import Generator, List, Self


@dataclass(frozen=True)
class Card:
    index: int
    winners: List[int]
    numbers: List[int]

    @property
    def num_winning(self) -> int:
        return len(set(self.winners) & set(self.numbers))

    @property
    def points(self) -> int:
        matching = set(self.winners) & set(self.numbers)
        if n := len(matching):
            return 1 * (2 ** (n - 1))
        return 0

    @classmethod
    def from_str(cls, s: str) -> Self:
        a, b = s.split(":")
        _, id = a.split()
        winners, numbers = b.split("|")
        return cls(int(id)-1, [int(v) for v in numbers.split()], [int(v) for v in winners.split()])


@dataclass(frozen=True)
class Game:
    cards: List[Card]

    # Returns cards - this fit my mental model better than counting
    def winning_cards(self) -> Generator[Card, None, None]:
        def _winning_cards(cards: List[Card]) -> Generator[Card, None, None]:
            for card in cards:
                yield card
                if n := card.num_winning:
                    yield from _winning_cards(self.cards[card.index+1:card.index+1+n])
        yield from _winning_cards(self.cards)

    @classmethod
    def from_path(cls, path: Path) -> Self:
        with open(path) as f:
            return cls([Card.from_str(line.strip()) for line in f.readlines()])


def part1() -> int:
    game = Game.from_path(Path("day4.txt"))
    return sum(card.points for card in game.cards)


def part2() -> int:
    game = Game.from_path(Path("day4.txt"))
    return sum(1 for _ in game.winning_cards()) # Can't count an iterable with len


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 1:", part2())