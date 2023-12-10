#!/usr/bin/env python


from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Self


class Direction(Enum):
    N = auto()
    S = auto()
    W = auto()
    E = auto()


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def move(self, direction: Direction) -> "Position":
        match direction:
            case Direction.N:
                return Position(self.x, self.y - 1)
            case Direction.S:
                return Position(self.x, self.y + 1)
            case Direction.W:
                return Position(self.x - 1, self.y)
            case Direction.E:
                return Position(self.x + 1, self.y)


PIPE_TO_DIRECTIONS = {
    "|": [Direction.N, Direction.S],
    "-": [Direction.W, Direction.E],
    "7": [Direction.S, Direction.W],
    "F": [Direction.S, Direction.E],
    "J": [Direction.N, Direction.W],
    "L": [Direction.N, Direction.E],
}


@dataclass
class Grid:
    data: List[List[str]]
    width: int = field(init=False)
    height: int = field(init=False)

    def __post_init__(self):
        self.width = len(self.data[0])
        self.height = len(self.data)

    def find_start(self) -> Position:
        for y in range(self.height):
            for x in range(self.width):
                if self.data[y][x] == "S":
                    return Position(x, y)
        raise Exception("No starting position found")

    def get(self, p: Position) -> None | str:
        if p.x >= 0 and p.x < self.width:
            if p.y >= 0 and p.y < self.height:
                return self.data[p.y][p.x]
        return None

    def set(self, p: Position, v: str):
        if p.x >= 0 and p.x < self.width:
            if p.y >= 0 and p.y < self.height:
                self.data[p.y][p.x] = v

    def next_positions(self, p: Position) -> List[Position]:
        return [p.move(d) for d in self.possible_directions(p)]

    def resolve_start_tile(self, p: Position) -> str:
        # This is pretty horrible
        directions = []
        if self.get(Position(p.x, p.y - 1)) in ("|", "7", "F"):
            directions.append(Direction.N)
        if self.get(Position(p.x, p.y + 1)) in ("|", "L", "J"):
            directions.append(Direction.S)
        if self.get(Position(p.x - 1, p.y)) in ("-", "L", "F"):
            directions.append(Direction.W)
        if self.get(Position(p.x + 1, p.y)) in ("-", "7", "J"):
            directions.append(Direction.E)
        for k, v in PIPE_TO_DIRECTIONS.items():
            if v == directions:
                return k
        raise Exception("Can't resolve start tile")

    def possible_directions(self, p: Position) -> List[Direction]:
        t = self.get(p)
        if t == "S":
            t = self.resolve_start_tile(p)
        match t:
            case "|":
                return [Direction.N, Direction.S]
            case "-":
                return [Direction.E, Direction.W]
            case "L":
                return [Direction.N, Direction.E]
            case "J":
                return [Direction.N, Direction.W]
            case "7":
                return [Direction.S, Direction.W]
            case "F":
                return [Direction.S, Direction.E]
        raise Exception(f"Invalid tile <{self.get(p)}>")

    @classmethod
    def from_path(cls, path: str) -> Self:
        with open(path) as f:
            data = f.read().strip()
            return cls([list(line) for line in data.split("\n")])


def part1() -> int:
    grid = Grid.from_path("day10.txt")
    position = grid.find_start()
    seen = set([position])

    # Since we're chasing a loop we don't need to do anything fancy recurive
    while True:
        for position in grid.next_positions(position):
            if position not in seen:
                seen.add(position)
                break
        else:
            break
    return len(seen) // 2


if __name__ == "__main__":
    print("Part 1:", part1())
