

from dataclasses import dataclass
from enum import Enum, IntEnum
from itertools import islice, product
from typing import Any, List


def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)


def manhattan_distance(v):
    return abs(v[0]) + abs(v[1])


def around(p):
    for q in product([-1, 0, 1], repeat=2):
        if q != (0,0):
            yield (p[0] + q[0], p[1] + q[1])


def sort_str(s):
    return "".join(sorted(s))


def same(e):
    return len(set(e)) == 1


def empty(e):
    return len(e) == 0


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    @classmethod
    def from_string(cls, s):
        c = s.split(",")
        return cls(int(c[0]), int(c[1]))

    def translate(self, dx, dy):
        return Position(self.x + dx, self.y + dy)

    @property
    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)


@dataclass(frozen=True)
class Line:
    start: Position
    end: Position

    @classmethod
    def from_string(cls, s):
        c = s.split()
        if c[1] == "->":
            return cls(Position.from_string(c[0]), Position.from_string(c[2]))

    def ishorizontal(self):
        return self.start.y == self.end.y

    def isvertical(self):
        return self.start.x == self.end.x


class Grid:
    @classmethod
    def from_file(cls, path, value_fn = lambda v: v):
        with open(path) as fp:
            rows = []
            for line in (line.strip() for line in fp.readlines()):
                rows.append([value_fn(e) for e in line])
            grid = cls(len(rows[0]), len(rows))
            grid.setnodes(rows)
            return grid

    def __init__(self, width, height, default=None):
        self.width = width
        self.height = height
        self.nodes = [default] * (width * height)

    def get(self, p):
        return self.nodes[p.x + (p.y * self.width)]

    def set(self, p, v, default=None):
        self.nodes[p.x + (p.y * self.width)] = v

    def setnodes(self, rows):
        assert self.height == len(rows)
        assert self.width == len(rows[0])
        self.nodes = []
        for row in rows:
            self.nodes += row

    def count(self, value):
        return sum(node == value for node in self.nodes)

    def neighbours(self, p, diagonal=False):
        if diagonal:
            positions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
        else:
            positions = [(-1,0), (1,0), (0,1), (0,-1)]
        for xo, yo in positions:
            px = p.x + xo
            py = p.y + yo
            if px >= 0 and px < self.width and py >= 0 and py < self.height:
                yield Position(px, py)

    def copy(self):
        grid = Grid(self.width, self.height)
        grid.nodes = list(self.nodes)
        return grid

    def fill(self, top_left: Position, width: int, height: int, value: Any):
        if top_left.x < self.width and top_left.y < self.height:
            for y in range(top_left.y, min(top_left.y + height, self.width)):
                for x in range(top_left.x, min(top_left.x + width, self.height)):
                    self.set(Position(x, y), value)

    def get_row(self, row: int) -> List[Any]:
        return self.nodes[row*self.width:(row+1)*self.width]

    def set_row(self, row: int, data: List[Any]):
        if len(data) != self.width:
            raise ValueError('row is not the correct size')
        self.nodes[row*self.width:(row+1)*self.width] = data

    def rotate_row(self, row: int, n: int):
        r = self.get_row(row)
        r = r[-n % len(r):] + r[:-n % len(r)]
        self.set_row(row,r)

    def get_column(self, column: int) -> List[Any]:
        return [self.nodes[column + (i*self.width)] for i in range(self.height)]

    def set_column(self, column: int, data: List[Any]):
        if len(data) != self.height:
            raise ValueError('column is not the correct size')
        for i in range(self.height):
            self.nodes[column + (i*self.width)] = data[i]

    def rotate_column(self, column: int, n: int):
        c = self.get_column(column)
        c = c[-n % len(c):] + c[:-n % len(c)]
        self.set_column(column, c)

    def dump(self):
        for row in range(self.height):
            print("|" + "".join(self.get_row(row)) + "|")


class InfiniteGrid:
    @classmethod
    def from_file(cls, path):
        grid = cls()
        with open(path) as fp:
            lines = fp.readlines()
            for y, line in enumerate([line.strip() for line in lines]):
                for x, v in enumerate(line):
                    grid.set(Position(x, len(lines) - y - 1), v)
        return grid

    def __init__(self):
        self.nodes = dict()

    def get(self, p, default=None):
        return self.nodes.get(p, default)

    def set(self, p, v):
        self.nodes[p] = v

    def remove(self, p):
        return self.nodes.pop(p, None)

    def maxx(self):
        return max(p.x for p in self.nodes)

    def maxy(self):
        return max(p.y for p in self.nodes)


