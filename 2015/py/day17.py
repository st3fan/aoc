#!/usr/bin/env python3


from collections import defaultdict
from itertools import combinations


INPUT = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]


def main():

    # Part 1

    n = 0
    for length in range(len(INPUT)):
        for p in combinations(INPUT, length):
            if sum(p) == 150:
                n += 1
    print("Part one:", n)

    # Part 2

    n = 0
    counts = defaultdict(int)
    for length in range(len(INPUT)):
        for p in combinations(INPUT, length):
            if sum(p) == 150:
                counts[length] += 1
                n += 1
    print("Part two:", counts[min(counts.keys())])



if __name__ == "__main__":
    main()

