#!/usr/bin/env python


def read_input() -> str:
    return open("day6.txt").read()


def find_start_marker(stream: str, marker_length: int) -> int:
    stream = read_input()
    for position in range(marker_length, len(stream)):
        packet = stream[position - marker_length : position]
        if len(set(packet)) == marker_length:
            return position
    raise Exception("No marker found")


def part1() -> int:
    return find_start_marker(read_input(), 4)


def part2() -> int:
    return find_start_marker(read_input(), 14)


if __name__ == "__main__":
    print("Part1:", part1())
    print("Part2:", part2())
