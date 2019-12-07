#!/usr/bin/env python3


from collections import deque
from itertools import permutations
import fileinput


INS_ADD           = 1
INS_MULTIPLY      = 2
INS_INPUT         = 3
INS_OUTPUT        = 4
INS_JUMP_IF_TRUE  = 5
INS_JUMP_IF_FALSE = 6
INS_LESS_THAN     = 7
INS_EQUALS        = 8
INS_DONE          = 99

MODE_IMMEDIATE = True
MODE_POSITION  = False


class InvalidInstructionException (Exception):
    def __init__(self, instruction):
        super().__init__("<%d>" % instruction)


class Computer:

    def __init__(self, data, inputs):
        self._memory = data.copy()
        self._pc = 0
        self._inputs = deque(inputs)

    def input(self, value):
        self._inputs.append(value)
        
    def _parse_modes(self, instruction):
        i = "%.5d" % instruction
        return (i[2] == "1", i[1] == "1", i[0] == "1")
        
    def _fetch(self):
        instruction = self._memory[self._pc]
        self._pc += 1
        if instruction > 100:
            return instruction % 100, self._parse_modes(instruction)
        else:
            return instruction, (MODE_POSITION, MODE_POSITION, MODE_POSITION)

    def _pop(self):
        v = self._memory[self._pc]
        self._pc += 1
        return v
        
    def _load(self, position, mode):
        if mode == MODE_IMMEDIATE:
            return position
        else:
            return self._memory[position]

    def _store(self, position, value):
        self._memory[position] = value
        
    def _add(self, modes):
        a = self._pop()
        b = self._pop()
        d = self._pop()
        self._store(d, self._load(a, modes[0]) + self._load(b, modes[1]))

    def _multiply(self, modes):
        a = self._pop()
        b = self._pop()
        d = self._pop()
        self._store(d, self._load(a, modes[0]) * self._load(b, modes[1]))

    def _input(self):
        self._store(self._pop(), self._inputs.popleft())

    def _output(self, modes):
        #self._outputs.append(self._load(self._pop(), modes[0]))
        v = self._pop()
        return self._load(v, modes[0])

    def _jump_if_true(self, modes):
        if self._load(self._pop(), modes[0]) != 0:
            self._pc = self._load(self._pop(), modes[1])
        else:
            self._pop()

    def _jump_if_false(self, modes):
        if self._load(self._pop(), modes[0]) == 0:
            self._pc = self._load(self._pop(), modes[1])
        else:
            self._pop()

    def _less_than(self, modes):
        if self._load(self._pop(), modes[0]) < self._load(self._pop(), modes[1]):
            self._store(self._pop(), 1)
        else:
            self._store(self._pop(), 0)

    def _equals(self, modes):
        if self._load(self._pop(), modes[0]) == self._load(self._pop(), modes[1]):
            self._store(self._pop(), 1)
        else:
            self._store(self._pop(), 0)
            
    def run(self):
        while True:
            instruction, modes = self._fetch()
            if instruction == INS_ADD:
                self._add(modes)
            elif instruction == INS_MULTIPLY:
                self._multiply(modes)
            elif instruction == INS_INPUT:
                self._input()
            elif instruction == INS_OUTPUT:
                return self._output(modes)
            elif instruction == INS_JUMP_IF_TRUE:
                self._jump_if_true(modes)
            elif instruction == INS_JUMP_IF_FALSE:
                self._jump_if_false(modes)
            elif instruction == INS_LESS_THAN:
                self._less_than(modes)
            elif instruction == INS_EQUALS:
                self._equals(modes)
            elif instruction == INS_DONE:
                return None
            else:
                raise InvalidInstructionException(instruction)


CODE = [3,8,1001,8,10,8,105,1,0,0,21,38,47,64,85,106,187,268,349,430,99999,3,9,1002,9,4,9,1001,9,4,9,1002,9,4,9,4,9,99,3,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,102,5,9,9,1001,9,5,9,4,9,99,3,9,101,3,9,9,102,5,9,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,1002,9,3,9,101,2,9,9,102,4,9,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]


def test_phases(code, phases):
    signal = 0

    a1 = Computer(code, [phases[0], 0])
    a2 = Computer(code, [phases[1]])
    a3 = Computer(code, [phases[2]])
    a4 = Computer(code, [phases[3]])
    a5 = Computer(code, [phases[4]])

    while True:
        r1 = a1.run()
        if r1 is None:
            return signal
        a2.input(r1)
        
        r2 = a2.run()
        if r2 is None:
            return signal
        a3.input(r2)
        
        r3 = a3.run()
        if r3 is None:
            return signal
        a4.input(r3)
        
        r4 = a4.run()
        if r4 is None:
            return signal
        a5.input(r4)
        
        r5 = a5.run()
        if r5 is None:
            return signal
        a1.input(r5)
        
        signal = r5

    return signal


if __name__ == "__main__":
    best = max([test_phases(CODE, phases) for phases in permutations([5,6,7,8,9])])
    print(best)
