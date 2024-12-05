#!/usr/bin/env python3

from functools import cmp_to_key


def make_elf_compare(rules):
    def elf_compare(a, b):
        if [a, b] in rules:
            return -1
        return 1

    return elf_compare


def elf_sort(pages, rules):
    return sorted(pages, key=cmp_to_key(make_elf_compare(rules)))


def read_rules(path: str) -> list[list[int]]:
    with open(path) as fp:
        return [[int(v) for v in line.split("|")] for line in fp]


def read_pages(path: str) -> list[list[int]]:
    with open(path) as fp:
        return [[int(v) for v in line.split(",")] for line in fp]


if __name__ == "__main__":
    rules = read_rules("day5_rules.txt")
    pages = read_pages("day5_pages.txt")

    print("Part1:", sum(p[len(p) // 2] for p in pages if p == elf_sort(p, rules)))
    print("Part2:", sum(good[len(good) // 2] for p in pages if p != (good := elf_sort(p, rules))))
