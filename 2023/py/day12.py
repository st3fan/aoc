#!/usr/bin/python


# This mostly comes from https://advent-of-code.xavd.id/writeups/2023/day/12/


import re
from itertools import chain, combinations
from multiprocessing import Pool
from typing import List, Iterable

#
#    ?###???????? 3,2,1
#    .###.##.#...
#    .###.##..#..
#    .###.##...#.
#    .###.##....#
#    .###..##.#..
#    .###..##..#.
#    .###..##...#
#    .###...##.#.
#    .###...##..#
#    .###....##.#
#


def is_valid(groups: List[str], counts: List[int]):
    if len(groups) != len(counts):
        return False
    for group, count in zip(groups, counts):
        if len(group) != count:
            return False
    return True


def powerset(l: List[int]):
    return chain.from_iterable(combinations(l, r) for r in range(len(l) + 1))


def every_solve_combination(record: str) -> Iterable[List[str]]:
    unknown_indexes = [i for i, c in enumerate(record) if c == "?"]
    for indexes_to_replace in powerset(unknown_indexes):
        chars = list(record)
        for i in indexes_to_replace:
            chars[i] = "#"
        yield re.findall(r"#+", "".join(chars).replace("?", "."))


def count_valid_combinations(line: str) -> int:
    record, raw_shape = line.split()
    shape = list(map(int, raw_shape.split(",")))

    total = 0
    for group in every_solve_combination(record):
        if is_valid(group, shape):
            total += 1
    return total


def read_input() -> List[str]:
    with open("day12.txt") as f:
        return [line.strip() for line in f.readlines()]


def part1() -> int:
    input = read_input()
    with Pool(processes=8) as pool:
        return sum(pool.map(count_valid_combinations, input))


if __name__ == "__main__":
    print("Part 1:", part1())
