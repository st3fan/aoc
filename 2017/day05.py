#!/usr/bin/env python3


def read_input():
    with open("day05.input") as f:
        return [int(line) for line in f.readlines()]


if __name__ == "__main__":

    # Part 1

    instructions = read_input()

    pc = 0
    steps = 0

    while True:
        if pc >= len(instructions):
            break
        offset = instructions[pc]
        instructions[pc] += 1
        pc += offset
        steps += 1

    print("Part one:", steps)

    # Part 2

    instructions = read_input()

    pc = 0
    steps = 0

    while True:
        if pc >= len(instructions):
            break
        offset = instructions[pc]
        if offset >= 3:
            instructions[pc] -= 1
        else:
            instructions[pc] += 1
        pc += offset
        steps += 1

    print("Part two:", steps)
