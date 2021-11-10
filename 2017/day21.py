#!/usr/bin/env python3

#
# Not my best code. Since this theme is coming back every year I think
# the Pattern (Image?) class is a great candidate to move into the aoc
# module so that it can be used again.
#
# Part two takes a little while. I am not sure if back in 2017 it was
# expected to do something smarter to optimize. On a MacBook Air M1 it
# runs in about 11 seconds.
#


from dataclasses import dataclass


@dataclass
class Pattern:
    data: str
    size: int

    @classmethod
    def from_string(cls, s):
        data = [list(r) for r in s.split("/")]
        return cls(data, len(data))

    def __init__(self, data, size):
        self.data = data
        self.size = size

    def hflip(self):
        return Pattern([list(reversed(row)) for row in self.data], self.size)

    def vflip(self):
        return Pattern(list(reversed(self.data)), self.size)

    def rotate(self):
        # Yeah that is a good trick - found on Stack Overflow
        return Pattern([list(e) for e in list(zip(*self.data[::-1]))], self.size)

    def variants(self):
        yield self
        yield self.rotate()
        yield self.rotate().rotate()
        yield self.rotate().rotate().rotate()
        yield self.vflip()
        yield self.vflip().rotate()
        yield self.vflip().rotate().rotate()
        yield self.vflip().rotate().rotate().rotate()
        yield self.hflip()
        yield self.hflip().rotate()
        yield self.hflip().rotate().rotate()
        yield self.hflip().rotate().rotate().rotate()

    def cutout(self, px, py, size):
        result = []
        for y in range(size):
            row = []
            for x in range(size):
                row.append(self.data[py + y][px+x])
            result.append(row)
        return Pattern(result, size)

    def count(self, v):
        total = 0
        for row in self.data:
            for c in row:
                if c == v:
                    total += 1
        return total


@dataclass
class Rule:
    src: Pattern
    dst: Pattern

    def __init__(self, rule):
        src, dst = rule.split(" => ")
        self.src = Pattern.from_string(src)
        self.dst = Pattern.from_string(dst)


def parse_rules(path):
    return [Rule(line) for line in [line.strip() for line in open(path).readlines()]]


def divisor_for_pattern(pattern):
    for n in (2, 3):
        if pattern.size % n == 0:
            return n


def divide_pattern(pattern):
    divisor = divisor_for_pattern(pattern)
    result = []
    for y in range(pattern.size // divisor):
        row = []
        for x in range(pattern.size // divisor):
            row.append(pattern.cutout(x * divisor, y * divisor, divisor))
        result.append(row)
    return result


def merge_row_of_patterns(row):
    result = []
    for r in range(row[0].size):
        l = []
        for p in row:
            l += p.data[r]
        result.append(l)
    return result


def merge_patterns(patterns):
    result = []
    for row in patterns:
        result += merge_row_of_patterns(row)
    return Pattern(result, len(patterns) * patterns[0][0].size)


def find_matching_rule(pattern, rules):
    for variant in pattern.variants():
        for rule in rules:
            if rule.src.data == variant.data:
                return rule


def replace_pattern(pattern, rules):
    if rule := find_matching_rule(pattern, rules):
        return rule.dst
    raise Exception(f"Could not find find rule for {pattern}")


def iterate(pattern, rules, n):
    for i in range(n):
        patterns = divide_pattern(pattern)
        for y, row in enumerate(patterns):
            for x, pattern in enumerate(row):
                patterns[y][x] = replace_pattern(pattern, rules)
        pattern = merge_patterns(patterns)
    return pattern


def main():

    rules = parse_rules("day21.input")
    pattern = Pattern.from_string(".#./..#/###")

    print("Part one:", iterate(pattern, rules, 5).count("#"))
    print("Part two:", iterate(pattern, rules, 18).count("#"))


if __name__ == "__main__":
    main()

