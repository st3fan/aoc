#!/usr/bin/env python3


import fileinput


def fuel_required(mass):
    return mass // 3 - 2


if __name__ == "__main__":
    sum = 0
    for line in fileinput.input():
        sum +=  fuel_required(int(line))
    print(sum)

