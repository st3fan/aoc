#!/usr/bin/env python3


from collections import defaultdict
from threading import Thread
from queue import Queue


class CPU:
    def __init__(self, instructions, pid, snd_queue, rcv_queue):
        self.instructions = instructions
        self.snd_queue = snd_queue
        self.rcv_queue = rcv_queue
        self.registers = defaultdict(int)
        self.registers["p"] = pid
        self.pc = 0
        self.sent = 0

    def __call__(self):
        try:
            self.run()
        except Exception as e:
            print(e)

    def run(self):
        while self.pc >= 0 and self.pc < len(self.instructions):
            #print("Executing", self.instructions[self.pc])
            match self.instructions[self.pc]:
                case ["snd", int(x)]:
                    self.snd_queue.put(x)
                    self.pc += 1
                case ["snd", str(x)]:
                    self.snd_queue.put(self.registers[x])
                    self.pc += 1
                    self.sent += 1
                case ["set", str(x), int(y)]:
                    self.registers[x] = y
                    self.pc += 1
                case ["set", str(x), str(y)]:
                    self.registers[x] = self.registers[y]
                    self.pc += 1
                case ["add", str(x), int(y)]:
                    self.registers[x] += y
                    self.pc += 1
                case ["add", str(x), str(y)]:
                    self.registers[x] += self.registers[y]
                    self.pc += 1
                case ["mul", str(x), int(y)]:
                    self.registers[x] *= y
                    self.pc += 1
                case ["mod", str(x), int(y)]:
                    self.registers[x] = self.registers[x] % y
                    self.pc += 1
                case ["mod", str(x), str(y)]:
                    self.registers[x] = self.registers[x] % self.registers[y]
                    self.pc += 1
                case ["rcv", str(x)]:
                    self.registers[x] = self.rcv_queue.get(block=True, timeout=1)
                    self.pc += 1
                case ["jgz", str(x), int(y)]:
                    if self.registers[x] > 0:
                        self.pc += y 
                    else:
                        self.pc += 1
                case ["jgz", str(x), str(y)]:
                    if self.registers[x] > 0:
                        self.pc += self.registers[y]
                    else:
                        self.pc += 1
                case ["jgz", int(x), int(y)]:
                    if x > 0:
                        self.pc += y
                    else:
                        self.pc += 1
                case ["jgz", int(x), str(y)]:
                    if x > 0:
                        self.pc += self.registers[y]
                    else:
                        self.pc += 1
                case _:
                    raise f"Invalid instruction: {self.instructions[self.pc]}"


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

    # Part 2

    q1 = Queue()
    q2 = Queue()

    print("Starting thread 1")
    c1 = CPU(instructions, 0, q1, q2)
    t1 = Thread(target=c1)
    t1.start()

    print("Starting thread 2")
    c2 = CPU(instructions, 1, q2, q1)
    t2 = Thread(target=c2)
    t2.start()

    print("Waiting for completion")

    t1.join()
    t2.join()

    print("Part two:", c2.sent)

