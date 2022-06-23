#!/usr/bin/env python3


def load():
    return [line.strip() for line in open("day10.input").readlines()]


class CorruptChunk (Exception):
    def __init__(self, c):
        super().__init__(f"Invalid character found in chunk: {c}")
        self.c = c
    def score(self):
        scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
        return scores[self.c]


class IncompleteChunk (Exception):
    def __init__(self):
        super().__init__("Incomplete chunk")


def validate_chunk(chunk):
    s = []
    for c in chunk:
        match c:
            case "(":
                s.append(c)
            case "[":
                s.append(c)
            case "{":
                s.append(c)
            case "<":
                s.append(c)
            case ")":
                if s.pop() != "(":
                    raise CorruptChunk(c)
            case "]":
                if s.pop() != "[":
                    raise CorruptChunk(c)
            case "}":
                if s.pop() != "{":
                    raise CorruptChunk(c)
            case ">":
                if s.pop() != "<":
                    raise CorruptChunk(c)
    if len(s) != 0:
        raise IncompleteChunk()


def fix_corrupt_chunk(chunk):
    s = []
    fix = []
    for c in reversed(chunk):
        match c:
            case ")":
                s.append(c)
            case "]":
                s.append(c)
            case "}":
                s.append(c)
            case ">":
                s.append(c)
            case "(":
                if len(s) == 0 or s.pop() != ")":
                    fix.append(")")
            case "[":
                if len(s) == 0 or s.pop() != "]":
                    fix.append("]")
            case "{":
                if len(s) == 0 or s.pop() != "}":
                    fix.append("}")
            case "<":
                if len(s) == 0 or s.pop() != ">":
                    fix.append(">")

    points = {")": 1, "]": 2, "}": 3, ">": 4}

    score = 0
    for c in fix:
        score *= 5
        score += points[c]
    return score
        


def part1():
    corrupt = 0
    for line in load():
        try:
            validate_chunk(line)
        except CorruptChunk as e:
            corrupt += e.score()
        except IncompleteChunk:
            pass
    return corrupt


def part2():
    scores = []
    for chunk in load():
        try:
            validate_chunk(chunk)
        except CorruptChunk:
            pass
        except IncompleteChunk:
            scores.append(fix_corrupt_chunk(chunk))
    scores = sorted(scores)
    return scores[len(scores) // 2]


if __name__ == "__main__":
    print("Part one:", part1())
    print("Part two:", part2())

