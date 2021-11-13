#!/usr/bin/env python3


from itertools import groupby


INPUT = "1113122113"


def turn(s):
    result = ""
    for n, c in list([(len(list(g)), e) for e, g in groupby(s)]):
        result += str(n) + c
    return result


def main():

    # Part 1
    
    s = INPUT
    for _ in range(40):
        s = turn(s)
    print("Part one:", len(s))

    # Part 2
    
    s = INPUT
    for _ in range(50):
        s = turn(s)
    print("Part two:", len(s))


if __name__ == "__main__":
    main()

