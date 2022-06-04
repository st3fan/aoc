#!/usr/bin/env python3


def main():
    input = list(open("day01.input").read().strip())

    floor = 0
    for c in input:
        match c:
            case "(":
                floor += 1
            case ")":
                floor -= 1
    print("Part one:", floor)

    floor = 1
    for i, c in enumerate(input):
        match c:
            case "(":
                floor += 1
            case ")":
                floor -= 1
        if floor == -1:
            break
    print("Part two:", i)


if __name__ == "__main__":
    main()

