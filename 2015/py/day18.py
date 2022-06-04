#!/usr/bin/env python3


from aoc import Grid, Position


def main():

    # Part 1

    grid = Grid.from_file("day18.input")
    for _ in range(100):
        copy = grid.copy()
        for y in range(grid.height):
            for x in range(grid.width):
                p = Position(x, y)
                neighbours = [n for n in copy.neighbours(p) if copy.get(n) == '#']
                match grid.get(p):
                    case '#':
                        if len(neighbours) != 2 and len(neighbours) != 3:
                            grid.set(p, '.')
                    case '.':
                        if len(neighbours) == 3:
                            grid.set(p, '#')
    print("Part one:", grid.count('#'))

    # Part 2


    grid = Grid.from_file("day18.input")

    stuck = [Position(0, 0), Position(99, 0), Position(0, 99), Position(99, 99)]
    for p in stuck:
        grid.set(p, '#')

    for _ in range(100):
        copy = grid.copy()
        for y in range(grid.height):
            for x in range(grid.width):
                p = Position(x, y)
                neighbours = [n for n in copy.neighbours(p) if copy.get(n) == '#']
                match grid.get(p):
                    case '#':
                        if len(neighbours) != 2 and len(neighbours) != 3:
                            if p not in stuck:
                                grid.set(p, '.')
                    case '.':
                        if len(neighbours) == 3:
                            grid.set(p, '#')
    print("Part two:", grid.count('#'))

if __name__ == "__main__":
    main()
