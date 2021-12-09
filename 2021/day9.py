#!/usr/bin/env python3


from aoc import Grid, Position


def low_points(grid):
    for y in range(grid.height):
        for x in range(grid.width):
            p = Position(x, y)
            if grid.get(p) < min(grid.get(q) for q in grid.neighbours(p, diagonal=False)):
                yield p


def part1():
    grid = Grid.from_file("day9.input", value_fn=int)
    return sum(grid.get(p)+1 for p in low_points(grid))


def adjecent(grid, p, seen):
    def _check(n):
        return n not in seen and grid.get(n) > grid.get(p) and grid.get(n) != 9
    return [n for n in grid.neighbours(p, diagonal=False) if _check(n)]


def extend_group(grid, points, seen):
    for p in points:
        seen.add(p)
        if adj := adjecent(grid, p, seen):
            extend_group(grid, adj, seen)


def basin_points(grid, low_point):
    seen = set([low_point])
    if adj := adjecent(grid, low_point, seen):
        extend_group(grid, adj, seen)
    return seen


def part2():
    grid = Grid.from_file("day9.input", value_fn=int)
    sizes = sorted([len(basin_points(grid, p)) for p in low_points(grid)], reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


if __name__ == "__main__":
    print("Part one:", part1())
    print("Part two:", part2())

