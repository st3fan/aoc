#!/usr/bin/env python3


from aoc import InfiniteGrid, Position, Santa


def main():
    moves = open("day03.input").read().strip()

    # Part 1

    grid = InfiniteGrid()
    santa = Santa()

    grid.set(Position(0,0), True)

    for move in moves:
        match move:
            case "<":
                santa.west()
            case ">":
                santa.east()
            case "^":
                santa.north()
            case "v":
                santa.south()
        grid.set(santa.position, True)

    print("Part one:", len(grid.nodes))

    # Part 2

    grid = InfiniteGrid()
    movers = [Santa(), Santa()]

    grid.set(Position(0,0), True)

    for i, move in enumerate(moves):
        m = movers[i & 1]
        match move:
            case "<":
                m.west()
            case ">":
                m.east()
            case "^":
                m.north()
            case "v":
                m.south()
        grid.set(m.position, True)

    print("Part two:", len(grid.nodes))


if __name__ == "__main__":
    main()
