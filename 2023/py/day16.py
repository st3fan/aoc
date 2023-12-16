#!/usr/bin/env python

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Iterator, List, Self, Set


class Direction(Enum):
    N = auto()
    S = auto()
    W = auto()
    E = auto()


@dataclass
class Position:
    x: int
    y: int

    def peek(self, direction: Direction) -> Position:
        match direction:
            case Direction.N:
                return Position(self.x, self.y - 1)
            case Direction.S:
                return Position(self.x, self.y + 1)
            case Direction.W:
                return Position(self.x - 1, self.y)
            case Direction.E:
                return Position(self.x + 1, self.y)

    def move(self, direction: Direction):
        match direction:
            case Direction.N:
                self.y -= 1
            case Direction.S:
                self.y += 1
            case Direction.W:
                self.x -= 1
            case Direction.E:
                self.x += 1


class TileType(Enum):
    EMPTY = "."
    RMIRROR = "\\"
    LMIRROR = "/"
    VSPLITTER = "|"
    HSPLITTER = "-"


@dataclass
class Tile:
    type: TileType
    energized: Set[Direction] = field(default_factory=set)

    @classmethod
    def from_str(cls, s: str) -> Self:
        return cls(TileType(s))


@dataclass
class Grid:
    data: List[List[Tile]]

    width: int = field(init=False)
    height: int = field(init=False)

    def __post_init__(self):
        self.width = len(self.data[0])
        self.height = len(self.data)

    def contains(self, p: Position) -> bool:
        return p.x >= 0 and p.x < self.width and p.y >= 0 and p.y < self.height

    def get(self, p: Position) -> Tile:
        if p.x >= 0 and p.x < self.width:
            if p.y >= 0 and p.y < self.height:
                return self.data[p.y][p.x]
        raise Exception(f"Grid position <{p}> out of bounds")

    def set(self, p: Position, tile: Tile):
        if p.x >= 0 and p.x < self.width:
            if p.y >= 0 and p.y < self.height:
                self.data[p.y][p.x] = tile
                return
        raise Exception(f"Grid position <{p}> out of bounds")

    def energized(self) -> int:
        count = 0
        for y in range(self.height):
            for x in range(self.width):
                count += len(self.data[y][x].energized) != 0
        return count

    def reset(self):
        for y in range(self.height):
            for x in range(self.width):
                self.data[y][x].energized.clear()

    @classmethod
    def from_path(cls, path: str) -> Self:
        with open(path) as f:
            data = f.read().strip()
            return cls([[Tile.from_str(c) for c in line] for line in data.split("\n")])


@dataclass
class Beam:
    position: Position
    direction: Direction

    def move(self, grid: Grid) -> Beam | None:
        if tile := grid.get(self.position):
            match tile.type:
                case TileType.EMPTY:
                    self.position.move(self.direction)
                case TileType.RMIRROR:  # \
                    match self.direction:
                        case Direction.N:
                            self.position.move(Direction.W)
                            self.direction = Direction.W
                        case Direction.S:
                            self.position.move(Direction.E)
                            self.direction = Direction.E
                        case Direction.E:
                            self.position.move(Direction.S)
                            self.direction = Direction.S
                        case Direction.W:
                            self.position.move(Direction.N)
                            self.direction = Direction.N
                case TileType.LMIRROR:  # /
                    match self.direction:
                        case Direction.N:
                            self.position.move(Direction.E)
                            self.direction = Direction.E
                        case Direction.S:
                            self.position.move(Direction.W)
                            self.direction = Direction.W
                        case Direction.E:
                            self.position.move(Direction.N)
                            self.direction = Direction.N
                        case Direction.W:
                            self.position.move(Direction.S)
                            self.direction = Direction.S
                case TileType.VSPLITTER:  # |
                    match self.direction:
                        case Direction.N | Direction.S:
                            self.position.move(self.direction)
                        case Direction.E | Direction.W:
                            new_beam = Beam(
                                self.position.peek(Direction.N), Direction.N
                            )
                            self.position.move(Direction.S)
                            self.direction = Direction.S
                            return new_beam
                case TileType.HSPLITTER:  # -
                    match self.direction:
                        case Direction.E | Direction.W:
                            self.position.move(self.direction)
                        case Direction.N | Direction.S:
                            new_beam = Beam(
                                self.position.peek(Direction.E), Direction.E
                            )
                            self.position.move(Direction.W)
                            self.direction = Direction.W
                            return new_beam
        return None


def solve(grid: Grid, position: Position, direction: Direction) -> int:
    beams: List[Beam] = [Beam(position, direction)]

    while len(beams) != 0:
        # Delete all the beams that have moved off the grid
        beams = [beam for beam in beams if grid.contains(beam.position)]

        # Delete all the beams that are now energizing tiles in direction
        # already seen This kills infinite looping.
        beams = [
            beam
            for beam in beams
            if beam.direction not in grid.get(beam.position).energized
        ]

        # Energize all the tiles the beams are on
        for beam in beams:
            grid.get(beam.position).energized.add(beam.direction)

        # Move all the beams to the next step. Possibly adding new beams from splitters.
        for beam in beams.copy():
            if new_beam := beam.move(grid):
                beams.append(new_beam)

    return grid.energized()


def part1() -> int:
    return solve(Grid.from_path("day16.txt"), Position(0, 0), Direction.E)


def part2() -> int:
    grid = Grid.from_path("day16.txt")
    m = 0
    for x in range(grid.width):
        m = max(m, solve(grid, Position(x, 0), Direction.S))
        grid.reset()
        m = max(m, solve(grid, Position(x, grid.height - 1), Direction.N))
        grid.reset()
    for y in range(grid.height):
        m = max(m, solve(grid, Position(0, y), Direction.E))
        grid.reset()
        m = max(m, solve(grid, Position(grid.width - 1, y), Direction.W))
        grid.reset()
    return m


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
