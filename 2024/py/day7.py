#!/usr/bin/env python3

from itertools import product, zip_longest


def read_input(path):
    with open(path) as fp:
        for line in fp.readlines():
            tn, en = line.strip().split(": ")
            yield int(tn), [v for v in en.split(" ")]


def concat_numbers(input_list):
    output_list = []
    i = 0
    while i < len(input_list):
        if input_list[i] == "||":
            output_list[-1] += input_list[i + 1]
            i += 2
        else:
            output_list.append(input_list[i])
            i += 1
    return output_list


def left_to_right(tokens):
    e = tokens[0]
    it = iter(tokens[1:])
    for o, v in zip_longest(it, it, fillvalue=None):
        if o == "||":
            e = "(" + f"int(str({e}) + '{v}')" + ")"  # Mind exploding
        else:
            e = "(" + e + o + v + ")"
    return e


def solve2(value, numbers):
    for operators in product(["*", "+", "||"], repeat=len(numbers) - 1):
        tokens = [item for pair in zip_longest(numbers, operators) for item in pair if item is not None]
        tokens = left_to_right(tokens)
        if eval(tokens) == value:
            return value
    return 0


def solve1(value, numbers):
    for operators in product(["*", "+"], repeat=len(numbers) - 1):
        tokens = [item for pair in zip_longest(numbers, operators) for item in pair if item is not None]
        expression = left_to_right(tokens)
        if eval(expression) == value:
            return value
    return 0


if __name__ == "__main__":
    print("Part1:", sum(solve1(value, numbers) for value, numbers in read_input("day7.txt")))
    print("Part2:", sum(solve2(value, numbers) for value, numbers in read_input("day7.txt")))
