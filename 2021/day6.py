#!/usr/bin/env/python3


from collections import Counter


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
    r = [0] * 9
    for v in load():
        r[v] += 1
    for _ in range(256):
        t = r[0]
        r[0] = r[1]
        r[1] = r[2]
        r[2] = r[3]
        r[3] = r[4]
        r[4] = r[5]
        r[5] = r[6]
        r[6] = t + r[7]
        r[7] = r[8]
        r[8] = t
    return sum(r)
    

if __name__ == "__main__":
    print("Part one:", part1())
    print("Part two:", part2())
