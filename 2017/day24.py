#!/usr/bin/env python3


def read_input(path):
    return set([tuple(sorted([int(e) for e in line.strip().split("/")])) for line in open(path).readlines()])


def find_matching_plugs(start_plug, plugs):
    matching = set()
    for p in plugs:
        if p[0] == start_plug[1] or p[1] == start_plug[1]:
            if p not in matching:
                matching.add(p)
    return matching


def find_matching_plug(start_plug, plugs):
    for p in plugs:
        if p[0] == start_plug[1] or p[1] == start_plug[1]:
            return p


def adjust_plug(n, plug):
    if n == plug[0]:
        return plug
    else:
        return (plug[1], plug[0])


def bridge_strength(bridge):
    return sum([p[0]+p[1] for p in bridge])


def bridges(plugs, bridge=[(0,0)]):
    yield bridge
    if matching_plugs := find_matching_plugs(bridge[-1], plugs):
        for plug in matching_plugs:
            yield from bridges(plugs - {plug}, bridge + [adjust_plug(bridge[-1][1], plug)])


def main():
    
    plugs = read_input("day24.input")

    # Part 1

    max_strength = max([bridge_strength(bridge) for bridge in bridges(plugs)]) 
    print("Part one:", max_strength)

    # Part 2

    max_length = 0
    max_strength = 0
    for bridge in bridges(plugs):
        if len(bridge) >= max_length:
            max_length = len(bridge)
            max_strength = max(max_strength, bridge_strength(bridge))
    print("Part two:", max_strength)


if __name__ == "__main__":
    main()

