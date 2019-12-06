#!/usr/bin/env python3


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

    def __init__(self, data):
        self.memory = data
        self.pc = 0

    def _parse_modes(self, instruction):
        i = "%.5d" % instruction
        return (i[2] == "1", i[1] == "1", i[0] == "1")
        
    def _fetch(self):
        instruction = self.memory[self.pc]
        self.pc += 1
        if instruction > 100:
            return instruction % 100, self._parse_modes(instruction)
        else:
            return instruction, (MODE_POSITION, MODE_POSITION, MODE_POSITION)

    def _pop(self):
        v = self.memory[self.pc]
        self.pc += 1
        return v
        
    def _load(self, position, mode):
        if mode == MODE_IMMEDIATE:
            return position
        else:
            return self.memory[position]

    def _store(self, position, value):
        self.memory[position] = value
        
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
        self._store(self._pop(), int(input("$=> ")))

    def _output(self, modes):
        print(self._load(self._pop(), modes[0]))

    def _jump_if_true(self, modes):
        if self._load(self._pop(), modes[0]) != 0:
            self.pc = self._load(self._pop(), modes[1])
        else:
            self._pop()

    def _jump_if_false(self, modes):
        if self._load(self._pop(), modes[0]) == 0:
            self.pc = self._load(self._pop(), modes[1])
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
                self._output(modes)
            elif instruction == INS_JUMP_IF_TRUE:
                self._jump_if_true(modes)
            elif instruction == INS_JUMP_IF_FALSE:
                self._jump_if_false(modes)
            elif instruction == INS_LESS_THAN:
                self._less_than(modes)
            elif instruction == INS_EQUALS:
                self._equals(modes)
            elif instruction == INS_DONE:
                break
            else:
                raise InvalidInstructionException(instruction)

CODE = [
    3,225,1,225,6,6,1100,1,238,225,104,0,1101,32,43,225,101,68,192,224,
    1001,224,-160,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,
    1001,118,77,224,1001,224,-87,224,4,224,102,8,223,223,1001,224,6,224,
    1,223,224,223,1102,5,19,225,1102,74,50,224,101,-3700,224,224,4,224,
    1002,223,8,223,1001,224,1,224,1,223,224,223,1102,89,18,225,1002,14,
    72,224,1001,224,-3096,224,4,224,102,8,223,223,101,5,224,224,1,223,
    224,223,1101,34,53,225,1102,54,10,225,1,113,61,224,101,-39,224,224,
    4,224,102,8,223,223,101,2,224,224,1,223,224,223,1101,31,61,224,101,
    -92,224,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1102,
    75,18,225,102,48,87,224,101,-4272,224,224,4,224,102,8,223,223,1001,
    224,7,224,1,224,223,223,1101,23,92,225,2,165,218,224,101,-3675,224,
    224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1102,8,49,225,
    4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,
    1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,
    1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,
    1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,
    1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,
    99999,1107,226,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,
    1007,677,226,224,1002,223,2,223,1006,224,344,1001,223,1,223,108,677,
    226,224,102,2,223,223,1006,224,359,1001,223,1,223,7,226,226,224,1002,
    223,2,223,1005,224,374,101,1,223,223,107,677,677,224,1002,223,2,223,
    1006,224,389,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,
    404,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,419,1001,
    223,1,223,108,226,226,224,102,2,223,223,1006,224,434,1001,223,1,223,
    1108,226,677,224,1002,223,2,223,1006,224,449,1001,223,1,223,1108,677,
    226,224,102,2,223,223,1005,224,464,1001,223,1,223,107,226,226,224,102,
    2,223,223,1006,224,479,1001,223,1,223,1008,226,226,224,102,2,223,223,
    1005,224,494,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,509,
    101,1,223,223,8,226,677,224,1002,223,2,223,1006,224,524,1001,223,1,223,
    1007,226,226,224,1002,223,2,223,1006,224,539,101,1,223,223,1008,677,
    677,224,1002,223,2,223,1006,224,554,101,1,223,223,1108,677,677,224,
    102,2,223,223,1006,224,569,101,1,223,223,1107,226,677,224,102,2,223,
    223,1005,224,584,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,
    599,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,614,1001,223,
    1,223,7,226,677,224,1002,223,2,223,1005,224,629,101,1,223,223,107,226,
    677,224,102,2,223,223,1005,224,644,101,1,223,223,8,677,677,224,102,2,
    223,223,1005,224,659,1001,223,1,223,108,677,677,224,1002,223,2,223,
    1005,224,674,101,1,223,223,4,223,99,226]

    
if __name__ == "__main__":
    computer = Computer(CODE)
    computer.run()
