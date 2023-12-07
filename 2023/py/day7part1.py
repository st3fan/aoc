#!/usr/bin/env python


from collections import Counter
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Self


class Card(Enum):
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()
    ACE = auto()

    @classmethod
    def from_str(cls, s: str) -> "Card":
        m = {
            "2": Card.TWO,
            "3": Card.THREE,
            "4": Card.FOUR,
            "5": Card.FIVE,
            "6": Card.SIX,
            "7": Card.SEVEN,
            "8": Card.EIGHT,
            "9": Card.NINE,
            "T": Card.TEN,
            "J": Card.JACK,
            "Q": Card.QUEEN,
            "K": Card.KING,
            "A": Card.ACE,
        }
        return m[s]

    def __lt__(self, other: Self) -> bool:
        return self.value < other.value


class HandType(Enum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIR = auto()
    THREE_OF_A_KIND = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    FIVE_OF_A_KIND = auto()

    @classmethod
    def from_str(cls, cards: str) -> "HandType":
        match sorted(Counter(cards).values()):
            case [1, 1, 1, 1, 1]:
                return cls.HIGH_CARD
            case [1, 1, 1, 2]:
                return cls.ONE_PAIR
            case [1, 2, 2]:
                return cls.TWO_PAIR
            case [1, 1, 3]:
                return cls.THREE_OF_A_KIND
            case [2, 3]:
                return cls.FULL_HOUSE
            case [1, 4]:
                return cls.FOUR_OF_A_KIND
            case [5]:
                return cls.FIVE_OF_A_KIND
        raise Exception(f"Can't determine type of hand <{cards}>")


@dataclass(frozen=True)
class Hand:
    cards: List[Card]
    bid: int
    type: HandType

    @classmethod
    def from_str(cls, s: str) -> Self:
        cards, bid = s.split()
        return cls(
            [Card.from_str(c) for c in cards], int(bid), HandType.from_str(cards)
        )

    def __lt__(self, other: Self) -> bool:
        if self.type == other.type:
            return self.cards < other.cards
        return self.type.value < other.type.value


def read_input() -> List[Hand]:
    with open("day7.txt") as f:
        return [Hand.from_str(line.strip()) for line in f.readlines()]


def part1() -> int:
    return sum(i * hand.bid for i, hand in enumerate(sorted(read_input()), 1))


if __name__ == "__main__":
    print("Part 1:", part1())
