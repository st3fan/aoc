#!/usr/bin/env python3


INPUT = 33_100_000


def number_of_presents(house):
    n = 0
    for elf in range(1, house+1):
        if house % elf == 0:
            n += (10 * elf)
    return n


if __name__ == "__main__":

    # Part 1 - Brute force .. I narrowed it down to a reasonable range manually. Not
    # the best solution but I got to the correct answer.

    for house in range(776_000, 776_250):
        n = number_of_presents(house)
        if n >= INPUT:
            break
    print("Part one:", house, n)

    # Part 2


