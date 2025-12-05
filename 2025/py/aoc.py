from collections.abc import Iterator
from dataclasses import dataclass
from typing import Callable, Self


@dataclass(frozen=True)
class Position:
    x: int
    y: int


@dataclass(frozen=True)
class Size:
    h: int
    w: int


type GridNodeConstructor[T] = Callable[[str], T]


@dataclass
class Grid[T]:
    size: Size
    nodes: list[T]

    def positions(self, *, value: T | None = None) -> Iterator[Position]:
        for y in range(self.size.h):
            for x in range(self.size.w):
                if value is None:
                    yield Position(x=x, y=y)
                elif self.get(Position(x, y)) == value:
                    yield Position(x=x, y=y)

    def get(self, p: Position) -> T | None:
        if p.x >= 0 and p.x < self.size.w and p.y >= 0 and p.y < self.size.h:
            return self.nodes[(p.y * self.size.w) + p.x]

    def set(self, p: Position, value: T):
        if p.x >= 0 and p.x < self.size.w and p.y >= 0 and p.y < self.size.h:
            self.nodes[(p.y * self.size.w) + p.x] = value

    def adjecent_positions(self, p: Position, *, value=T | None, diagonal: bool = True) -> list[Position]:
        adjecent = []
        for v in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
            if r := self.get(Position(x=p.x + v[0], y=p.y + v[1])):
                if value is not None:
                    if r == value:
                        adjecent.append(r)
                else:
                    adjecent.append(r)
        if diagonal:
            for v in {(-1, -1), (-1, 1), (1, 1), (1, -1)}:
                if r := self.get(Position(x=p.x + v[0], y=p.y + v[1])):
                    if value is not None:
                        if value == r:
                            adjecent.append(r)
                    else:
                        adjecent.append(r)
        return adjecent

    @classmethod
    def from_file(cls, path: str, *, node_constructor: GridNodeConstructor = str) -> Self:
        with open(path) as fp:
            nodes: list[T] = []
            width = 0
            height = 0
            for line in (line.strip() for line in fp.readlines()):
                width = len(line)
                height += 1
                nodes += [node_constructor(e) for e in line]
            return cls(size=Size(w=width, h=height), nodes=nodes)
