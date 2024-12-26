#!/usr/bin/env python

from itertools import islice

from more_itertools import nth, sliding_window, take


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


def price_and_difference(initial: int):
    secret = initial

    previous = secret % 10

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

        yield secret % 10, (secret % 10) - previous

        previous = secret % 10


def part1(numbers: list[int]) -> int:
    return sum(nth(generator(n), 2000) for n in numbers)  # pyright: ignore


def part2(numbers: list[int]) -> int:
    buyers: list[dict[tuple[int, int, int, int], int]] = []

    all_sequences = set()

    for n in numbers:
        d = {}
        for w in sliding_window(islice(take(2000, price_and_difference(n)), 1, None), 4):
            s = (w[0][1], w[1][1], w[2][1], w[3][1])
            all_sequences.add(s)
            v = w[3][0]
            if s not in d:
                d[s] = v
        buyers.append(d)

    m = 0
    sequences_by_added_values = {}
    for s in all_sequences:
        t = 0
        for buyer in buyers:
            if s in buyer:
                t += buyer[s]
        sequences_by_added_values[s] = t
        if t > m:
            m = t

    return m


if __name__ == "__main__":
    numbers = read_input("day22.txt")
    print("Part1:", part1(numbers))
    print("Part2:", part2(numbers))
