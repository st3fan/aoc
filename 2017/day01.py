#!/usr/bin/env python3


def read_input():
    with open("day01.input") as f:
        return [int(c) for c in f.read().strip()]


def other_digit(input, index, offset):
    return input[(index+offset) % len(input)]


if __name__ == "__main__":

    digits = read_input()

    r = sum(v for i,v in enumerate(digits) if v == other_digit(digits, i, 1))
    print("Part one: ", r)

    r = sum(v for i,v in enumerate(digits) if v == other_digit(digits, i, len(digits)//2))
    print("Part two: ", r)
