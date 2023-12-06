#!/usr/bin/env python


from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Race:
    time: int
    distance: int


def read_input1() -> List[Race]:
    with open("day6.txt") as f:
        ts = f.readline().strip()
        ds = f.readline().strip()
        return [Race(int(t), int(d)) for (t, d) in zip(ts.split()[1:], ds.split()[1:])]


def read_input2() -> Race:
    with open("day6.txt") as f:
        t = "".join(f.readline().strip().split(":")[1:]).replace(" ", "")
        d = "".join(f.readline().strip().split(":")[1:]).replace(" ", "")
        return Race(int(t), int(d))


def calculate_distance(total_time: int, hold_time: int) -> int:
    return (total_time - hold_time) * hold_time


def part1():
    r = 1
    for race in read_input1():
        n = 0
        for hold_time in range(race.time):
            if calculate_distance(race.time, hold_time) > race.distance:
                n += 1
        r *= n
    return r


def part2():
    race = read_input2()
    for hold_time in range(race.time):
        if calculate_distance(race.time, hold_time) > race.distance:
            return race.time - 2 * hold_time + 1


if __name__ == "__main__":
    print("Part 1", part1())
    print("Part 2", part2())
