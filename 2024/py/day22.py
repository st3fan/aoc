#!/usr/bin/env python

from more_itertools import nth


def read_input(path: str) -> list[int]:
    with open(path) as fp:
        return [int(line.strip()) for line in fp]


def generator(initial: int):
    secret = initial

    yield secret

    while True:
        t = secret * 64
        secret ^= t
        secret %= 16777216

        t = secret // 32
        secret ^= t
        secret %= 16777216

        t = secret * 2048
        secret ^= t
        secret %= 16777216

        yield secret


if __name__ == "__main__":
    numbers = read_input("day22.txt")
    print("Part1:", sum(nth(generator(n), 2000) for n in numbers))  # pyright: ignore
