#!/usr/bin/env python3


# Optimized for speed


# From https://stackoverflow.com/a/72914390/56837
def profile(fnc):
    """
    Profiles any function in following class just by adding @profile above function
    """
    import cProfile, pstats, io

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = "cumulative"  # Ordered
        ps = pstats.Stats(pr, stream=s).strip_dirs().sort_stats(sortby)
        n = 25
        ps.print_stats(n)
        # ps.dump_stats("profile.prof")
        print(s.getvalue())
        return retval

    return inner


def load_input(path):
    with open(path) as fp:
        return [[ord(c) for c in line.strip()] for line in fp.readlines()]


# Map from direction to new direction if a wall is hit
DIRECTION_VECTOR_CHANGES = {
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
    (0, -1): (1, 0),
}


def find(map, width, height, c):
    for y in range(height):
        for x in range(width):
            if map[y][x] == c:
                return x, y


def part1():
    map = load_input("day6.txt")
    width = len(map[0])
    height = len(map)

    v = (0, -1)  # Up

    positions = {}

    if p := find(map, width, height, 94):  # Conditional to keep mypy happy
        while True:
            positions[p] = 1
            np = (p[0] + v[0], p[1] + v[1])
            if np[0] < 0 or np[1] < 0 or np[0] == width or np[1] == height:
                break  # We fell off the map
            if map[np[1]][np[0]] == 35:
                # We hit a wall and turned
                v = DIRECTION_VECTOR_CHANGES[v]
            else:
                # We actually moved
                p = np
                positions[p] = 1
    return positions


def stuck(map, px, py, width, height):
    v = (0, -1)  # Up

    positions = {}

    while True:
        # positions[p] = 1
        nx = px + v[0]
        ny = py + v[1]
        if nx < 0 or ny < 0 or nx == width or ny == height:
            return False
        if map[ny][nx] == 35:
            # We hit a wall and turned
            v = DIRECTION_VECTOR_CHANGES[v]
        else:
            key = (nx, ny, v)
            if key in positions:
                return True
            # We actually moved
            px = nx
            py = ny
            positions[key] = None


@profile
def part2(positions):
    map = load_input("day6.txt")
    width = len(map[0])
    height = len(map)
    sx, sy = find(map, width, height, 94)

    total = 0
    for x, y in positions:
        if map[y][x] == 46:
            map[y][x] = 35
            if stuck(map, sx, sy, width, height):
                total += 1
            map[y][x] = 46
    return total


if __name__ == "__main__":
    positions = part1()
    print("Part1:", len(positions))
    print("Part2:", part2(positions))
