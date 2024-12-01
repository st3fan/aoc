#!/usr/bin/env python3

if __name__ == "__main__":
    left, right = list(zip(*[(int(a), int(b)) for a, b in [line.split() for line in open("day1.txt")]]))
    print("Part 1:", sum(abs(a - b) for a, b in zip(sorted(left), sorted(right))))
    print("Part 2:", sum((a * right.count(a)) for a in left))
