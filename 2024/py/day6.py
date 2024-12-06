#!/usr/bin/env python3


from aoc import Grid, Position


def load_input(path):
    with open(path) as fp:
        return [line.strip() for line in fp.readlines()]


# Map from direction to new direction if a wall is hit
DIRECTION_VECTOR_CHANGES = {
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
    (0, -1): (1, 0),
}


def part1():
    map = Grid.from_file("day6.txt", lambda v: v)

    v = (0, -1)  # Up

    positions = {}

    if p := map.find("^"):  # Conditional to keep mypy happy
        while True:
            positions[p] = 1
            np = Position(p.x + v[0], p.y + v[1])
            if np.x < 0 or np.y < 0 or np.x == map.width or np.y == map.height:
                break  # We fell off the map
            if map.get(np) == "#":
                # We hit a wall and turned
                v = DIRECTION_VECTOR_CHANGES[v]
            else:
                # We actually moved
                p = np
                positions[p] = 1
    return len(positions)


def part2():
    pass


if __name__ == "__main__":
    print("Part1:", part1())
    print("Part2:", part2())
