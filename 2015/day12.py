#!/usr/bin/env python3


import json


def sum_int_values1(o):
    match o:
        case int(i):
            return i
        case dict(d):
            return sum(sum_int_values1(o) for o in d.values())
        case list(l):
            return sum(sum_int_values1(o) for o in l)
        case _:
            return 0
                

def sum_int_values2(o):
    match o:
        case int(i):
            return i
        case dict(d):
            if "red" in d.values():
                return 0
            return sum(sum_int_values2(o) for o in d.values())
        case list(l):
            return sum(sum_int_values2(o) for o in l)
        case _:
            return 0


def main():
    input = json.load(open("day12.input"))
    print("Part one:", sum_int_values1(input))
    print("Part two:", sum_int_values2(input))


if __name__ == "__main__":
    main()

