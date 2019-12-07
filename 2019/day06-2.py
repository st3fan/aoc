#!/usr/bin/env python3

import fileinput

index = {"COM": None}

def path(start, end):
    path = []
    while index.get(start) != end:
        start = index.get(start)
        path.append(start)
    return path

def crossing(a, b):
    for node in you_path:
        if node in san_path:
            return node

if __name__ == "__main__":
    for line in fileinput.input():
        parent_name, object_name = line.strip().split(")")
        index[object_name] = parent_name

    san_path = path("SAN", "COM")
    you_path = path("YOU", "COM")
    x = crossing(you_path, san_path)
    print(san_path.index(x) + you_path.index(x))

