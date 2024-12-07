#!/usr/bin/env python3


from itertools import product


def read_input(path):
    with open(path) as fp:
        for line in fp.readlines():
            tn, en = line.strip().split(": ")
            yield int(tn), [int(v) for v in en.split(" ")]


def solve(value, numbers, tokens):
    for operators in product(tokens, repeat=len(numbers) - 1):
        a = numbers[0]
        for o, v in zip(operators, numbers[1:]):
            match o, v:
                case "+", v:
                    a += v
                case "*", v:
                    a *= v
                case "||", v:
                    a = int(str(a) + str(v))
            if a > value:
                break
            if a == value:
                return a
    return 0


if __name__ == "__main__":
    print("Part1:", sum(solve(value, numbers, ("+", "*")) for value, numbers in read_input("day7.txt")))
    print("Part2:", sum(solve(value, numbers, ("+", "*", "||")) for value, numbers in read_input("day7.txt")))
