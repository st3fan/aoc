#!/usr/bin/env python3


from itertools import combinations
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Item:
    name: str
    cost: int
    damage: int
    armor: int


WEAPONS = [
    Item("Dagger",        8,     4,       0),
    Item("Shortsword",   10,     5,       0),
    Item("Warhammer",    25,     6,       0),
    Item("Longsword",    40,     7,       0),
    Item("Greataxe",     74,     8,       0)
]

ARMOR = [
    Item("Leather",      13,     0,       1),
    Item("Chainmail",    31,     0,       2),
    Item("Splintmail",   53,     0,       3),
    Item("Bandedmail",   75,     0,       4),
    Item("Platemail",   102,     0,       5)
]

RINGS = [
    Item("Damage +1",    25,     1,       0),
    Item("Damage +2",    50,     2,       0),
    Item("Damage +3",   100,     3,       0),
    Item("Defense +1",   20,     0,       1),
    Item("Defense +2",   40,     0,       2),
    Item("Defense +3",   80,     0,       3)
]


@dataclass
class Player:
    items: [Item]
    hit_points: int

    total_cost: int = field(init=False)
    total_damage: int = field(init=False)
    total_armor: int = field(init=False)

    def __post_init__(self):
        self.total_cost = sum(item.cost for item in self.items)
        self.total_damage = sum(item.damage for item in self.items)
        self.total_armor = sum(item.armor for item in self.items)

    def take_damage(self, points: int):
        self.hit_points -= points

    def alive(self) -> bool:
        return self.hit_points > 0


def play(boss, player):
    """Play until either boss or player dies. Returns True if the player won."""
    while boss.alive() and player.alive():
        boss.take_damage(player.total_damage - boss.total_armor)
        if not boss.alive():
            break
        player.take_damage(boss.total_damage - player.total_armor)
        if not player.alive():
            break
    return player.alive()


def all_item_combos():
    """Return all possible item combinations"""
    for weapons in [[w] for w in WEAPONS]:
        for armors in [[]] + [[a] for a in ARMOR]:
            for rings in [[]] + [list(l) for l in combinations(RINGS, 1)] + [list(l) for l in combinations(RINGS, 2)]:
                yield weapons + armors + rings


def main():
    boss_items = [WEAPONS[4], ARMOR[0]]

    min_gold = 10_000
    for player_items in all_item_combos():
        boss = Player(boss_items, 104)
        player = Player(player_items, 100)
        if play(boss, player):
            min_gold = min(min_gold, player.total_cost)
    print("Part one:", min_gold)

    max_gold = 0
    for player_items in all_item_combos():
        boss = Player(boss_items, 104)
        player = Player(player_items, 100)
        if not play(boss, player):
            max_gold = max(max_gold, player.total_cost)
    print("Part two:", max_gold)


if __name__ == "__main__":
    main()

