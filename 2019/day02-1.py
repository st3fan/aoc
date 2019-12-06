#!/usr/bin/env python3


import fileinput


INS_ADD = 1
INS_MULTIPLY = 2
INS_DONE = 99


class Computer:

    def __init__(self, data):
        self.memory = data
        self.pc = 0

    def _fetch(self):
        instruction = self.memory[self.pc]
        self.pc += 1
        return instruction

    def _add(self):
        a = self._fetch()
        b = self._fetch()
        d = self._fetch()
        self.memory[d] = self.memory[a] + self.memory[b]

    def _multiply(self):
        a = self._fetch()
        b = self._fetch()
        d = self._fetch()
        self.memory[d] = self.memory[a] * self.memory[b]

    def run(self):
        while True:
            instruction = self._fetch()
            if instruction == INS_ADD:
                self._add()
            elif instruction == INS_MULTIPLY:
                self._multiply()
            elif instruction == INS_DONE:
                break
            else:
                raise Exception("Invalid instruction")


if __name__ == "__main__":

    data = []
    for line in fileinput.input():
        line = line.strip()
        data = data + [int(v) for v in line.split(",")]

    computer = Computer(data)
    computer.memory[1] = 12
    computer.memory[2] = 2
    computer.run()
    print(computer.memory[0])

