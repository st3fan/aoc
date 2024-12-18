#!/usr/bin/env python

from enum import IntEnum
from math import trunc


class Opcode(IntEnum):
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7


class CPU:
    # code: list[tuple[int, int]]
    # a: int
    # b: int
    # c: int
    # pc: int = 0
    # output: list[int] = []

    def __init__(self, *, code: list[int], a: int = 0, b: int = 0, c: int = 0, debug: bool = False):
        self.code = [(code[i * 2], code[i * 2 + 1]) for i in range(len(code) // 2)]
        self.a = a
        self.b = b
        self.c = c
        self.debug = debug
        self.pc = 0
        self.output = []

    def _combo_operand(self, operand) -> int:
        match operand:
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c
            case v if v < 4:
                return v
            case _:
                raise Exception(f"Invalid operand value: {operand}")

    def run(self):
        while self.pc < len(self.code):
            if self.debug:
                print("EXECUTING", self.pc, "=>", self.code[self.pc])
            match self.code[self.pc]:
                case (Opcode.ADV, operand):
                    self.a = int(trunc(self.a // (2 ** self._combo_operand(operand))))
                    self.pc += 1
                case (Opcode.BXL, operand):
                    self.b ^= operand
                    self.pc += 1
                case (Opcode.BST, operand):
                    self.b = self._combo_operand(operand) % 8
                    self.pc += 1
                case (Opcode.JNZ, operand):
                    if self.a == 0:
                        self.pc += 1
                    else:
                        self.pc = operand
                case (Opcode.BXC, _operand):
                    self.b ^= self.c
                    self.pc += 1
                case (Opcode.OUT, operand):
                    self.output.append(self._combo_operand(operand) % 8)
                    # if self.output[0] == 2:
                    #     return True
                    self.pc += 1
                case (Opcode.BDV, operand):
                    self.b = int(trunc(self.a // (2 ** self._combo_operand(operand))))
                    self.pc += 1
                case (Opcode.CDV, operand):
                    self.c = int(trunc(self.a // (2 ** self._combo_operand(operand))))
                    self.pc += 1
                case _:
                    print("UNKNOWN INSTRUCTION", self.code[self.pc])  #

            if self.debug:
                print("  =>", f"a={self.a} b={self.b} c={self.c} output={self.output}")

        return False


# [0o0, 0o1, 0o2], 0o3 => 0o0123...padding (length(n))
def _build_a(inputs: list[int], i, length: int) -> int:
    a = 0
    for v in inputs:
        a <<= 3
        a |= v
    a <<= 3
    a |= i
    # Pad right
    for _ in range(length - len(inputs) - 1):
        a <<= 3
        a |= 1  # The padding doesn't seem to make a difference
    # print("BUILD_A", inputs, i, length, "=>", oct(a))
    return a


def part2() -> int:
    # We compare the code from right to left
    CODE = [2, 4, 1, 3, 7, 5, 0, 3, 4, 1, 1, 5, 5, 5, 3, 0]

    # The inputs are in "A order" - so rightmost bits are CODE[0]
    def crack(inputs: list[int]):
        print("\n\nCRACK:", inputs)

        # # We found a solution This should be below?
        # if len(inputs) == len(CODE):
        #     print("FOUND CODE", inputs)  # Should push into queue or simply turn into A and MIN with other results for final answer
        #     return

        for i in range(8):  # range(8): reverse?
            # Run the code
            a = _build_a(inputs, i, len(CODE))
            cpu = CPU(code=[2, 4, 1, 3, 7, 5, 0, 3, 4, 1, 1, 5, 5, 5, 3, 0], a=a)
            cpu.run()

            print("INPUTS", inputs, "I", i, "A", oct(a), "OUTPUT", cpu.output, "LEN(INPUTS)+1", len(inputs) + 1)

            # # The output length should be equal to the current length of the inputs plus one extra. This fails with leading zeros.
            # if len(cpu.output) != len(inputs) + 1:
            #     print("CPU.OUTPUT", cpu.output)
            #     print("INPUTS", inputs)
            #     raise Exception(f"len(cpu.output) != len(inputs)+1: {len(cpu.output)} != {len(inputs)+1}")

            # print("OUTPUT:", cpu.output, "CODE:", CODE)

            # If the CPU output is the same as the code for N from the right then we are on the right track

            n = len(inputs) + 1  # This is how many outputs to compare from the right side (plus one because we have not added the one just found)

            # print("COMPARING", n, "OUT", cpu.output, "CODE", CODE)

            if cpu.output[-n:] == CODE[-n:]:
                # inputs =   # Inputs grow to the right. Not sure if we need the copy.
                crack(inputs.copy() + [i])

            # NOPE
            # n = len(inputs) + 1  # This is how much to compare from the right
            # if cpu.output[-n] == CODE[-n]:
            #     inputs = inputs.copy() + [i]  # Inputs grow to the right. Not sure if we need the copy.
            #     crack(inputs)

    crack([])

    return 0


# #
# # DO {
# #     B = A % 8           # 0: BST A
# #     B = B ^ 3           # 1: BXL 3
# #     C = A / (2 ** B)    # 2: CDV B
# #     A = A / (2 ** 3)    # 3: ADV 3
# #     B = B ^ C           # 4: BXC
# #     B = B ^ 5           # 5: BXL 5
# #     OUT B               # 6: OUT 5
# # } WHILE A != 0          # 7: JNZ 0
# #

if __name__ == "__main__":
    # cpu = CPU(code=[0, 1, 5, 4, 3, 0], a=729, b=0, c=0)
    # cpu = CPU(code=[2, 6], c=9)
    # cpu = CPU(code=[5, 0, 5, 1, 5, 4], a=10)
    # cpu = CPU(code=[0, 1, 5, 4, 3, 0], a=2024)
    # cpu = CPU(code=[4, 0], b=2024, c=43690)
    # cpu.run()

    # cpu = CPU(code=[0, 1, 5, 4, 3, 0], a=729)
    # cpu.run()
    # print("Part1:", "".join(str(v) for v in cpu.output))

    # Part 1
    cpu = CPU(code=[2, 4, 1, 3, 7, 5, 0, 3, 4, 1, 1, 5, 5, 5, 3, 0], a=45483412)
    cpu.run()
    print("Part1:", ",".join(str(v) for v in cpu.output))
    print("Part2:", part2())

    # # Part 2

    print(oct(45483412))

    cpu = CPU(code=[2, 4, 1, 3, 7, 5, 0, 3, 4, 1, 1, 5, 5, 5, 3, 0], a=0o200000000)
    cpu.run()
    print("A", cpu.output)

    cpu = CPU(code=[2, 4, 1, 3, 7, 5, 0, 3, 4, 1, 1, 5, 5, 5, 3, 0], a=0o250000000)
    cpu.run()
    print("B", cpu.output)

    cpu = CPU(code=[2, 4, 1, 3, 7, 5, 0, 3, 4, 1, 1, 5, 5, 5, 3, 0], a=0o255000000)
    cpu.run()
    print("C", cpu.output)

    cpu = CPU(code=[2, 4, 1, 3, 7, 5, 0, 3, 4, 1, 1, 5, 5, 5, 3, 0], a=0o255400000)
    cpu.run()
    print("D", cpu.output)

    cpu = CPU(code=[2, 4, 1, 3, 7, 5, 0, 3, 4, 1, 1, 5, 5, 5, 3, 0], a=211106232532992)
    cpu.run()
    print("JA?", cpu.output)
