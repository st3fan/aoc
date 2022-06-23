#!/usr/bin/env python3


from dataclasses import dataclass
from more_itertools import chunked, collapse, split_at


@dataclass
class Board:
    size: int
    data: [int]
    marked: [bool]

    @classmethod
    def from_lines(cls, lines):
        size = len(lines)
        data = [int(e) for e in collapse([e.split() for e in lines])]
        return cls(len(lines), data, [False] * (size*size))

    def mark(self, n):
        try:
            self.marked[self.data.index(n)] = True
        except:
            pass

    def iswinner(self):
        rows = list(chunked(self.marked, self.size))
        for r in rows:
            if sum(r) == self.size:
                return True
        for c in range(self.size):
            if sum(r[c] for r in rows) == self.size:
                return True

    def score(self, n):
        total = sum(v for i,v in enumerate(self.data) if not self.marked[i])
        return total*n


def load():
    lines = [line.strip() for line in open("day4.input").readlines()]
    [[numbers], *chunks] = split_at(lines, lambda s: s == "")
    return [int(e) for e in numbers.split(",")], [Board.from_lines(c) for c in chunks]


def part1():
    numbers, boards = load()
    for n in numbers:
        for b in boards:
            b.mark(n)
            if b.iswinner():
                return b.score(n)


def part2():
    numbers, boards = load()
    winners = []
    scores = []
    for n in numbers:
        for b in boards:
            if b not in winners:
                b.mark(n)
                if b.iswinner():
                    winners.append(b)
                    scores.append(b.score(n))
    return scores[-1]


if __name__ == "__main__":
    print("Part one:", part1())
    print("Part two:", part2())
