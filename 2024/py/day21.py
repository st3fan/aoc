#!/usr/bin/env python

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


def num_movements(g: nx.DiGraph, src: str, dst: str) -> list[str]:
    moves = []
    for a, b in pairwise(nx.shortest_path(g, source=src, target=dst)):
        moves.append(g.get_edge_data(a, b)["move"])
    return sorted(moves, reverse=src == "A")  # Seems to take the most efficient path?


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


def dir_movements(g: nx.DiGraph, src: str, dst: str) -> list[str]:
    moves = []
    for a, b in pairwise(nx.shortest_path(g, source=src, target=dst)):
        moves.append(g.get_edge_data(a, b)["move"])
    return moves


#


def part1(codes: list[str]) -> int:
    num_move_graph = build_numeric_keypad_graph()
    dir_move_graph = build_directional_keypad_graph()

    t = 0

    for code in codes:
        moves1 = []
        for a, b in pairwise("A" + code):
            moves1 += num_movements(num_move_graph, a, b)
            moves1.append("A")
        # print("".join(moves1) + f" {len(moves1)}")

        moves2 = []
        for a, b in pairwise(["A"] + moves1):
            moves2 += dir_movements(dir_move_graph, a, b)
            moves2.append("A")
        # print("".join(moves2) + f" {len(moves2)}")

        moves3 = []
        for a, b in pairwise(["A"] + moves2):
            moves3 += dir_movements(dir_move_graph, a, b)
            moves3.append("A")
        # print("".join(moves3) + f" {len(moves3)}")

        print(code + ": " + "".join(moves3) + f" ({len(moves3)})")

        t += len(moves3) * int(code[:-1])

    return t


if __name__ == "__main__":
    print("Test1", part1(["029A", "980A", "179A", "456A", "379A"]), "Should be 126384")
    print("Part1", part1(["879A", "508A", "463A", "593A", "189A"]), "Should not be 198336")
