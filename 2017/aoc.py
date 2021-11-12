

from dataclasses import dataclass
from itertools import islice, product


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


class Grid:
    def __init__(self, width, height, default=None):
        self.width = width
        self.height = height
        self.nodes = [default] * (width * height)

    def get(self, p):
        return self.nodes[p.x + (p.y * self.width)]

    def set(self, p, v, default=None):
        self.nodes[p.x + (p.y * self.width)] = v

    def count(self, value):
        return sum(node == value for node in self.nodes)


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

    def get(self, p):
        return self.nodes.get(p)

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

