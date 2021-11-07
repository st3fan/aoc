#!/usr/bin/env python3


class Coprocessor:

    def __init__(self, instructions):
        self.instructions = instructions
        self.registers = {r: 0 for r in "abcdefgh"}
        self.pc = 0
        self.muls = 0

    def run(self):
        while self.pc >= 0 and self.pc < len(self.instructions):
            print("Executing", self.pc, self.instructions[self.pc])
            match self.instructions[self.pc]:
                case ["set", str(x), int(y)]:
                    self.registers[x] = y
                    self.pc += 1
                case ["set", str(x), str(y)]:
                    self.registers[x] = self.registers[y]
                    self.pc += 1
                case ["sub", str(x), int(y)]:
                    self.registers[x] -= y
                    self.pc += 1
                case ["sub", str(x), str(y)]:
                    self.registers[x] -= self.registers[y]
                    self.pc += 1
                case ["mul", str(x), int(y)]:
                    self.registers[x] *= y
                    self.pc += 1
                    self.muls += 1
                case ["mul", str(x), str(y)]:
                    self.registers[x] *= self.registers[y]
                    self.pc += 1
                    self.muls += 1
                case ["jnz", str(x), int(y)]:
                    if self.registers[x] != 0:
                        self.pc += y 
                    else:
                        self.pc += 1
                case ["jnz", str(x), str(y)]:
                    if self.registers[x] != 0:
                        self.pc += self.registers[y]
                    else:
                        self.pc += 1
                case ["jnz", int(x), int(y)]:
                    if x != 0:
                        self.pc += y
                    else:
                        self.pc += 1
                case ["jnz", int(x), str(y)]:
                    if x != 0:
                        self.pc += self.registers[y]
                    else:
                        self.pc += 1
                case _:
                    raise Exception(f"Invalid instruction: {self.instructions[self.pc]}")



if __name__ == "__main__":

    # Setup

    instructions = []
    for line in [line.strip() for line in open("day23.input").readlines()]:
        c = line.split()
        for i,v in enumerate(c):
            try:
                c[i] = int(v)
            except:
                pass
        instructions.append(c)

    # Part 1

    c = Coprocessor(instructions)
    c.run()

    print("Part one:", c.muls)

    # Part 2

    c = Coprocessor(instructions)
    c.registers["a"] = 1
    c.run()

    print("Part two:", c.registers["h"])
