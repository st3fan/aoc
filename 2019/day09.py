#!/usr/bin/env python3


from collections import deque
from itertools import permutations


INS_ADD           = 1
INS_MULTIPLY      = 2
INS_INPUT         = 3
INS_OUTPUT        = 4
INS_JUMP_IF_TRUE  = 5
INS_JUMP_IF_FALSE = 6
INS_LESS_THAN     = 7
INS_EQUALS        = 8
INS_ADJUST_RELATIVE_BASE = 9
INS_DONE          = 99

MODE_POSITION  = 0
MODE_IMMEDIATE = 1
MODE_RELATIVE  = 2


class InvalidInstructionException (Exception):
    def __init__(self, instruction):
        super().__init__("<%d>" % instruction)


class InvalidModeException (Exception):
    pass


class Computer:

    def __init__(self, data, inputs, memory_size=8192, interactive=True):
        self._memory = [0] * memory_size
        for i in range(len(data)):
            self._memory[i] = data[i]
        self._pc = 0
        self._inputs = deque(inputs)
        self._outputs = []
        self._relative_base = 0
        self._interactive = interactive

    def input(self, value):
        self._inputs.append(value)
        
    def _parse_modes(self, instruction):
        i = "%.5d" % instruction
        return (int(i[2]), int(i[1]), int(i[0]))
        
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
        
    def _load(self, a, mode):
        if mode == MODE_IMMEDIATE:
            return a
        elif mode == MODE_POSITION:
            return self._memory[a]
        elif mode == MODE_RELATIVE:
            return self._memory[self._relative_base + a]
        else:
            raise InvalidModeException()

    def _store(self, a, mode, v):
        if mode == MODE_IMMEDIATE:
            pass
        if mode == MODE_POSITION:
            self._memory[a] = v
        elif mode == MODE_RELATIVE:
            self._memory[self._relative_base + a] = v
        else:
            raise InvalidModeException()
        
    def _add(self, modes, a, b, d):
        self._store(d, modes[2], self._load(a, modes[0]) + self._load(b, modes[1]))
        
    def _multiply(self, modes, a, b, d):
        self._store(d, modes[2], self._load(a, modes[0]) * self._load(b, modes[1]))

    def _input(self, modes, a):
        if self._interactive:
            self._store(a, modes[0], int(input("=> ")))
        else:
            self._store(a, modes[0], self._inputs.popleft())

    def _output(self, modes, s):
        v = self._load(s, modes[0])
        if self._interactive:
            print(v)
        else:
            self._outputs.append(v)
        
    def _jump_if_true(self, modes, a, d):
        if self._load(a, modes[0]) != 0:
            self._pc = self._load(d, modes[1])

    def _jump_if_false(self, modes, a, d):
        if self._load(a, modes[0]) == 0:
            self._pc = self._load(d, modes[1])

    def _less_than(self, modes, a, b, d):
        if self._load(a, modes[0]) < self._load(b, modes[1]):
            self._store(d, modes[2], 1)
        else:
            self._store(d, modes[2], 0)

    def _equals(self, modes, a, b, d):
        if self._load(a, modes[0]) == self._load(b, modes[1]):
            self._store(d, modes[2], 1)
        else:
            self._store(d, modes[2], 0)

    def _adjust_relative_base(self, modes, a):
        self._relative_base += self._load(a, modes[0])
            
    def run(self, debug = False):
        while True:
            instruction, modes = self._fetch()
            if debug:
                print(instruction, modes)
            if instruction == INS_ADD:
                self._add(modes, self._pop(), self._pop(), self._pop())
            elif instruction == INS_MULTIPLY:
                self._multiply(modes, self._pop(), self._pop(), self._pop())
            elif instruction == INS_INPUT:
                self._input(modes, self._pop())
            elif instruction == INS_OUTPUT:
                v = self._output(modes, self._pop())
                if not self._interactive:
                    return v
            elif instruction == INS_JUMP_IF_TRUE:
                self._jump_if_true(modes, self._pop(), self._pop())
            elif instruction == INS_JUMP_IF_FALSE:
                self._jump_if_false(modes, self._pop(), self._pop())
            elif instruction == INS_LESS_THAN:
                self._less_than(modes, self._pop(), self._pop(), self._pop())
            elif instruction == INS_EQUALS:
                self._equals(modes, self._pop(), self._pop(), self._pop())
            elif instruction == INS_ADJUST_RELATIVE_BASE:
                self._adjust_relative_base(modes, self._pop())
            elif instruction == INS_DONE:
                return self._outputs
            else:
                raise InvalidInstructionException(instruction)


