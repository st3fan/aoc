#!/usr/bin/env python3


import sys
from collections import defaultdict


if __name__ == "__main__":

    # Setup

    instructions = []
    for line in [line.strip() for line in open("day18.input").readlines()]:
        c = line.split()
        for i,v in enumerate(c):
            try:
                c[i] = int(v)
            except:
                pass
        instructions.append(c)

    # Part 1

    pc = 0
    last_snd = 0
    registers = defaultdict(int)

    while pc >= 0 and pc < len(instructions):
        match instructions[pc]:
            case ["snd", int(x)]:
                last_snd = x
                pc += 1
            case ["snd", str(x)]:
                last_snd = registers[x]
                pc += 1
            case ["set", str(x), int(y)]:
                registers[x] = y
                pc += 1
            case ["set", str(x), str(y)]:
                registers[x] = registers[y]
                pc += 1
            case ["add", str(x), int(y)]:
                registers[x] += y
                pc += 1
            case ["add", str(x), str(y)]:
                registers[x] += registers[y]
                pc += 1
            case ["mul", str(x), int(y)]:
                registers[x] *= y
                pc += 1
            case ["mod", str(x), int(y)]:
                registers[x] = registers[x] % y
                pc += 1
            case ["mod", str(x), str(y)]:
                registers[x] = registers[x] % registers[y]
                pc += 1
            case ["rcv", str(x)]:
                if registers[x] != 0:
                    break
                pc += 1
            case ["jgz", str(x), int(y)]:
                if registers[x] > 0:
                    pc += y 
                else:
                    pc += 1
            case ["jgz", str(x), str(y)]:
                if registers[x] > 0:
                    pc += registers[y]
                else:
                    pc += 1
            case ["jgz", int(x), int(y)]:
                if x > 0:
                    pc += y
                else:
                    pc += 1
            case ["jgz", int(x), str(y)]:
                if x > 0:
                    pc += registers[y]
                else:
                    pc += 1
            case _:
                print("Invalid instruction:", instructions[pc])
                sys.exit(1)

    print("Part one:", last_snd)



