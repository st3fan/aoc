#!/usr/bin/env python3

from aoc import sort_str
from collections import Counter


def read_input():
    with open("day04.input") as f:
        return f.readlines()




if __name__ == "__main__":

    # Part 1

    def check_password(password):
        c = Counter(password.split())
        return c.most_common()[0][1] == 1

    print("Part one:", sum(check_password(password) for password in read_input()))

    # Part 2

    def check_password(password):
        c = Counter([sort_str(w) for w in password.split()])
        return c.most_common()[0][1] == 1

    print("Part two:", sum(check_password(password) for password in read_input()))
