#!/usr/bin/env python3


def parse_line(line):
    c = line.split(" ", 1)
    i = [c[0]] + c[1].split(", ")
    if i[0] in ("jio", "jie"):
        i[2] = int(i[2])
    if i[0] == "jmp":
        i[1] = int(i[1])
    return i

def load_input(path):
    return [parse_line(line.strip()) for line in open(path).readlines()]

def run(instructions, registers):
    pc = 0
    while True:
        if pc > (len(instructions) - 1):
            break
        match instructions[pc]:
            case ["jio", str(r), int(n)]:
                if registers[r] == 1:
                    pc += n
                else:
                    pc += 1
            case ["jie", str(r), int(n)]:
                if (registers[r] & 1) == 0:
                    pc += n
                else:
                    pc += 1
            case ["inc", str(r)]:
                registers[r] += 1
                pc += 1
            case ["tpl", str(r)]:
                registers[r] *= 3
                pc += 1
            case ["jmp", int(n)]:
                pc += n
            case ["hlf", str(r)]:
                registers[r] >>= 1
                pc += 1
            case _:
                raise Exception(f"Invalid instruction {i}")


def main():
    instructions = load_input("day23.input")

    # Part 1

    registers = {"a": 0, "b": 0}
    run(instructions, registers)
    print("Part one:", registers["b"])

    registers = {"a": 1, "b": 0}
    run(instructions, registers)
    print("Part two:", registers["b"])


if __name__ == "__main__":
    main()

