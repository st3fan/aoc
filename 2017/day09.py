#!/usr/bin/env python3


def read_input():
    with open("day09.input") as f:
        return [line.strip() for line in f.readlines()]


def score_group(group):
    stack = []
    score = 0
    skip = False
    garbage = False
    skipped = 0
    for c in group:
        if skip:
            skip = False
            continue
        match c:
            case "{":
                if not garbage:
                    stack.append(c)
                else:
                    skipped += 1
            case "}":
                if not garbage:
                    if stack.pop() != "{":
                        return 0,skipped
                    score += len(stack)+1
                else:
                    skipped += 1
            case "!":
                skip = True
            case "<":
                if not garbage:
                    stack.append(c)
                    garbage = True
                else:
                    skipped += 1
            case ">":
                if stack.pop() != "<":
                    return 0,skipped
                garbage = False
            case _:
                if garbage:
                    skipped += 1
    if len(stack) == 0:
        return score,skipped
    return 0,skipped


if __name__ == "__main__":

    groups = read_input()

    #assert score_group("{}") == 1
    #assert score_group("{{{}}}") == 6
    #assert score_group("{{},{}}") == 5
    #assert score_group("{{{},{},{{}}}}") == 16
    #assert score_group("{<a>,<a>,<a>,<a>}") == 1
    #assert score_group("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9
    #assert score_group("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9
    #assert score_group("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3

    # Part 1

    print("Part one:", sum([score_group(group)[0] for group in groups]))
    print("Part two:", sum([score_group(group)[1] for group in groups]))

