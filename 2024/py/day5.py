#!/usr/bin/env python3

from functools import cmp_to_key

RULES = []

with open("day5_rules.txt") as fp:
    for line in fp.readlines():
        a, b = line.strip().split("|")
        RULES.append((int(a), int(b)))


def elf_compare(a, b):
    if (a, b) in RULES:
        return -1
    else:
        return 1


def elf_sort(pages):
    return sorted(pages, key=cmp_to_key(elf_compare))


if __name__ == "__main__":
    pages = []
    with open("day5_pages.txt") as fp:
        for line in fp.readlines():
            p = line.strip().split(",")
            pages.append([int(v) for v in p])

    t = 0
    for p in pages:
        print(p, " => ", elf_sort(p))
        if p == elf_sort(p):
            t += p[len(p) // 2]
    print("Part1:", t)

    t = 0
    for p in pages:
        print(p, " => ", elf_sort(p))
        if p != (good := elf_sort(p)):
            t += good[len(good) // 2]
    print("Part2:", t)
