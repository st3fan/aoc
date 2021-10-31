#!/usr/bin/env python3


from dataclasses import dataclass


@dataclass
class Point:
    x: int = 0
    y: int = 0
    z: int = 0


def read_input():
    return open("day11.input").read().strip().split(",")


def hex_distance(a, b):
    return (abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z)) // 2


if __name__ == "__main__":

    steps = read_input();

    # Part 1

    p = Point(0,0,0)

    for step in steps:
        match step:
            case "n":
                p.y += 1
                p.z -= 1
            case "s":
                p.y -= 1
                p.z += 1
            case "nw":
                p.x -= 1
                p.y += 1
            case "ne":
                p.x += 1
                p.z -= 1
            case "sw":
                p.x -= 1
                p.z += 1
            case "se":
                p.x += 1
                p.y -= 1

    print("Part one:", hex_distance(Point(0,0,0), p))

    # Part 2

    max_distance = 0
    p = Point(0,0,0)

    for step in steps:
        match step:
            case "n":
                p.y += 1
                p.z -= 1
            case "s":
                p.y -= 1
                p.z += 1
            case "nw":
                p.x -= 1
                p.y += 1
            case "ne":
                p.x += 1
                p.z -= 1
            case "sw":
                p.x -= 1
                p.z += 1
            case "se":
                p.x += 1
                p.y -= 1
        max_distance = max(max_distance, hex_distance(Point(0,0,0), p))

    print("Part two:", max_distance)

