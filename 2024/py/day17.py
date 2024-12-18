#!/usr/bin/env python

from enum import IntEnum
from math import trunc

# Too lazy to parse the input for this one
CODE = [2, 4, 1, 3, 7, 5, 0, 3, 4, 1, 1, 5, 5, 5, 3, 0]
A = 45483412


#
# DO {
#     B = A % 8           # 0: BST A
#     B = B ^ 3           # 1: BXL 3
#     C = A / (2 ** B)    # 2: CDV B
#     A = A / (2 ** 3)    # 3: ADV 3
#     B = B ^ C           # 4: BXC
#     B = B ^ 5           # 5: BXL 5
#     OUT B               # 6: OUT 5
# } WHILE A != 0          # 7: JNZ 0
#


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
    code: list[tuple[int, int]]
    a: int
    b: int
    c: int
    debug: bool
    pc: int = 0
    output: list[int] = []

    def __init__(self, *, code: list[int], a: int = 0, b: int = 0, c: int = 0, debug: bool = False):
        self.code = [(code[i * 2], code[i * 2 + 1]) for i in range(len(code) // 2)]
        self.a = a
        self.b = b
        self.c = c
        self.debug = debug

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
    # Padding
    for _ in range(length - len(inputs) - 1):
        a <<= 3
    return a


def part2(code: list[int]) -> int:
    solutions = []

    def crack(inputs: list[int]):
        for i in range(8):
            a = _build_a(inputs, i, len(code))
            cpu = CPU(code=code, a=a)
            cpu.run()
            n = len(inputs) + 1
            if cpu.output[-n:] == code[-n:]:
                if n == len(code):
                    solutions.append(a)
                else:
                    crack(inputs.copy() + [i])

    crack([])

    return min(solutions)


def part1(code: list[int], a: int = 0) -> str:
    cpu = CPU(code=code, a=a)
    cpu.run()
    return ",".join(str(v) for v in cpu.output)


if __name__ == "__main__":
    print("Part1:", part1(CODE, A))
    print("Part2:", part2(CODE))
