#!/usr/bin/env python

from operator import attrgetter
from typing import NamedTuple

from more_itertools import split_when

type PlantType = str


class Point(NamedTuple):
    x: float
    y: float


type Map = dict[Point, PlantType]


class Region(NamedTuple):
    points: set[Point]
    plant_type: PlantType


def load_map(path: str) -> Map:
    points: Map = {}
    with open(path) as fp:
        for y, line in enumerate(fp):
            for x, c in enumerate(line.strip()):
                points[Point(x=x, y=y)] = c
        return points


def area(region: Region) -> int:
    return len(region.points)


def perimeter(region: Region, map: Map) -> int:
    t = 0
    for p in region.points:
        for v in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            neighbour = Point(x=p.x + v[0], y=p.y + v[1])
            if neighbour not in map or map[neighbour] != region.plant_type:
                t += 1
    return t


def sides(region: Region, map: Map) -> int:
    side_points = set()
    for p in region.points:
        for v in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            sp = Point(p.x + v[0], p.y + v[1])
            if sp not in map or map[sp] != region.plant_type:
                np = Point(p.x + (0.25 * v[0]), p.y + (0.25 * v[1]))
                side_points.add(np)

    w = int(max(p[0] for p in map.keys()) + 1)
    h = int(max(p[1] for p in map.keys()) + 1)

    total = 0

    # Scan vertically Group by x diff is 1.0
    for y in range(h + 1):
        points = sorted([p for p in side_points if p.y == (y - 0.25)], key=attrgetter("x"))
        total += len(list(split_when(points, lambda a, b: b.x - a.x > 1.0)))  # ?
        points = sorted([p for p in side_points if p.y == (y - 0.75)], key=attrgetter("x"))
        total += len(list(split_when(points, lambda a, b: b.x - a.x > 1.0)))  # ?

    # Scan horitontally Group by y diff is 1.0
    for x in range(w + 1):
        points = sorted([p for p in side_points if p.x == (x - 0.25)], key=attrgetter("y"))
        total += len(list(split_when(points, lambda a, b: b.y - a.y > 1.0)))
        points = sorted([p for p in side_points if p.x == (x - 0.75)], key=attrgetter("y"))
        total += len(list(split_when(points, lambda a, b: b.y - a.y > 1.0)))

    return total


def expand_region(map: Map, p: Point) -> Region:
    points: set[Point] = set()
    plant_type: PlantType = map[p]

    def dfs(p: Point):
        if p in points or (p not in map or map[p] != plant_type):
            return
        points.add(p)
        for v in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            dfs(Point(x=p.x + v[0], y=p.y + v[1]))

    dfs(p)

    return Region(points=points, plant_type=plant_type)


def price(region: Region, map: Map) -> int:
    return area(region) * perimeter(region, map)


def discounted_price(region: Region, map: Map) -> int:
    return area(region) * sides(region, map)


def calculate(map: Map, price_fn) -> int:
    total_price = 0
    seen = set()
    for p in map.keys():
        if p not in seen:
            region = expand_region(map, p)
            total_price += price_fn(region, map)
            seen |= region.points
    return total_price


if __name__ == "__main__":
    print("Part1", calculate(load_map("day12.txt"), price))
    print("Part2", calculate(load_map("day12.txt"), discounted_price))
