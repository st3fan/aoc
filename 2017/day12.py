#!/usr/bin/env python3


import networkx as nx


def parse_line(line):
    c = line.split(maxsplit=2)
    return [int(c[0]), [int(i) for i in c[2].split(", ")]]


def read_input():
    with open("day12.input") as fp:
        return [parse_line(line.strip()) for line in fp.readlines()]


if __name__ == "__main__":

    graph = nx.Graph()
    for (program_id, connected_to) in read_input():
        graph.add_edges_from([(program_id, i) for i in connected_to])

    print("Part one:", len(nx.node_connected_component(graph, 0)))

    print("Part two:", len(list(nx.connected_components(graph))))
