#!/usr/bin/env python3


from collections import Counter
from copy import deepcopy


TOP=0
RIGHT=1
BOTTOM=2
LEFT=3


def top(tile):
    return tile['edges'][TOP]

def right(tile):
    return tile['edges'][RIGHT]

def bottom(tile):
    return tile['edges'][BOTTOM]

def left(tile):
    return tile['edges'][LEFT]


def parse_edges(data):
    return [data[0],                       # top
            "".join([s[9] for s in data]), # right
            data[9],                       # bottom
            "".join([s[0] for s in data])] # left


def parse_tile(data):
    lines = data.split("\n")
    return {"id": int(lines[0][5:-1]),
            "edges": parse_edges(lines[1:11])}


def parse_input(path):
    with open(path) as f:
        return [parse_tile(data) for data in f.read().split("\n\n")]


def rotate(tile):
    tile['edges'] = [
        tile['edges'][LEFT],    # TOP
        tile['edges'][TOP],     # RIGHT
        tile['edges'][RIGHT],   # BOTTOM
        tile['edges'][BOTTOM],  # LEFT
    ]
    return tile


def fliph(tile):
    left = tile['edges'][LEFT]
    right = tile['edges'][RIGHT]
    tile['edges'][LEFT] = right
    tile['edges'][RIGHT] = left
    tile['edges'][TOP] = tile['edges'][TOP][::-1]
    tile['edges'][BOTTOM] = tile['edges'][BOTTOM][::-1]
    return tile


def flipv(tile):
    top = tile['edges'][TOP]
    bottom = tile['edges'][BOTTOM]
    tile['edges'][TOP] = bottom
    tile['edges'][BOTTOM] = top
    tile['edges'][LEFT] = tile['edges'][LEFT][::-1]
    tile['edges'][RIGHT] = tile['edges'][RIGHT][::-1]
    return tile


def transform_tile(tile, *transformations):
    tile = deepcopy(tile)
    for t in transformations:
        tile = t(tile)
    return tile


def variations(tile):
    return [
        transform_tile(tile),

        transform_tile(tile, fliph),
        transform_tile(tile, flipv),
        transform_tile(tile, fliph, flipv),
        transform_tile(tile, flipv, fliph),

        transform_tile(tile, rotate),
        transform_tile(tile, rotate, rotate),
        transform_tile(tile, rotate, rotate, rotate),

        transform_tile(tile, fliph),
        transform_tile(tile, fliph, rotate),
        transform_tile(tile, fliph, rotate, rotate),
        transform_tile(tile, fliph, rotate, rotate, rotate),

        transform_tile(tile, flipv),
        transform_tile(tile, flipv, rotate),
        transform_tile(tile, flipv, rotate, rotate),
        transform_tile(tile, flipv, rotate, rotate, rotate),

        transform_tile(tile, fliph, flipv),
        transform_tile(tile, fliph, flipv, rotate),
        transform_tile(tile, fliph, flipv, rotate, rotate),
        transform_tile(tile, fliph, flipv, rotate, rotate, rotate),
    ]


HEIGHT = 3
WIDTH = 3


tiles = parse_input("../../resources/advent_of_code/2020/day20/test")
tiles_by_id = {tile['id']: tile for tile in tiles}

grid = [None, None, None,
        None, None, None,
        None, None, None]

def grid_get(grid, row, col):
    return grid[row * WIDTH + col]

def grid_set(grid, row, col, tile):
    grid[row * WIDTH + col] = tile


def available_tiles(tiles, grid):
    tile_ids = [tile['id'] for tile in grid if tile is not None]
    for tile in tiles:
        if tile['id'] not in tile_ids:
            for v in variations(tile):
                yield v


def tile_fits(tile, grid, row, col):
    # Check top
    if row > 0 and bottom(grid_get(grid, row-1, col)) != top(tile):
        return False
    # Check left
    if col > 0 and right(grid_get(grid, row, col-1)) != left(tile):
        return False
    return True

def find_empty(grid):
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if grid_get(grid, row, col) is None:
                return (row, col)

def solve(grid):
    pos = find_empty(grid)
    if not pos:
        return True

    row, col = pos

    for tile in available_tiles(tiles, grid):
        if tile_fits(tile, grid, row, col):
            grid_set(grid, row, col, tile)
            if solve(grid):
                return True
            grid_set(grid, row, col, None)
    return False

if __name__ == "__main__":

    for tile in variations(tiles[0]):
        print(tile)

    #for tile in available_tiles(tiles, grid):
    #    print(tile['id'])

    #solve1()
    #solve(grid, 0, 0)

    solve(grid)
    print(grid)

    #print(grid[0][0] * grid[0][2] * grid[2][0] * grid[2][2])

    # counter = Counter()
    # for tile in tiles:
    #     for v in variations(tile):
    #         counter.update(v['edges'])
    # print(counter)

    # tile = {"edges": ["abc", "def", "ghi", "jkl"]}
    # for v in variations(tile):
    #     print(v['edges'])

