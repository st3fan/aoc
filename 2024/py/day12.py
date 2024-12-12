#!/usr/bin/env python

from typing import NamedTuple

type PlantType = str


class Point(NamedTuple):
    x: int
    y: int


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


def price(region: Region, map: Map) -> int:
    return area(region) * perimeter(region, map)


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


def part1(map: Map) -> int:
    total_price = 0
    seen = set()
    for p in map.keys():
        if p not in seen:
            region = expand_region(map, p)
            total_price += price(region, map)
            seen |= region.points
    return total_price


if __name__ == "__main__":
    print("Part1", part1(load_map("day12.txt")))
