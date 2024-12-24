#!/usr/bin/env python

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Gate:
    ina: str
    op: str
    inb: str
    out: str

    @classmethod
    def from_str(cls, s: str) -> Gate:
        c = s.split()
        return Gate(c[0], c[1], c[2], c[4])


def read_input(path: str) -> tuple[dict[str, int], list[Gate]]:
    input = Path(path).read_text().strip()
    initial, gates = input.split("\n\n")

    return (
        {name: int(value) for name, value in [line.split(": ") for line in initial.split("\n")]},
        [Gate.from_str(s) for s in gates.split("\n")],
    )


def part1(state: dict[str, int], gates: list[Gate]) -> int:
    seen = set()
    while len(seen) != len(gates):  # Assumes they are all connected
        for gate in gates:
            if gate.ina in state and gate.inb in state:
                match gate.op:
                    case "AND":
                        state[gate.out] = state[gate.ina] & state[gate.inb]
                    case "OR":
                        state[gate.out] = state[gate.ina] | state[gate.inb]
                    case "XOR":
                        state[gate.out] = state[gate.ina] ^ state[gate.inb]
                seen.add(gate)

    keys = sorted([key for key in state.keys() if key[0] == "z"])
    return sum(2**i for i, key in enumerate(keys) if state[key] == 1)


def part2(state: dict[str, int], gates: list[Gate]) -> int:
    return 0


if __name__ == "__main__":
    state, gates = read_input("day24.txt")
    print("Part1:", part1(state, gates))
    print("Part2:", part2(state, gates))
