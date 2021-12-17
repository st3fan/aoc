#!/usr/bin/env python3


def in_target_area(p, xs, xe, ys, ye):
    return xe >= p[0] >= xs and ye >= p[1] >= ys


def create_probe(vx, vy):
    x, y = 0, 0
    while True:
        yield (x, y)
        x += vx
        y += vy
        if vx != 0:
            if vx > 0:
                vx -= 1
            else:
                vx += 1
        vy -= 1


def part1():

    #xs = 20
    #xe = 30
    #ys = -10
    #ye = -5

    xs = 207
    xe = 263
    ys = -115
    ye = -63

    result = 0
    for vx in range(263):
        for vy in range(1000):
            max_y = 0
            for i, p in enumerate(create_probe(vx, vy)):
                max_y = max(max_y, p[1])
                if p[1] < ys:
                    break
                if in_target_area(p, xs, xe, ys, ye):
                    result = max(result, max_y)
                    break
    return result


def part2():

    #xs = 20
    #xe = 30
    #ys = -10
    #ye = -5

    xs = 207
    xe = 263
    ys = -115
    ye = -63

    result = set()
    for vx in range(-1000, 1000):
        for vy in range(-1000, 1000):
            for p in create_probe(vx, vy):
                if p[1] < ys or p[0] > xe:
                    break
                if in_target_area(p, xs, xe, ys, ye):
                    result.add((vx,vy))
                    break
    return len(result)


if __name__ == "__main__":
    print("Part one:", part1())
    print("Part two:", part2())
