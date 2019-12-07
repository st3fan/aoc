#!/usr/bin/env python3

import fileinput

index = {"COM": None}

def count_orbits(object_name):
    total = 0
    while object_name:
        total += 1
        object_name = index.get(object_name)
    return total

if __name__ == "__main__":
    for line in fileinput.input():
        parent_name, object_name = line.strip().split(")")
        index[object_name] = parent_name
    print(sum([count_orbits(node) for node in index.values()]))
