#!/usr/bin/env python3


import fileinput


def fuel_required(mass):
    total = 0
    required = mass // 3 - 2
    total += required
    while required > 6:
        required = required // 3 - 2
        total += required
    return total


if __name__ == "__main__":
    sum = 0
    for line in fileinput.input():
        sum += fuel_required(int(line))
    print(sum)

