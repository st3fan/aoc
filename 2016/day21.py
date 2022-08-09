#!/usr/bin/env python3


def read_input():
    def parse_line(line):
        components = line.split()
        for i, v in enumerate(components):
            if v.isnumeric():
                components[i] = int(v)
        return components
    return [parse_line(line.strip()) for line in open("day21.input").readlines()]


def apply_operation(operation, s):
    match operation:
        case ["swap", "position", int(position_a), "with", "position", int(position_b)]:
            s[position_a], s[position_b] = s[position_b], s[position_a]
        case ["swap",  "letter", str(letter_a), "with", "letter", str(letter_b)]:
            pass
        case ["reverse", "positions", int(position_start), "through", int(position_end)]:
            pass
        case ["move", "position", int(position_a), "to", "position", int(position_b)]:
            pass
        case ["move", "position", int(position_a), "to", "position", int(position_b)]:
            pass
        case ["rotate", "right", int(steps) ,"steps"]:
            pass
        case ["rotate", "left", int(steps) ,"steps"]:
            pass
        case ["rotate", "based", "on", "position", "of", "letter", str(letter)]:
            pass
        case _:
            assert f"Unknown operation: {operation}"
    return s


def part1():
    s = list("abcdefgh")
    for op in read_input():
        s = apply_operation(op, s)
    return s


if __name__ == "__main__":
    print("Part one:", part1())