PROGRAM = [1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1101,0,3,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1101,0,396,1029,1101,0,356,1023,1101,401,0,1028,1101,24,0,1008,1101,33,0,1019,1101,35,0,1010,1102,359,1,1022,1102,32,1,1001,1101,37,0,1004,1101,0,31,1009,1101,0,30,1003,1101,28,0,1002,1102,1,36,1014,1102,20,1,1012,1101,21,0,1000,1101,0,22,1015,1102,23,1,1013,1102,1,1,1021,1102,1,39,1007,1102,26,1,1017,1101,0,38,1016,1101,0,437,1024,1102,432,1,1025,1101,0,421,1026,1101,0,29,1005,1101,27,0,1011,1102,1,0,1020,1101,0,25,1018,1101,0,414,1027,1102,34,1,1006,109,6,2108,33,-3,63,1005,63,201,1001,64,1,64,1105,1,203,4,187,1002,64,2,64,109,14,21108,40,40,-6,1005,1014,221,4,209,1105,1,225,1001,64,1,64,1002,64,2,64,109,-21,2102,1,3,63,1008,63,28,63,1005,63,251,4,231,1001,64,1,64,1106,0,251,1002,64,2,64,109,12,2101,0,-3,63,1008,63,21,63,1005,63,275,1001,64,1,64,1105,1,277,4,257,1002,64,2,64,109,-10,1207,1,27,63,1005,63,293,1105,1,299,4,283,1001,64,1,64,1002,64,2,64,109,9,21108,41,42,3,1005,1013,315,1105,1,321,4,305,1001,64,1,64,1002,64,2,64,109,-12,1202,6,1,63,1008,63,37,63,1005,63,347,4,327,1001,64,1,64,1105,1,347,1002,64,2,64,109,29,2105,1,-4,1105,1,365,4,353,1001,64,1,64,1002,64,2,64,109,-17,2108,32,-9,63,1005,63,387,4,371,1001,64,1,64,1105,1,387,1002,64,2,64,109,17,2106,0,1,4,393,1105,1,405,1001,64,1,64,1002,64,2,64,109,1,2106,0,-1,1001,64,1,64,1106,0,423,4,411,1002,64,2,64,109,-13,2105,1,9,4,429,1106,0,441,1001,64,1,64,1002,64,2,64,109,3,21107,42,41,-1,1005,1017,461,1001,64,1,64,1106,0,463,4,447,1002,64,2,64,109,-4,21107,43,44,1,1005,1015,481,4,469,1106,0,485,1001,64,1,64,1002,64,2,64,109,-6,21101,44,0,6,1008,1014,47,63,1005,63,505,1106,0,511,4,491,1001,64,1,64,1002,64,2,64,109,-6,1208,-1,32,63,1005,63,529,4,517,1105,1,533,1001,64,1,64,1002,64,2,64,109,11,1205,7,545,1106,0,551,4,539,1001,64,1,64,1002,64,2,64,109,11,21102,45,1,-7,1008,1017,48,63,1005,63,575,1001,64,1,64,1106,0,577,4,557,1002,64,2,64,109,-8,1206,5,593,1001,64,1,64,1105,1,595,4,583,1002,64,2,64,109,7,1206,-3,609,4,601,1106,0,613,1001,64,1,64,1002,64,2,64,109,-10,2101,0,-6,63,1008,63,39,63,1005,63,635,4,619,1106,0,639,1001,64,1,64,1002,64,2,64,109,-9,1208,0,39,63,1005,63,655,1106,0,661,4,645,1001,64,1,64,1002,64,2,64,109,4,2107,25,0,63,1005,63,681,1001,64,1,64,1105,1,683,4,667,1002,64,2,64,109,-5,2107,31,-2,63,1005,63,701,4,689,1106,0,705,1001,64,1,64,1002,64,2,64,109,19,1205,-1,719,4,711,1105,1,723,1001,64,1,64,1002,64,2,64,109,-17,1201,3,0,63,1008,63,24,63,1005,63,745,4,729,1106,0,749,1001,64,1,64,1002,64,2,64,109,13,21102,46,1,-3,1008,1015,46,63,1005,63,771,4,755,1105,1,775,1001,64,1,64,1002,64,2,64,109,-13,1207,4,32,63,1005,63,793,4,781,1106,0,797,1001,64,1,64,1002,64,2,64,109,7,2102,1,-9,63,1008,63,27,63,1005,63,821,1001,64,1,64,1105,1,823,4,803,1002,64,2,64,109,-18,1201,8,0,63,1008,63,25,63,1005,63,847,1001,64,1,64,1106,0,849,4,829,1002,64,2,64,109,23,21101,47,0,2,1008,1019,47,63,1005,63,871,4,855,1106,0,875,1001,64,1,64,1002,64,2,64,109,-22,1202,5,1,63,1008,63,19,63,1005,63,899,1001,64,1,64,1106,0,901,4,881,4,64,99,21102,27,1,1,21102,1,915,0,1105,1,922,21201,1,25165,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21102,942,1,0,1105,1,922,22102,1,1,-1,21201,-2,-3,1,21101,0,957,0,1105,1,922,22201,1,-1,-2,1106,0,968,21201,-2,0,-2,109,-3,2105,1,0]


if __name__ == "__main__":
    c = Computer(PROGRAM, [])
    c.run()
