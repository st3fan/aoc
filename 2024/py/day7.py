#!/usr/bin/env python3

from itertools import product, zip_longest


def read_input(path):
    with open(path) as fp:
        for line in fp.readlines():
            tn, en = line.strip().split(": ")
            yield int(tn), [v for v in en.split(" ")]


def left_to_right(tokens):
    """Wrap in parens so that the expression is evaluated left to right"""
    e = tokens[0]
    it = iter(tokens[1:])
    for o, v in zip_longest(it, it, fillvalue=None):
        if o == "||":
            e = "(" + f"int(str({e}) + '{v}')" + ")"
        else:
            e = "(" + e + o + v + ")"
    return e


def solve(value, numbers, tokens):
    for operators in product(tokens, repeat=len(numbers) - 1):
        tokens = [item for pair in zip_longest(numbers, operators) for item in pair if item is not None]
        expression = left_to_right(tokens)
        if eval(expression) == value:
            return value
    return 0


if __name__ == "__main__":
    print("Part1:", sum(solve(value, numbers, ("+", "*")) for value, numbers in read_input("day7.txt")))
    print("Part2:", sum(solve(value, numbers, ("+", "*", "||")) for value, numbers in read_input("day7.txt")))
