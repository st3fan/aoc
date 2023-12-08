#!/usr/bin/env python3


from dataclasses import dataclass
from functools import reduce
from itertools import cycle
from operator import mul
from typing import Self, Dict, Tuple

from sympy import lcm


@dataclass
class Node:
    id: str
    left: str
    right: str

    @classmethod
    def from_str(cls, s: str) -> Self:
        id, values = s.split(" = ")
        left, right = values.split(", ")
        return cls(id, left[1:], right[:-1])


def read_input() -> Tuple[str, Dict[str, Node]]:
    instructions, lines = open("day8.txt").read().split("\n\n")
    return instructions, {
        node.id: node
        for node in [Node.from_str(s.strip()) for s in lines.strip().split("\n")]
    }


def part1() -> int:
    instructions, nodes = read_input()
    current = "AAA"
    for steps, ins in enumerate(cycle(instructions), start=1):
        match ins:
            case "L":
                current = nodes[current].left
            case "R":
                current = nodes[current].right
        if current == "ZZZ":
            return steps
    return 0


def part2() -> int:
    def _steps(instructions: str, nodes: Dict[str, Node], start: str) -> int:
        current = start
        for steps, ins in enumerate(cycle(instructions), start=1):
            match ins:
                case "L":
                    current = nodes[current].left
                case "R":
                    current = nodes[current].right
            if current.endswith("Z"):
                return steps
        return 0

    ins, nodes = read_input()
    return lcm(_steps(ins, nodes, id) for id in nodes.keys() if id.endswith("A"))


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())