class Turtle:

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def __init__(self, position=Position(0,0)):
        self.position = position
        self.direction = Turtle.UP

    def left(self):
        match self.direction:
            case Turtle.UP:
                self.direction = Turtle.LEFT
            case Turtle.RIGHT:
                self.direction = Turtle.UP
            case Turtle.DOWN:
                self.direction = Turtle.RIGHT
            case Turtle.LEFT:
                self.direction = Turtle.DOWN

    def right(self):
        match self.direction:
            case Turtle.UP:
                self.direction = Turtle.RIGHT
            case Turtle.RIGHT:
                self.direction = Turtle.DOWN
            case Turtle.DOWN:
                self.direction = Turtle.LEFT
            case Turtle.LEFT:
                self.direction = Turtle.UP

    def forward(self):
        match self.direction:
            case Turtle.UP:
                self.position = Position(self.position.x, self.position.y+1)
            case Turtle.RIGHT:
                self.position = Position(self.position.x+1, self.position.y)
            case Turtle.DOWN:
                self.position = Position(self.position.x, self.position.y-1)
            case Turtle.LEFT:
                self.position = Position(self.position.x-1, self.position.y)


class CartesianDirection(Enum):
    LEFT = 0
    RIGHT = 1
    FORWARD = 2
    BACKWARD = 3
    UP = 4
    DOWN = 5

    @classmethod
    def from_str(cls, s: str) -> "CartesianDirection":
        if s.lower() in ('l', 'left'):
            return CartesianDirection.LEFT
        if s.lower() in ('r', 'right'):
            return CartesianDirection.RIGHT
        if s.lower() in ('f', 'forward'):
            return CartesianDirection.FORWARD
        if s.lower() in ('b', 'backward'):
            return CartesianDirection.BACKWARD
        if s.lower() in ('u', 'up'):
            return CartesianDirection.UP
        if s.lower() in ('d', 'down'):
            return CartesianDirection.DOWN
        raise ValueError(f"don't know how to convert literal <{s}> into a CartesianDirection")


class CardinalDirection(IntEnum):
    N = 0
    E = 1
    S = 2
    W = 3

    @classmethod
    def from_str(cls, s: str) -> "CardinalDirection":
        if s.lower() in ('n', 'north'):
            return CardinalDirection.N
        if s.lower() in ('e', 'east'):
            return CardinalDirection.E
        if s.lower() in ('s', 'south'):
            return CardinalDirection.S
        if s.lower() in ('w', 'west'):
            return CardinalDirection.W
        raise ValueError(f"don't know how to convert literal <{s}> into a CardinalDirection")

    def turn(self, direction: CartesianDirection) -> "CardinalDirection":
        values: List[CardinalDirection] = list(CardinalDirection)
        index = values.index(self)
        match direction:
            case CartesianDirection.LEFT:
                return values[-1] if values[0] == self else values[index - 1]
            case CartesianDirection.RIGHT:
                return values[0] if values[-1] == self else values[index + 1]
            case _:
                raise ValueError("CardinalDirection can only turn LEFT or RIGHT")


class Santa:
    """Like a turtle, except we move N/S/E/W"""

    def __init__(self, position=Position(0,0)):
        self.position = position

    def west(self):
        self.position = Position(self.position.x-1, self.position.y)

    def east(self):
        self.position = Position(self.position.x+1, self.position.y)

    def north(self):
        self.position = Position(self.position.x, self.position.y-1)

    def south(self):
        self.position = Position(self.position.x, self.position.y+1)


if __name__ == "__main__":
    grid = Grid(5, 5, 0)

    #grid.set_row(3, [1, 2, 3, 4, 5])
    #grid.set_row(3, [v+3 for v in grid.get_row(3)])

    grid.set_column(3, [1, 2, 3, 4, 5])
    grid.rotate_column(3, 1)
    #grid.set_column(3, [v+3 for v in grid.get_column(3)])

    print(grid.nodes[0:5])
    print(grid.nodes[5:10])
    print(grid.nodes[10:15])
    print(grid.nodes[15:20])
    print(grid.nodes[20:25])
