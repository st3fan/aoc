#!/usr/bin/env python3


from itertools import permutations
from more_itertools import flatten


def load_output_values():
    return [line.split(" | ")[1].split() for line in open("day8.input").readlines()]


def part1():
    return sum(len(e) in (2,4,3,7) for e in flatten(load_output_values()))


def sortstr(s):
    return "".join(sorted(s))

def all_patterns(p):
    def _get(p, a):
        return sortstr([p[n] for n in a])
    return {
        _get(p, [0,1,2,4,5,6]): 0,
        _get(p, [2,5]): 1,
        _get(p, [0,2,3,4,6]): 2,
        _get(p, [0,2,3,5,6]): 3,
        _get(p, [1,2,3,5]): 4,
        _get(p, [0,1,3,5,6]): 5,
        _get(p, [0,1,3,4,5,6]): 6,
        _get(p, [0,2,5]): 7,
        _get(p, [0,1,2,3,4,5,6]): 8,
        _get(p, [0,1,2,3,5,6]): 9,
    }


def find_match(signal_patterns, output_values):
    signal_patterns = [sortstr(e) for e in signal_patterns.split()]
    output_values = [sortstr(e) for e in output_values.split()]
    for p in permutations("abcdefg", 7):
        patterns = all_patterns(p)
        if all(q in signal_patterns for q in patterns):
            return int("".join([str(patterns[ov]) for ov in output_values]))


def part2():
    total = 0
    with open("day8.input") as fp:
        for line in fp.readlines():
            [signal_patterns, output_values] = line.strip().split(" | ")
            total += find_match(signal_patterns, output_values)
    return total


if __name__ == "__main__":
    print(part1())
    print(part2())

