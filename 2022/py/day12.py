#!/usr/bin/env python

from typing import Generator, List
from aoc import Grid, Position


def read_input() -> Grid:
    return Grid.from_file("day12.txt")


def _can_move(grid: Grid, src_position: Position, dst_position: Position, path: List[Position]) -> bool:
    if dst_position in path:
        return False

    src: int = ord(grid.get(src_position))
    dst: int = ord(grid.get(dst_position))

    if src == ord("S"):
        src = ord("a")

    if dst == ord("E"):
        dst = ord("z")

    if dst <= src:
        return True

    if dst > src and ((dst - src) == 1):
        return True

    return False


def find_all_paths(grid: Grid, position: Position, path: List[Position] = []) -> Generator[List[Position], None, None]:
    path.append(position)
    if grid.get(position) == "E":
        # print("Got to the end!")
        yield path
    else:
        # print("Loop:")
        for neighbour_position in grid.neighbours(position):
            # print("Looking at", neighbour_position, path)
            if _can_move(grid, position, neighbour_position, path):
                # print("  Can go", neighbour_position)
                yield from find_all_paths(grid, neighbour_position, path)
            # else:
            # print("  Can't go")
    path.pop()


def part1() -> int:
    grid = Grid.from_file("day12.txt")

    # for path in find_all_paths(grid, grid.find("S")):  # type: ignore
    #     print(path)

    for _ in range(1000):
        min(len(path) for path in find_all_paths(grid, grid.find("S")))

    return min(len(path) for path in find_all_paths(grid, grid.find("S"))) - 1  # type: ignore


def part2() -> int:
    return 0


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
