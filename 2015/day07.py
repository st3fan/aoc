#!/usr/bin/env python3


def parse_int(s):
    if s.isdecimal():
        return int(s)
    return s


def execute(instruction, registers):
    match instruction:
        case [str(a), "RSHIFT", int(b), "->", str(dst)]:
            if a in registers:
                registers[dst] = (registers[a] >> b) & 0xffff
                return True
        case [str(a), "LSHIFT", int(b), "->", str(dst)]:
            if a in registers:
                registers[dst] = (registers[a] << b) & 0xffff
                return True
        case [int(a), "AND", str(b), "->", str(dst)]:
            if b in registers:
                registers[dst] = (a & registers[b]) & 0xffff
                return True
        case [str(a), "AND", str(b), "->", str(dst)]:
            if a in registers and b in registers:
                registers[dst] = (registers[a] & registers[b]) & 0xffff
                return True
        case [int(a), "OR", str(b), "->", str(dst)]:
            if b in registers:
                registers[dst] = (a & registers[b]) | 0xffff
                return True
        case [str(a), "OR", str(b), "->", str(dst)]:
            if a in registers and b in registers:
                registers[dst] = (registers[a] | registers[b]) & 0xffff
                return True
        case [str(a), "->", str(dst)]:
            if a in registers:
                registers[dst] = registers[a]
                return True
        case [int(a), "->", str(dst)]:
            if dst not in registers:
                registers[dst] = a
            return True
        case ["NOT", str(a), "->", str(dst)]:
            if a in registers:
                registers[dst] = (~registers[a]) & 0xffff
                return True
        case _:
            raise Exception(f"Unexpected input: {line}")


def main():

    #
    # Part 1 - We could build a tree of instructions and their dependencies but it
    # is much simpler to just loop through all the instructions, executing only
    # those for which we have enough data. After enough iterations we will have
    # executed all instructions.
    #

    registers = {}
    instructions = set()

    for line in (line.strip() for line in open("day07.input").readlines()):
        instructions.add(tuple([parse_int(e) for e in line.split()]))

    while len(instructions):
        for i in set(instructions):
            if execute(i, registers):
                instructions.remove(i)

    print("Part one:", registers["a"])

    #
    # Part 2 - We do the same thing except we just initialize the registers.
    # Also modified execute() a bit to ignore instructions that set a register
    # twice.
    #

    registers = {"b": registers["a"]}
    instructions = set()

    for line in (line.strip() for line in open("day07.input").readlines()):
        instructions.add(tuple([parse_int(e) for e in line.split()]))

    while len(instructions):
        for i in set(instructions):
            if execute(i, registers):
                instructions.remove(i)

    print("Part two:", registers["a"])

if __name__ == "__main__":
    main()

