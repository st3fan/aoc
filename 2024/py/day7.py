#!/usr/bin/env python3

from itertools import product, zip_longest


def read_input(path):
    with open(path) as fp:
        for line in fp.readlines():
            tn, en = line.strip().split(": ")
            yield int(tn), [int(v) for v in en.split(" ")]


def evaluate(tokens, value):
    a: int = tokens[0]
    it = iter(tokens[1:])
    for o, v in zip_longest(it, it, fillvalue=None):
        if a > value:
            return False
        match o, v:
            case "+", v:
                a += v  # pyright: ignore
            case "*", v:
                a *= v  # pyright: ignore
            case "||", v:
                a = int(str(a) + str(v))
    return a


def solve(value, numbers, tokens):
    for operators in product(tokens, repeat=len(numbers) - 1):
        tokens = [item for pair in zip_longest(numbers, operators) for item in pair if item is not None]
        if evaluate(tokens, value) == value:
            return value
    return 0


if __name__ == "__main__":
    print("Part1:", sum(solve(value, numbers, ("+", "*", "||")) for value, numbers in read_input("day7.txt")))
    print("Part2:", sum(solve(value, numbers, ("+", "*", "||")) for value, numbers in read_input("day7.txt")))
