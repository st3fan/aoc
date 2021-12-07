#!/usr/bin/env/python3


def load():
    #return [3,4,3,1,2]
    return [int(line.strip()) for line in open("day6.input").readline().split(",")]


def iterate(l):
    adding = 0
    for i, v in enumerate(l):
        if v == 0:
            l[i] = 6
            adding += 1
            continue
        else:
            l[i] -= 1
    l += [8]*adding


def part1():
    l = load()
    for _ in range(80):
        iterate(l)
    return len(l)


def part2():
    # These are the values that day6.c outputs
    totals = [6206821033, 5617089148, 5217223242, 4726100874, 4368232009]
    return sum(totals[n-1] for n in load())


if __name__ == "__main__":
    print("Part one:", part1())
    print("Part two:", part2())
