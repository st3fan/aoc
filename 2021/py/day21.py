#!/usr/bin/env python3


from itertools import count, cycle


def deterministic_dice():
    n = 1
    while True:
        yield n
        n += 1
        if n == 101:
            n = 1


def part1():
    dice = deterministic_dice()

    points = [0, 0]
    positions = [4-1, 8-1]
    positions = [10-1, 4-1]

    for player, turn in zip(cycle([0, 1]), count(1)):
        rolls = (next(dice), next(dice), next(dice))

        positions[player] = (positions[player] + sum(rolls)) % 10
        points[player] += positions[player] + 1
        print("Adding to score:", positions[player]+1)

        if points[player] >= 1000:
            if player == 0:
                return turn*3 * points[1]
            else:
                return turn*3 * points[0]


def part2():
    pass


if __name__ == "__main__":
    print("Part one:", part1())
    print("Part two:", part2())
