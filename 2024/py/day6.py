#!/usr/bin/env python3


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


def find(map, c):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == c:
                return (x, y)


def part1():
    map = load_input("day6.txt")
    width = len(map[0])
    height = len(map)

    v = (0, -1)  # Up

    positions = {}

    if p := find(map, 94):  # Conditional to keep mypy happy
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


def stuck(map, p, width, height):
    v = (0, -1)  # Up

    positions = {}  # (position, v)

    while True:
        positions[p] = 1
        np = (p[0] + v[0], p[1] + v[1])
        if np[0] < 0 or np[1] < 0 or np[0] == width or np[1] == height:
            break  # We fell off the map
        if map[np[1]][np[0]] == 35:
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


# @profile
def part2(positions):
    map = load_input("day6.txt")
    width = len(map[0])
    height = len(map)
    start = find(map, 94)

    total = 0
    for p in positions:
        if map[p[1]][p[0]] == 46:
            map[p[1]][p[0]] = 35
            if stuck(map, start, width, height):
                total += 1
            map[p[1]][p[0]] = 46
    return total


if __name__ == "__main__":
    positions = part1()
    print("Part1:", len(positions))
    print("Part2:", part2(positions))
