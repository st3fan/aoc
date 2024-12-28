#!/usr/bin/env python

from functools import cache
from itertools import pairwise

import networkx as nx

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+


def build_numeric_keypad_graph() -> nx.DiGraph:
    g = nx.DiGraph()
    movements = {
        "A": [("0", "<"), ("3", "^")],
        "0": [("A", ">"), ("2", "^")],
        "1": [("2", ">"), ("4", "^")],
        "2": [("0", "v"), ("1", "<"), ("3", ">"), ("5", "^")],
        "3": [("A", "v"), ("2", "<"), ("6", "^")],
        "4": [("1", "v"), ("5", ">"), ("7", "^")],
        "5": [("2", "v"), ("4", "<"), ("6", ">"), ("8", "^")],
        "6": [("3", "v"), ("5", "<"), ("9", "^")],
        "7": [("4", "v"), ("8", ">")],
        "8": [("5", "v"), ("7", "<"), ("9", ">")],
        "9": [("6", "v"), ("8", "<")],
    }
    for src, dst in movements.items():
        for d in dst:
            g.add_edge(src, d[0], move=d[1])
    return g


#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+


def build_directional_keypad_graph() -> nx.DiGraph:
    g = nx.DiGraph()
    movements = {
        "A": [("^", "<"), (">", "v")],
        "<": [("v", ">")],
        ">": [("v", "<"), ("A", "^")],
        "^": [("A", ">"), ("v", "v")],
        "v": [("<", "<"), (">", ">"), ("^", "^")],
    }
    for src, dst in movements.items():
        for d in dst:
            g.add_edge(src, d[0], move=d[1])
    return g


NUM_GRAPH = build_numeric_keypad_graph()
DIR_GRAPH = build_directional_keypad_graph()


@cache  # Barely helps. But maybe more effective for part two.
def dir_movements(src: str, dst: str) -> list[str]:
    moves = []
    for a, b in pairwise(nx.shortest_path(DIR_GRAPH, source=src, target=dst)):
        moves.append(DIR_GRAPH.get_edge_data(a, b)["move"])
    return moves


def all_moves(g: nx.DiGraph, src: str, dst: str) -> list[list[str]]:
    all_moves = []
    for path in nx.all_shortest_paths(g, source=src, target=dst):
        moves = []
        for a, b in pairwise(path):
            moves.append(g.get_edge_data(a, b)["move"])
        all_moves.append(moves)
    return all_moves


#


def min_button_presses1(code: str, n: int) -> int:
    min_presses = 9999999999

    # LOL At least there are not so much for the numeric
    for num_path_1 in all_moves(NUM_GRAPH, "A", code[0]):
        for num_path_2 in all_moves(NUM_GRAPH, code[0], code[1]):
            for num_path_3 in all_moves(NUM_GRAPH, code[1], code[2]):
                for num_path_4 in all_moves(NUM_GRAPH, code[2], code[3]):
                    # We generate unique paths - this is what you would type in
                    path = num_path_1 + ["A"] + num_path_2 + ["A"] + num_path_3 + ["A"] + num_path_4 + ["A"]

                    def _foo(path):
                        new_path = []
                        for a, b in pairwise(["A"] + path):
                            new_path += dir_movements(a, b)
                            new_path.append("A")
                        return new_path

                    for _ in range(n):
                        path = _foo(path)

                    t = len(path)
                    if t < min_presses:
                        min_presses = t

    return min_presses


def min_button_presses2(code: str, n: int) -> int:
    return 0  # TODO TODO TODO TODO


def part1(codes: list[str]) -> int:
    return sum(min_button_presses1(code, 2) * int(code[:-1]) for code in codes)


def part2(codes: list[str]) -> int:
    return sum(min_button_presses2(code, 4) * int(code[:-1]) for code in codes)


if __name__ == "__main__":
    print("Test1", part1(["029A", "980A", "179A", "456A", "379A"]), "Should be 126384")
    print("Part1", part1(["879A", "508A", "463A", "593A", "189A"]), "Should be 188384")

    codes = ["879A", "508A", "463A", "593A", "189A"]
    print("Part2 Method1", sum(min_button_presses1(code, 8) * int(code[:-1]) for code in codes))
    print("Part2 Method2", sum(min_button_presses2(code, 8) * int(code[:-1]) for code in codes))
