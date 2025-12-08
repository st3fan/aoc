#!/usr/bin/env python3


from functools import lru_cache
from typing import NamedTuple


class Pos(NamedTuple):
    x: int
    y: int


def read_input(path: str) -> tuple[list[Pos], int, int]:
    """
    Read all the splitters as (x,y) tuples
    """

    lines = [line.strip() for line in open(path).readlines()]
    w = len(lines[0])
    h = len(lines)

    splitters = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "^":
                splitters.append(Pos(x, y))

    return splitters, w, h


def part1(splitters: list[Pos], w: int, h: int) -> int:
    """
    Count all splitter that have a parent
    """

    def _has_parent(s: Pos) -> bool:
        """
        Go up and look for a splitter left or right. If we hit a
        splitter in the middle first then it is game over.
        """
        for y in range(s.y - 1, 0, -1):
            if Pos(s.x - 1, y) in splitters or Pos(s.x + 1, y) in splitters:
                return True
            if Pos(s.x, y) in splitters:
                return False
        return False

    return 1 + sum(_has_parent(s) for s in splitters)


def part2(splitterz: list[Pos], w: int, h: int) -> int:
    """
    Use DFS to walk and count all possible paths from the root. The final score
    for a path is 2 because at the last node the beam can be splitted a final time.
    """

    splitters = set(splitterz)

    # Add a final layer of nodes
    for x in range(0, w):
        splitters.add(Pos(x, h))

    def _left_node(node: Pos) -> Pos | None:
        for y in range(node.y + 1, h + 1):
            p = Pos(node.x - 1, y)
            if p in splitters:
                return p

    def _right_node(node: Pos) -> Pos | None:
        for y in range(node.y + 1, h + 1):
            p = Pos(node.x + 1, y)
            if p in splitters:
                return p

    @lru_cache(maxsize=None)
    def count_paths(node):
        if node is None:
            return 0

        left = _left_node(node)
        right = _right_node(node)

        if left is None and right is None:
            return 1

        return count_paths(left) + count_paths(right)

    return count_paths(splitterz[0])


if __name__ == "__main__":
    splitters, w, h = read_input("day07_input.txt")
    print(w, h)
    print("Part 1:", part1(splitters, w, h))
    print("Part 2:", part2(splitters, w, h))
