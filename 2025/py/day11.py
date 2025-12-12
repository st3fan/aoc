#!/usr/bin/env python3


from collections import defaultdict
from collections.abc import Iterator


def read_input(path: str) -> dict[str, set[str]]:
    connectors = defaultdict(set)
    with open(path) as fp:
        for line in fp.readlines():
            f, t = line.strip().split(": ")
            for t in t.split():
                connectors[f].add(t)
    return connectors


def xfind_all_paths(graph, start, end, get_neighbors):
    """Find all paths from start to end, visiting each node at most once."""
    paths = []

    def dfs(current, path):
        if current == end:
            paths.append(path[:])
            return

        for neighbor in get_neighbors(graph, current):
            if neighbor not in path:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()

    dfs(start, [start])
    return paths


def find_all_paths(graph, start, end, get_neighbors) -> Iterator[int]:
    """Find all paths from start to end, visiting each node at most once."""

    def dfs(current, path) -> Iterator[int]:
        if current == end:
            yield 1  # path
            return

        for neighbor in get_neighbors(graph, current):
            if neighbor not in path:
                path.append(neighbor)
                yield from dfs(neighbor, path)
                path.pop()

    yield from dfs(start, [start])


def part1(input: dict[str, set[str]]) -> int:
    def get_neighbors(graph, node):
        return graph.get(node, [])

    return sum(1 for _ in find_all_paths(input, "you", "out", get_neighbors))


def part2(input: dict[str, set[str]]) -> int:
    def get_neighbors(graph, node):
        return graph.get(node, [])

    return sum(1 for _ in find_all_paths(input, "fft", "out", get_neighbors))


if __name__ == "__main__":
    print(part1(read_input("day11_test1.txt")))
    print(part1(read_input("day11_input.txt")))

    print(part2(read_input("day11_test2.txt")))
    print(part2(read_input("day11_input.txt")))
