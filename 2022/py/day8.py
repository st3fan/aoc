#!/usr/bin/env python3.11


from dataclasses import dataclass


@dataclass
class Tree:
    height: int
    visible: bool


def read_input() -> list[list[Tree]]:
    with open("day8.txt") as fp:
        return [[Tree(int(c), False) for c in line.strip()] for line in fp.readlines()]


def row(input: list[list[Tree]], row: int) -> list[Tree]:
    return input[row]


def col(input: list[list[Tree]], col: int) -> list[Tree]:
    return [row[col] for row in input]


def mark_visible(l: list[Tree]):
    max = -1
    for t in l:
        if t.height > max:
            max = t.height
            t.visible = True


def count_total_visible(input: list[list[Tree]]) -> int:
    total = 0
    for row in input:
        for tree in row:
            if tree.visible:
                total += 1
    return total


def count_visible(height: int, l: list[Tree]) -> int:
    visible = 0
    for t in l:
        visible += 1
        if t.height >= height:
            break
    return visible


def part1() -> int:
    input = read_input()

    height = len(input)
    width = len(input[0])

    for i in range(0, height):
        l = row(input, i)
        mark_visible(l)
        mark_visible(list(reversed(l)))

    for i in range(0, width):
        l = col(input, i)
        mark_visible(l)
        mark_visible(list(reversed(l)))

    return count_total_visible(input)


def scenic_score(input: list[list[Tree]], r: int, c: int) -> int:
    rl = row(input, r)
    cl = col(input, c)

    t = input[r][c]

    return (
        count_visible(t.height, list(reversed(rl[0:c])))
        * count_visible(t.height, rl[c + 1 :])
        * count_visible(t.height, list(reversed(cl[0:r])))
        * count_visible(t.height, cl[r + 1 :])
    )


def part2() -> int:
    input = read_input()

    height = len(input)
    width = len(input[0])

    max = 0
    for r in range(0, height):
        for c in range(0, width):
            score = scenic_score(input, r, c)
            if score > max:
                max = score
    return max


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 1:", part2())
