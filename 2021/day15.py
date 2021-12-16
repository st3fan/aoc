#!/usr/bin/env python3


from queue import PriorityQueue
from more_itertools import flatten


class Graph:

    def __init__(self, num_vertices):
        self.v = num_vertices
        self.edges = [[-1 for _ in range(num_vertices)] for _ in range(num_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight_to):
        self.edges[u][v] = weight_to


def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


if __name__ == "__main__":

    with open("day15.input") as fp:
        data = [[int(e) for e in list(line.strip())] for line in fp.readlines()]
        size = len(data)

        graph = Graph(size * size)

        for y in range(size):
            for x in range(size-1):
                graph.add_edge((y*size)+x, (y*size)+x+1, data[y][x+1])
                graph.add_edge((y*size)+x+1, (y*size)+x, data[y][x])

        for y in range(size-1):
            for x in range(size):
                graph.add_edge((y*size)+x, ((y+1)*size)+x, data[y+1][x])
                graph.add_edge(((y+1)*size)+x, (y*size)+x, data[y][x])

        D = dijkstra(graph, 0)
        print("Part one:", D[size*size-1])

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

        graph = Graph(size * size)

        for y in range(size):
            for x in range(size-1):
                graph.add_edge((y*size)+x, (y*size)+x+1, data[y][x+1])

        for y in range(size-1):
            for x in range(size):
                graph.add_edge((y*size)+x, ((y+1)*size)+x, data[y+1][x])

        D = dijkstra(graph, 0)
        print("Part two:", D[size*size-1])

