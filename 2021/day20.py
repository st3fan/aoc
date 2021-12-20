#!/usr/bin/env python3


from aoc import Grid, Position


def load_image():
    def _bit(v):
        if v == ".":
            return "0"
        else:
            return "1"
    return Grid.from_file("day20.image", _bit)


def load_algorithm():
    return open("day20.algorithm").read().strip().replace(".", "0").replace("#", "1")


def lookup(grid, p, algorithm, step):
    bits = ""
    positions = [(-1,-1), (0,-1), (1,-1), (-1,0), (0,0), (1,0), (-1,1), (0,1), (1,1)]
    for xo, yo in positions:
        px = p.x + xo
        py = p.y + yo
        if px >= 0 and px < grid.width and py >= 0 and py < grid.height:
            bits += grid.get(Position(px, py))
        else:
            if step % 2 == 0:
                bits += "0"
            else:
                bits += "1"
    i = int(bits, 2)
    return algorithm[i]


def part(steps):
    img = load_image()
    alg = load_algorithm()

    max_width = img.width + (steps*2)
    max_height = img.height + (steps*2)
    src = Grid(max_width, max_height, "0")

    for y in range(img.height):
        for x in range(img.width):
            imgp = Position(x, y)
            srcp = Position(x+(max_width-img.width)//2, y+(max_height-img.height)//2)
            src.set(srcp, img.get(imgp))
            
    for step in range(steps):
        dst = Grid(max_width, max_height, "0")
        for y in range(src.height):
            for x in range(src.width):
                p = Position(x, y)
                dst.set(p, lookup(src, p, alg, step))
        src = dst

    return src.count("1")


if __name__ == "__main__":
    print("Part one:", part(2))
    print("Part two:", part(50))

