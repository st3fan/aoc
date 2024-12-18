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
                    print("UNKNOWN INSTRUCTION", self.code[self.pc])

            if self.debug:
                print("  =>", f"a={self.a} b={self.b} c={self.c} output={self.output}")

        return False


# 0o3, [0o2, 0o1, 0o0] => 0o3210
def _build_a(i: int, inputs: list[int]) -> int:
    t = i
    for v in inputs:
        if v > 7:
            raise Exception(f"Invalid v: {v}")
        t <<= 3
        t |= v
    return t


def part2() -> int:
    # We compare the code from left to right
    CODE = [2, 4, 1, 3, 7, 5, 0, 3, 4, 1, 1, 5, 5, 5, 3, 0]

    # The inputs are in "A order" - so rightmost bits are CODE[0]
    def crack(inputs: list[int]):
        print("CRACK:", inputs)

        # We found a solution
        if len(inputs) == len(CODE):
            # print("FOUND CODE", inputs)  # Should push into queue or simply turn into A and MIN with other results for final answer
            return

        # We are going to loop over all 3 bit possibilities.

        for i in range(1, 8):
            # Run the code
            a = _build_a(i, inputs)
            cpu = CPU(code=[2, 4, 1, 3, 7, 5, 0, 3, 4, 1, 1, 5, 5, 5, 3, 0], a=a)
            cpu.run()

            print("I", i, "A", oct(a), "OUTPUT", cpu.output)

            # # The output length should be equal to the current length of the inputs plus one extra. This fails with leading zeros.
            # if len(cpu.output) != len(inputs) + 1:
            #     print("CPU.OUTPUT", cpu.output)
            #     print("INPUTS", inputs)
            #     raise Exception(f"len(cpu.output) != len(inputs)+1: {len(cpu.output)} != {len(inputs)+1}")

            # print("OUTPUT:", cpu.output, "CODE:", CODE)

            # If the CPU output (which length should match input) is the same as the code then recursively try the next digit

            if cpu.output == CODE[: len(cpu.output)]:
                # print(f"We found a match at {i}, going into this one")
                inputs = [i] + inputs  # Inputs grow to the left. New list, no copy needed?
                crack(inputs)

    crack([])

    return 0


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

    # #
    # # 2 4 BST
    # # 1 3 BXL
    # # 7 5 CDV
    # # 0 3 ADV
    # # 4 1 BXC
    # # 1 5 BXL
    # # 5 5 OUT
    # # 3 0 JNZ
    # #
    # # CODE:
    # #
    # # A = 45483412
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

    # #
    # # To get 16 results we need A to start at 8*16 = 281474976710656
    # #

    # CODE = [2, 4, 1, 3, 7, 5, 0, 3, 4, 1, 1, 5, 5, 5, 3, 0]

    # def truncate(l):
    #     if len(l) > 16:
    #         return l[:16] + ["..."]
    #     return l

    # # a = 35184372088832
    # # for a in range(35184372088832, 35184372088832 + 1_000_000):
    # #     cpu = CPU(code=CODE, a=a)
    # #     cpu.run()
    # #     print(a, "=>", cpu.output)

    # for n in range(35184372088832, 35184372088832 * 2):
    #     a = n
    #     cpu = CPU(code=CODE, a=a)
    #     cpu.run()
    #     print(a, "=>", cpu.output, cpu.a, cpu.b, cpu.c)

    # # Without recursion

    # part2()
