#!/usr/bin/env python3


from aoc import Position, InfiniteGrid, Turtle


def main():

    # Part 1

    grid = InfiniteGrid.from_file("day22.input")
    turtle = Turtle(Position(grid.maxx() // 2, grid.maxy() // 2))

    infected = 0
    for _ in range(10_000):
        match grid.get(turtle.position):
            case '.':
                turtle.left()
                grid.set(turtle.position, '#')
                infected += 1
            case '#':
                turtle.right()
                grid.set(turtle.position, '.')
        turtle.forward()
        if not grid.get(turtle.position):
            grid.set(turtle.position, '.')

    print("Part one:", infected)

    # Part 2

    grid = InfiniteGrid.from_file("day22.input")
    turtle = Turtle(Position(grid.maxx() // 2, grid.maxy() // 2))

    infected = 0
    for _ in range(10_000_000):
        match grid.get(turtle.position):
            case '.':
                turtle.left()
                grid.set(turtle.position, 'W')
            case '#':
                turtle.right()
                grid.set(turtle.position, 'F')
            case 'W':
                grid.set(turtle.position, '#')
                infected += 1
            case 'F':
                turtle.right()
                turtle.right()
                grid.set(turtle.position, '.')
        turtle.forward()
        if not grid.get(turtle.position):
            grid.set(turtle.position, '.')

    print("Part two:", infected)


if __name__ == "__main__":
    main()

