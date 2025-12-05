#!/usr/bin/env python3

from aoc import Grid

PAPER = "@"
FLOOR = "."


def day1(grid: Grid[str]) -> int:
    return sum(len(grid.adjecent_positions(p, value=PAPER)) < 4 for p in grid.positions(value="@"))


def day2(grid: Grid[str]) -> int:
    total_removed = 0
    while to_remove := [p for p in grid.positions(value="@") if len(grid.adjecent_positions(p, value=PAPER)) < 4]:
        total_removed += len(to_remove)
        for p in to_remove:
            grid.set(p, ".")
    return total_removed


if __name__ == "__main__":
    input = Grid[str].from_file("day04_input.txt")
    print("Day 1:", day1(input))
    print("Day 2:", day2(input))
