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
        return self._load(s, modes[0])
        
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
                # TODO if interactive ... move code here
            elif instruction == INS_OUTPUT:
                v = self._output(modes, self._pop())
                if self._interactive:
                    print(v)
                else:
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
                if self._interactive:
                    return self._outputs
                else:
                    return
            else:
                raise InvalidInstructionException(instruction)


PROGRAM = [3,8,1005,8,319,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,28,2,1105,12,10,1006,0,12,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,58,2,107,7,10,1006,0,38,2,1008,3,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,90,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,112,1006,0,65,1,1103,1,10,1006,0,91,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,144,1006,0,32,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,169,1,109,12,10,1006,0,96,1006,0,5,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,201,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,223,1,4,9,10,2,8,5,10,1,3,4,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,257,1,1,9,10,1006,0,87,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,287,2,1105,20,10,1,1006,3,10,1,3,4,10,101,1,9,9,1007,9,1002,10,1005,10,15,99,109,641,104,0,104,1,21102,1,932972962600,1,21101,0,336,0,1106,0,440,21101,838483681940,0,1,21101,0,347,0,1106,0,440,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,3375393987,0,1,21101,394,0,0,1105,1,440,21102,46174071847,1,1,21102,1,405,0,1106,0,440,3,10,104,0,104,0,3,10,104,0,104,0,21101,988648461076,0,1,21101,428,0,0,1106,0,440,21101,0,709580452200,1,21101,439,0,0,1105,1,440,99,109,2,22101,0,-1,1,21101,40,0,2,21102,1,471,3,21102,461,1,0,1106,0,504,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,466,467,482,4,0,1001,466,1,466,108,4,466,10,1006,10,498,1102,0,1,466,109,-2,2105,1,0,0,109,4,1202,-1,1,503,1207,-3,0,10,1006,10,521,21102,1,0,-3,22102,1,-3,1,21201,-2,0,2,21101,0,1,3,21102,540,1,0,1106,0,545,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,568,2207,-4,-2,10,1006,10,568,22101,0,-4,-4,1105,1,636,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,1,587,0,1105,1,545,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,606,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,628,21201,-1,0,1,21101,0,628,0,106,0,503,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]

COLOR_BLACK = 0
COLOR_WHITE = 1

TURN_LEFT = 0
TURN_RIGHT = 1

DIRECTION_UP = 0
DIRECTION_RIGHT = 1
DIRECTION_DOWN = 2
DIRECTION_LEFT = 3

def one():
    x, y = 0, 0
    direction = DIRECTION_UP
    visible = set()
    painted = set()

    c = Computer(PROGRAM, [], interactive=False)
    
    while True:
        #
        # Run to get the color to paint. Input is the color of the current tile.
        #
            
        if (x,y) in visible:
            c.input(COLOR_WHITE)
        else:
            c.input(COLOR_BLACK)

        paint_color = c.run()
        if paint_color is None:
            break

        painted.add((x,y))
        
        if paint_color == COLOR_WHITE:
            visible.add((x,y))
        elif paint_color == COLOR_BLACK:
            if (x,y) in visible:
                visible.remove((x,y))

        #
        # Run to get the direction to turn. No input.
        #
            
        turn = c.run()
        if turn is None:
            break

        if turn == TURN_LEFT:
            direction -= 1
            if direction == -1:
                direction = DIRECTION_LEFT
        elif turn == TURN_RIGHT:
            direction += 1
            if direction == 4:
                direction = DIRECTION_UP

        if direction == DIRECTION_UP:
            y += 1
        elif direction == DIRECTION_LEFT:
            x -= 1
        elif direction == DIRECTION_DOWN:
            y -= 1
        elif direction == DIRECTION_RIGHT:
            x += 1

    print("Day 11.1:", len(painted))


def two():

    x, y = 0, 0
    direction = DIRECTION_UP
    visible = set()
    painted = set()

    c = Computer(PROGRAM, [], interactive=False)

    visible.add((0,0))
    
    while True:
        #
        # Run to get the color to paint. Input is the color of the current tile.
        #
            
        if (x,y) in visible:
            c.input(COLOR_WHITE)
        else:
            c.input(COLOR_BLACK)

        paint_color = c.run()
        if paint_color is None:
            break

        painted.add((x,y))
        
        if paint_color == COLOR_WHITE:
            visible.add((x,y))
        elif paint_color == COLOR_BLACK:
            if (x,y) in visible:
                visible.remove((x,y))

        #
        # Run to get the direction to turn. No input.
        #
            
        turn = c.run()
        if turn is None:
            break

        if turn == TURN_LEFT:
            direction -= 1
            if direction == -1:
                direction = DIRECTION_LEFT
        elif turn == TURN_RIGHT:
            direction += 1
            if direction == 4:
                direction = DIRECTION_UP

        if direction == DIRECTION_UP:
            y += 1
        elif direction == DIRECTION_LEFT:
            x -= 1
        elif direction == DIRECTION_DOWN:
            y -= 1
        elif direction == DIRECTION_RIGHT:
            x += 1

    #
    # Oh dear, this is horrible :-)
    #
    
    minx = min([p[0] for p in visible])
    maxx = max([p[0] for p in visible])
    
    miny = min([p[1] for p in visible])
    maxy = max([p[1] for p in visible])

    width = abs(minx)+maxx+1
    height = abs(miny)+maxy+1
    output = bytearray(width * height)

    for p in visible:
        x = p[0] + abs(minx)
        y = p[1] + abs(miny)
        output[(y*width)+x] = 1

    print("Day 11.2:")
    for y in range(height-1, -1, -1):
        for x in range(width):
            if output[(y*width)+x]:
                print(u"\u2588", end="")
            else:
                print(" ", end="")
        print("")


if __name__ == "__main__":
    one()
    two()
