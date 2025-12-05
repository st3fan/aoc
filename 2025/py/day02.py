#!/usr/bin/env python3

from pathlib import Path
from typing import Callable


def read_input(path: Path) -> list[tuple[int, int]]:
    def _parse_range(s: str) -> tuple[int, int]:
        c = s.split("-")
        return int(c[0]), int(c[1])

    contents = path.read_text()
    return [_parse_range(range) for range in contents.strip().split(",")]


type ProductIdValidator = Callable[[int], bool]


def valid_id1(id: int) -> bool:
    s = str(id)
    return s[len(s) // 2 :] != s[: len(s) // 2]


def valid_id2(id: int) -> bool:
    s = str(id)
    for n in range(1, len(s)):
        chunks = [s[i : i + n] for i in range(0, len(s), n)]
        if len(set(chunks)) == 1:
            return False
    return True


def day(input: list[tuple[int, int]], validator: ProductIdValidator) -> int:
    total = 0
    for r in input:
        for id in range(r[0], r[1] + 1):
            if not validator(id):
                total += id
    return total


if __name__ == "__main__":
    input = read_input(Path("day02_input.txt"))
    print("Day1:", day(input, valid_id1))
    print("Day2:", day(input, valid_id2))
