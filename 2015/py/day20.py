#!/usr/bin/env python3


INPUT = 33_100_000


def number_of_presents1(house):
    n = 0
    for elf in range(1, house+1):
        if house % elf == 0:
            n += (10 * elf)
    return n


def number_of_presents2(house):
    n = 0
    for elf in range(1, house+1):
        if house % elf == 0:
            if house // elf < 50:
                n += (11 * elf)
    return n


if __name__ == "__main__":

    # Both brute force .. I narrowed it down to a reasonable range manually.
    # Not the best solution but I got to the correct answer. Python is
    # incredibly slow at basic integer math. The C version is probably 100x
    # faster. See day20.c :-)

    # Part 1

    for house in range(750_000, 1_000_000):
        if (n := number_of_presents1(house)) > INPUT:
            break
    print("Part one:", house, n)

    # Part 2

    for house in range(750_000, 1_000_000):
        if (n := number_of_presents2(house)) > INPUT:
            break
    print("Part one:", house, n)
