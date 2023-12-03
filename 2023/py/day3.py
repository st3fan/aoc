#!/usr/bin/env python3


from dataclasses import dataclass
from collections import defaultdict
from pathlib import Path
import re
from typing import Dict, Generator, List, Self, Set, Tuple


@dataclass(frozen=True)
class Position:
    x: int
    y: int


@dataclass(frozen=True)
class PartNumber:
    value: int
    start: Position
    end: Position


@dataclass(frozen=True)
class PartSymbol:
    c: str
    p: Position


SYMBOLS = "@&*=#%/+-$"
GEAR = "*"


@dataclass
class Schematic:
    lines: List[str]

    def get(self, p: Position) -> str|None:
        if p.y >= 0 and p.y < len(self.lines):
            if p.x >= 0 and p.x < len(self.lines[0]):
                return self.lines[p.y][p.x]
        return None

    def bounding_box_positions(self, part_number: PartNumber) -> Generator[Position, None, None]:
        for x in range(part_number.start.x-1, part_number.end.x+2):
            yield Position(x, part_number.start.y-1)
            yield Position(x, part_number.start.y+1)
        yield Position(part_number.start.x-1, part_number.start.y)
        yield Position(part_number.end.x+1, part_number.end.y)
    
    def adjecent_symbols(self, part_number) -> Generator[PartSymbol, None, None]:
        for p in self.bounding_box_positions(part_number):
            if c := self.get(p):
                if c in SYMBOLS:
                    yield PartSymbol(c, p)

    def part_numbers(self) -> Generator[Tuple[PartNumber, List[PartSymbol]], None, None]:
        for y, line in enumerate(self.lines):
            for m in re.finditer(r"(\d+)", line):
                part_number = PartNumber(int(m.group(1)), Position(m.span()[0], y), Position(m.span()[1]-1, y))
                symbols = self.adjecent_symbols(part_number)
                yield (part_number, list(symbols))

    @classmethod
    def from_file(cls, path: Path) -> Self:
        with open(path) as f:
            return cls(f.readlines())


def part1() -> int:
    total = 0
    schematic = Schematic.from_file(Path("day3.txt"))
    for (part_number, symbols) in schematic.part_numbers():
        print(part_number, symbols)
        if len(symbols):
            total += part_number.value
    return total


def part2() -> int:
    schematic = Schematic.from_file(Path("day3.txt"))

    part_numbers_by_gear_position: Dict[Position, Set[PartNumber]] = defaultdict(set)
    for (part_number, symbols) in schematic.part_numbers():
        for symbol in symbols:
            if symbol.c == GEAR:
                part_numbers_by_gear_position[symbol.p].add(part_number)

    total = 0
    for _, part_numbers in part_numbers_by_gear_position.items():
        if len(part_numbers) == 2:
            all = list(part_numbers)
            total += all[0].value * all[1].value
    return total

if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
