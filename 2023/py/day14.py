#!/usr/bin/env python


from dataclasses import dataclass, field
from typing import List, Self


@dataclass
class Dish:
    data: List[List[str]]
    width: int = field(init=False)
    height: int = field(init=False)

    def hash(self) -> str:
        import hashlib

        return hashlib.sha1(str(self.data).encode("utf-8")).hexdigest()

    def __post_init__(self):
        self.width = len(self.data[0])
        self.height = len(self.data)

    @classmethod
    def from_path(cls, path: str) -> Self:
        with open(path) as f:
            data = f.read().strip()
            return cls([list(line) for line in data.split("\n")])

    def get(self, x: int, y: int) -> None | str:
        if x >= 0 and x < self.width:
            if y >= 0 and y < self.height:
                return self.data[y][x]
        return None

    def set(self, x: int, y: int, v: str):
        if x >= 0 and x < self.width:
            if y >= 0 and y < self.height:
                self.data[y][x] = v

    # Do "one tilt" and return how many rocks moved
    def tilt_north(self) -> int:
        moved = 0
        for x in range(len(self.data[0])):
            for y in range(len(self.data)):
                if self.get(x, y) == "O":
                    if self.get(x, y - 1) == ".":
                        self.set(x, y, ".")
                        self.set(x, y - 1, "O")
                        moved += 1
        return moved

    def tilt_south(self) -> int:
        moved = 0
        for x in range(len(self.data[0])):
            for y in range(len(self.data)):
                if self.get(x, y) == "O":
                    if self.get(x, y + 1) == ".":
                        self.set(x, y, ".")
                        self.set(x, y + 1, "O")
                        moved += 1
        return moved

    def tilt_east(self) -> int:
        moved = 0
        for x in range(len(self.data[0])):
            for y in range(len(self.data)):
                if self.get(x, y) == "O":
                    if self.get(x + 1, y) == ".":
                        self.set(x, y, ".")
                        self.set(x + 1, y, "O")
                        moved += 1
        return moved

    def tilt_west(self) -> int:
        moved = 0
        for x in range(len(self.data[0])):
            for y in range(len(self.data)):
                if self.get(x, y) == "O":
                    if self.get(x - 1, y) == ".":
                        self.set(x, y, ".")
                        self.set(x - 1, y, "O")
                        moved += 1
        return moved

    def load(self) -> int:
        total = 0
        for i, line in enumerate(self.data):
            total += line.count("O") * (self.height - i)
        return total

    def tilt_all_directions(self):
        while self.tilt_north() != 0:
            pass
        while self.tilt_west() != 0:
            pass
        while self.tilt_south() != 0:
            pass
        while self.tilt_east() != 0:
            pass


def part1() -> int:
    dish = Dish.from_path("day14.txt")
    while dish.tilt_north() != 0:
        pass
    return dish.load()


def part2() -> int:
    dish = Dish.from_path("day14.txt")
    seen = {}
    seen[dish.hash()] = 0
    n = 0
    while True:
        dish.tilt_all_directions()
        n += 1
        hash = dish.hash()
        if hash in seen:
            print("WE ARE AT", n, "AND HAVE SEEN THIS ONE AT", seen[hash], hash)
            cycle_length = n - seen[hash]
            print("THE CYCLE IS ", cycle_length, "AND STARTS AT", 0)
            x = (1_000_000_000 - n) % cycle_length
            print("WE WANT TO DO THIS ", x, "MORE TIMES")
            for _ in range(x):
                dish.tilt_all_directions()
            return dish.load()
        seen[hash] = n
    return 0


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
