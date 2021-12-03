#!/usr/bin/env python3


from collections import Counter


def load():
    return [line.strip() for line in open("day3.input").readlines()]


# Part 1

def _rate(l, reverse=True):
    counters = [Counter() for _ in range(len(l[0]))]
    for n in l:
        for i, c in enumerate(n):
            counters[i][c] += 1
    r = ""
    for c in counters:
        mc = sorted(c.most_common(), reverse=reverse, key=lambda e: e[1])
        if len(mc) == 2 and mc[0][1] == mc[1][1]:
            r += "1" if reverse else "0"
        else:
            r += mc[0][0]
    return r


def _epsilon_rate(l):
    return _rate(l, True)

def epsilon_rate(l):
    return int(_epsilon_rate(l), 2)


def _gamma_rate(l):
    return _rate(l, False)

def gamma_rate(l):
    return int(_gamma_rate(l), 2)

def part1(data):
    return gamma_rate(data) * epsilon_rate(data)


# Part 2

def _rating(l, fn):
    for bit in range(len(l[0])):
        if (l := [e for e in l if fn(l)[bit] == e[bit]]) and len(l) == 1:
            return l[0]


def oxygen_generator_rating(l):
    return int(_rating(l, _gamma_rate), 2)


def carbon_dioxide_scrubber_rating(l):
    return int(_rating(l, _epsilon_rate), 2)


def part2(data):
    return oxygen_generator_rating(data) * carbon_dioxide_scrubber_rating(data)


if __name__ == "__main__":
    print("Part one:", part1(load()))
    print("Part two:", part2(load()))
