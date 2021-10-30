#!/usr/bin/env python


from collections import defaultdict


def parse_program(line):
    c = line.split()
    c[2] = int(c[2])
    c[6] = int(c[6])
    return c
    

def read_input():
    with open("day08.input") as f:
        return [parse_program(line) for line in f.readlines()]


if __name__ == "__main__":

    instructions = read_input()

    # Part one

    registers = defaultdict(int)
    highest = 0

    def incdec(reg, op, val):
        match op:
            case "inc":
                registers[reg] += val
            case "dec":
                registers[reg] -= val

    for instruction in instructions:
        match instruction:
            case [reg, ("inc" | "dec") as op, val, "if", cmpreg, "<", cmpval]:
                if registers[cmpreg] < cmpval:
                    incdec(reg, op, val)
            case [reg, ("inc" | "dec") as op, val, "if", cmpreg, ">", cmpval]:
                if registers[cmpreg] > cmpval:
                    incdec(reg, op, val)
            case [reg, ("inc" | "dec") as op, val, "if", cmpreg, "<=", cmpval]:
                if registers[cmpreg] <= cmpval:
                    incdec(reg, op, val)
            case [reg, ("inc" | "dec") as op, val, "if", cmpreg, ">=", cmpval]:
                if registers[cmpreg] >= cmpval:
                    incdec(reg, op, val)
            case [reg, ("inc" | "dec") as op, val, "if", cmpreg, "==", cmpval]:
                if registers[cmpreg] == cmpval:
                    incdec(reg, op, val)
            case [reg, ("inc" | "dec") as op, val, "if", cmpreg, "!=", cmpval]:
                if registers[cmpreg] != cmpval:
                    incdec(reg, op, val)
        if registers[reg] > highest:
            highest = registers[reg]

    print("Part one:", max(registers.values()))

    # Part two

    print("Part two:", highest)

