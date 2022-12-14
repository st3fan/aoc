#!/usr/bin/env python


from typing import Dict, Generator, List, Tuple, cast
from aoc import Grid, Position


def read_input() -> Tuple[Grid[int], Position, Position]:
    grid = Grid.from_file("day12.txt", lambda v: v)
    start_position = cast(Position, grid.find("S"))
    end_position = cast(Position, grid.find("E"))

    def _transform(v: str) -> int:
        match v:
            case "S":
                return ord("a")
            case "E":
                return ord("z")
            case _:
                return ord(v)

    return (Grid.from_file("day12.txt", _transform), start_position, end_position)


def _can_move(grid: Grid[int], src_position: Position, dst_position: Position) -> bool:
    src: int = grid.get(src_position)
    dst: int = grid.get(dst_position)
    return dst <= src or (dst > src and ((dst - src) == 1))


def bfs(grid: Grid[int], start_position: Position, end_position: Position) -> List[Position]:
    queue: List[Position] = []
    visited: Dict[Position, Position | None] = {start_position: None}

    current = start_position
    while current != end_position:
        for neighbour in grid.neighbours(current):
            if neighbour not in visited:
                if _can_move(grid, current, neighbour):
                    visited[neighbour] = current
                    queue.append(neighbour)
        if len(queue) == 0:
            return []
        current = queue.pop(0)

    path: List[Position] = [current]

    while current != start_position:
        current = visited[current]
        path.insert(0, current)

    return path


def part1() -> int:
    grid, start_position, end_position = read_input()
    return len(bfs(grid, start_position, end_position)) - 1


def _lowest_positions(grid: Grid[int]) -> Generator[Position, None, None]:
    for y in range(grid.height):
        for x in range(grid.width):
            p = Position(x, y)
            if grid.get(p) == ord("a"):
                yield p


def part2() -> int:
    grid, _, end_position = read_input()
    return min([len(path) for path in [bfs(grid, p, end_position) for p in _lowest_positions(grid)] if path]) - 1


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
