#!/usr/bin/env


def read_input(path) -> list[int]:
    def _transform(v: str) -> int:
        match v[0]:
            case "R":
                return int(v[1:])
            case "L":
                return -int(v[1:])
        raise ValueError(f"Unexpected input: {v}")

    return [_transform(line) for line in open(path)]


def day1(input: list[int]) -> int:
    p = 50
    n = 0
    for v in input:
        p = (p + v) % 100
        if p == 0:
            n += 1
    return n


def day2(input: list[int]) -> int:
    p = 50
    n = 0
    for v in input:
        if v > 0:
            n += (p + v) // 100
        else:
            n += (((100 - p) % 100) + abs(v)) // 100
        p = (p + v) % 100
    return n


if __name__ == "__main__":
    input = read_input("day01_input.txt")
    print("Part 1:", day1(input))
    print("Part 2:", day2(input))
