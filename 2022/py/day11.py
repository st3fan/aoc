#!/usr/bin/env python


from dataclasses import dataclass
from typing import Callable, List, Self


@dataclass
class Item:
    worry_level: int


DIVISORS_MUL = 11 * 7 * 13 * 5 * 3 * 17 * 2 * 19
# DIVISORS_MUL = 23 * 19 * 13 * 17


@dataclass
class Monkey:
    items: List[Item]
    operation: Callable[[int], int]
    divisor: int
    true_monkey: int
    false_monkey: int
    inspections: int = 0

    def __lt__(self, other: Self) -> bool:
        return self.inspections < other.inspections

    def inspect_item1(self, item: Item) -> int:
        self.inspections += 1
        item.worry_level = self.operation(item.worry_level)
        item.worry_level //= 3
        if (item.worry_level % self.divisor) == 0:
            return self.true_monkey
        else:
            return self.false_monkey

    def inspect_item2(self, item: Item) -> int:
        self.inspections += 1
        item.worry_level = self.operation(item.worry_level)
        item.worry_level %= DIVISORS_MUL
        # item.worry_level //= 3
        if (item.worry_level % self.divisor) == 0:
            return self.true_monkey
        else:
            return self.false_monkey


def part1() -> int:
    monkeys = [
        # Monkey([Item(w) for w in [79, 98]], lambda old: old * 19, 23, 2, 3),
        # Monkey([Item(w) for w in [54, 65, 75, 74]], lambda old: old + 6, 19, 2, 0),
        # Monkey([Item(w) for w in [79, 60, 97]], lambda old: old * old, 13, 1, 3),
        # Monkey([Item(w) for w in [74]], lambda old: old + 3, 17, 0, 1),
        Monkey([Item(w) for w in [57]], lambda old: old * 13, 11, 3, 2),
        Monkey([Item(w) for w in [58, 93, 88, 81, 72, 73, 65]], lambda old: old + 2, 7, 6, 7),
        Monkey([Item(w) for w in [65, 95]], lambda old: old + 6, 13, 3, 5),
        Monkey([Item(w) for w in [58, 80, 81, 83]], lambda old: old * old, 5, 4, 5),
        Monkey([Item(w) for w in [58, 89, 90, 96, 55]], lambda old: old + 3, 3, 1, 7),
        Monkey([Item(w) for w in [66, 73, 87, 58, 62, 67]], lambda old: old * 7, 17, 4, 1),
        Monkey([Item(w) for w in [85, 55, 89]], lambda old: old + 4, 2, 2, 0),
        Monkey([Item(w) for w in [73, 80, 54, 94, 90, 52, 69, 58]], lambda old: old + 7, 19, 6, 0),
    ]
    for _ in range(20):
        for monkey in monkeys:
            for item in monkey.items.copy():
                next_monkey = monkey.inspect_item1(item)
                monkey.items.remove(item)
                monkeys[next_monkey].items.append(item)
    monkeys.sort(reverse=True)
    return monkeys[0].inspections * monkeys[1].inspections


def part2() -> int:
    monkeys = [
        # Monkey([Item(w) for w in [79, 98]], lambda old: old * 19, 23, 2, 3),
        # Monkey([Item(w) for w in [54, 65, 75, 74]], lambda old: old + 6, 19, 2, 0),
        # Monkey([Item(w) for w in [79, 60, 97]], lambda old: old * old, 13, 1, 3),
        # Monkey([Item(w) for w in [74]], lambda old: old + 3, 17, 0, 1),
        Monkey([Item(w) for w in [57]], lambda old: old * 13, 11, 3, 2),
        Monkey([Item(w) for w in [58, 93, 88, 81, 72, 73, 65]], lambda old: old + 2, 7, 6, 7),
        Monkey([Item(w) for w in [65, 95]], lambda old: old + 6, 13, 3, 5),
        Monkey([Item(w) for w in [58, 80, 81, 83]], lambda old: old * old, 5, 4, 5),
        Monkey([Item(w) for w in [58, 89, 90, 96, 55]], lambda old: old + 3, 3, 1, 7),
        Monkey([Item(w) for w in [66, 73, 87, 58, 62, 67]], lambda old: old * 7, 17, 4, 1),
        Monkey([Item(w) for w in [85, 55, 89]], lambda old: old + 4, 2, 2, 0),
        Monkey([Item(w) for w in [73, 80, 54, 94, 90, 52, 69, 58]], lambda old: old + 7, 19, 6, 0),
    ]
    for _ in range(10000):
        for monkey in monkeys:
            for item in monkey.items.copy():
                next_monkey = monkey.inspect_item2(item)
                monkey.items.remove(item)
                monkeys[next_monkey].items.append(item)
    monkeys.sort(reverse=True)
    return monkeys[0].inspections * monkeys[1].inspections


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
