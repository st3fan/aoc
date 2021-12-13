#!/usr/bin/env python3


from collections import defaultdict, Counter


def load():
    with open("day12.input") as fp:
        vertices = defaultdict(set)
        for line in fp.readlines():
            [a, b] = line.strip().split("-")
            vertices[a].add(b)
            vertices[b].add(a)
        return vertices


def is_small_cave(node):
    return node.islower()


def is_big_cave(node):
    return node.isupper()


def is_valid_path(path):
    seen = set()
    for node in path:
        if is_small_cave(node):
            if node in seen:
                return False
            else:
                seen.add(node)
    return True


# DFS Traversal with the only logic added being that small caves can
# be visited once while big caves many times.

START_NODE = "start"
END_NODE = "end"


def should_visit1(node, path):
    return is_big_cave(node) or node not in path

def find_all_paths1(vertices, node=START_NODE, path = []):
    path.append(node)
    if node == END_NODE:
        yield path
    else:
        for n in vertices[node]:
            if should_visit1(n, path):
                yield from find_all_paths1(vertices, n, path)
    path.pop()


def part1():
    return sum(1 for _ in find_all_paths1(load()))


def should_visit2(node, path):
    if node == "start":
        return False
    if is_big_cave(node):
        return True

    c = Counter([e for e in path if is_small_cave(e)])
    if c.most_common()[0][1] == 2:
        return path.count(node) == 0
    else:
        return True


def find_all_paths2(vertices, node=START_NODE, path = []):
    path.append(node)
    if node == END_NODE:
        yield path
    else:
        for n in vertices[node]:
            if should_visit2(n, path):
                yield from find_all_paths2(vertices, n, path)
    path.pop()


def part2():
    return sum(1 for _ in find_all_paths2(load()))


if __name__ == "__main__":
    print("Part one:", part1())
    print("Part two:", part2())
