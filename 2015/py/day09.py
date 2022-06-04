#!/usr/bin/env python3


from itertools import permutations, tee


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


if __name__ == "__main__":

    # Setup

    cities = set()
    distances = {}

    for line in [line.strip() for line in open("day09.input").readlines()]:
        c = line.split()
        cities.add(c[0])
        cities.add(c[2])
        distances[(c[0], c[2])] = int(c[4])
        distances[(c[2], c[0])] = int(c[4])

    min_distance = 9999999999
    max_distance = 0

    for trip in permutations(cities):
        distance = sum(distances[(a,b)] for a,b in pairwise(trip))
        min_distance = min(min_distance, distance)
        max_distance = max(max_distance, distance)

    print("Part one:", min_distance)
    print("Part two:", max_distance)

