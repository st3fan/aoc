#!/usr/bin/env python3


import re


def is_nice1(s):
    if len(re.findall(r"[aeuio]", s)) < 3:
        return False
    if len(re.findall(r"([a-z])\1", s)) == 0:
        return False
    for e in ("ab", "cd", "pq", "xy"):
        if e in s:
            return False
    return True

def is_nice2(s):
    if len(re.findall(r"([a-z][a-z]).*\1", s)) == 0:
        return False
    if len(re.findall(r"([a-z])[a-z]\1", s)) == 0:
        return False
    return True


def main():
    strings = [line.strip() for line in open("day05.input").readlines()]

    print("Part one:", sum(is_nice1(s) for s in strings))
    print("Part two:", sum(is_nice2(s) for s in strings))



if __name__ == "__main__":
    main()

