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


def stuck(map):
    v = (0, -1)  # Up

    positions = {}  # (position, v)

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
                key = (np, v)
                if key in positions:
                    return True
                # We actually moved
                p = np
                positions[key] = 1
    return False


def part2():
    map = Grid.from_file("day6.txt", lambda v: v)
    total = 0
    for y in range(map.height):
        for x in range(map.width):
            p = Position(x, y)
            if map.get(p) == ".":
                map.set(p, "#")
                if stuck(map):
                    total += 1
                map.set(p, ".")
    return total


if __name__ == "__main__":
    print("Part1:", part1())
    print("Part2:", part2())
