#!/usr/bin/env python3


from dataclasses import dataclass
from aoc import empty, same


@dataclass
class Program:
    name: str
    weight: int
    subprograms: []


def parse_program(line):
    c = line.split()
    c[1] = int(c[1][1:-1])
    subprograms = [s.strip(",") for s in c[3:]]
    return Program(c[0], c[1], subprograms)
    

def read_input():
    with open("day07.input") as f:
        return [parse_program(line) for line in f.readlines()]


if __name__ == "__main__":

    programs_by_name = {}

    for program in read_input():
        programs_by_name[program.name] = program

    for program in programs_by_name.values():
        program.subprograms = [programs_by_name[name] for name in program.subprograms]

    # Part 1

    all_program_names = set(programs_by_name.keys())

    sub_program_names = set()
    for program in programs_by_name.values():
        sub_program_names.update([sp.name for sp in program.subprograms])

    root_name = list(all_program_names - sub_program_names)[0]

    print("Part one:", root_name)

    # Part 2

    def weight(program):
        return program.weight + sum([weight(p) for p in program.subprograms])

    def find_by_name(node):
        return node.name == "tdxow"

    def find_by_incorrect_weights(node):
        weights = [weight(p) for p in program.subprograms]
        return not empty(weights) and not same(weights)

    def print_name(node):
        print(node.name)

    def check(program):
        weights = [weight(p) for p in program.subprograms]
        if not empty(weights) and not same(weights):
            print(f"Program {program.name} {program.weight} does not have the same weights: {weights}")
            print("Part two:", program.subprograms[2].weight-8)

    def find(node, fn):
        if fn(node):
            return node
        for child in node.subprograms:
            if n := find(child, fn):
                return n


    root_node = programs_by_name[root_name]
    find(root_node, check)


    #for program in programs_by_name.values():
    #    weights = [weight(p) for p in program.subprograms]
    #    if not empty(weights) and not same(weights):
    #        print(f"Program {program.name} does not have the same weights: {weights}")

