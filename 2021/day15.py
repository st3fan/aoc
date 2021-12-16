#!/usr/bin/env python3


from heapq import heappush, heappop
from time import time

from more_itertools import flatten

import numpy as np


def dijkstra(grid, size, start_vertex):
    D = [float('inf')] * (size*size)
    D[start_vertex] = 0

    pq = []
    heappush(pq, (0, start_vertex))

    while len(pq):
        (_, current_vertex) = heappop(pq)

        x = current_vertex % size
        y = current_vertex // size

        neighbours = []
        if x > 0:
            neighbours.append(current_vertex-1)
        if x < (size-1):
            neighbours.append(current_vertex+1)
        if y > 0:
            neighbours.append(current_vertex-size)
        if y < (size-1):
            neighbours.append(current_vertex+size)

        for neighbor in neighbours:
            distance = grid[neighbor]
            old_cost = D[neighbor]
            new_cost = D[current_vertex] + distance
            if new_cost < old_cost:
                heappush(pq, (old_cost+distance, neighbor))
                D[neighbor] = new_cost
    return D


def dijkstra2(grid, start_vertex):
    D = np.full_like(grid, 1_000_000, dtype=np.uint64)
    D[start_vertex] = 0

    size = len(grid)

    pq = []
    heappush(pq, (0, start_vertex))

    while len(pq):
        (_, current_vertex) = heappop(pq)

        x = current_vertex[0]
        y = current_vertex[1]

        neighbours = []
        if x > 0:
            neighbours.append((x-1,y))
        if x < (size-1):
            neighbours.append((x+1,y))
        if y > 0:
            neighbours.append((x, y-1))
        if y < (size-1):
            neighbours.append((x, y+1))

        for neighbor in neighbours:
            distance = grid[neighbor]
            old_cost = D[neighbor]
            new_cost = D[current_vertex] + distance
            if new_cost < old_cost:
                heappush(pq, (old_cost+distance, neighbor))
                D[neighbor] = new_cost
    return D


if __name__ == "__main__":

    if True:
        with open("day15.input") as fp:
            data = [[int(e) for e in list(line.strip())] for line in fp.readlines()]
            size = len(data)
            grid = list(flatten(data))

            start = time()
            D = dijkstra(grid, size, 0)
            print("Part one:", D[(size*size)-1], "in", time()-start)


    if True:
        with open("day15.input") as fp:
            data = [[int(e) for e in list(line.strip())] for line in fp.readlines()]
            size = len(data)

            for n in range(4):
                for y in range(size):
                    for x in range(size):
                        data[y].append(((data[y][x]+n)%9)+1)

            for n in range(4):
                for y in range(size):
                    line = [((e+n)%9)+1 for e in data[y]]
                    data.append(line)

            size = len(data)
            grid = list(flatten(data))

            start = time()
            D = dijkstra(grid, size, 0)
            print("Part two:", D[size*size-1], "in", time()-start)

    if True:
        with open("day15.input") as fp:
            data = [[int(e) for e in list(line.strip())] for line in fp.readlines()]
            grid = np.array(data, dtype=np.uint64)
            size = len(grid)

            start = time()
            D = dijkstra2(grid, (0,0))
            print("Part one (with numpy arrays):", D[-1, -1], "in", time()-start)


    if True:
        with open("day15.input") as fp:
            data = [[int(e) for e in list(line.strip())] for line in fp.readlines()]
            size = len(data)

            for n in range(4):
                for y in range(size):
                    for x in range(size):
                        data[y].append(((data[y][x]+n)%9)+1)

            for n in range(4):
                for y in range(size):
                    line = [((e+n)%9)+1 for e in data[y]]
                    data.append(line)

            grid = np.array(data, dtype=np.uint64)
            size = len(grid)

            start = time()
            D = dijkstra2(grid, (0,0))
            print("Part two(with numpy arrays):", D[-1, -1], "in", time()-start)

