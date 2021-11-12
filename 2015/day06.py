#!/usr/bin/env python3


from aoc import Position, Grid
from dataclasses import dataclass


@dataclass
class Instruction:
    fr: Position
    to: Position
    op: str

    @classmethod
    def from_string(cls, s):
        c = s.split()
        if s.startswith("toggle"):
            return cls(Position.from_string(c[-3]), Position.from_string(c[-1]), "toggle")
        else:
            return cls(Position.from_string(c[-3]), Position.from_string(c[-1]), c[1])


def main():
    
    instructions = [Instruction.from_string(line.strip()) for line in open("day06.input").readlines()]

    # Part 1

    grid = Grid(1000, 1000, False)

    for i in instructions:
        for y in range(i.fr.y, i.to.y+1):
            for x in range(i.fr.x, i.to.x+1):
                match i.op:
                    case "toggle":
                        grid.set(Position(x, y), not grid.get(Position(x, y)))
                    case "on":
                        grid.set(Position(x, y), True)
                    case "off":
                        grid.set(Position(x, y), False)

    print("Part one:", grid.count(True))

    # Part 2

    grid = Grid(1000, 1000, 0)

    for i in instructions:
        for y in range(i.fr.y, i.to.y+1):
            for x in range(i.fr.x, i.to.x+1):
                match i.op:
                    case "toggle":
                        grid.set(Position(x, y), grid.get(Position(x, y)) + 2)
                    case "on":
                        grid.set(Position(x, y), grid.get(Position(x, y)) + 1)
                    case "off":
                        grid.set(Position(x, y), max(0, grid.get(Position(x, y)) - 1))

    print("Part two:", sum(node for node in grid.nodes))


if __name__ == "__main__":
    main()

