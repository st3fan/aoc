#!/usr/bin/env python3


from time import time


def parse_instruction(s):
    instruction = s.split()
    try:
        instruction[2] = int(instruction[2])
    except:
        pass
    return instruction


def load():
    return [parse_instruction(line.strip()) for line in open("day24.input").readlines()]


def generate_alu(program):
    print("uint64_t execute_alu(uint64_t inputs[14]) {")
    print("  uint64_t x = 0, y = 0, z = 0, w = 0;")
    input_index = 0
    for instruction in program:
        match instruction:
            case ["inp", str(r)]:
                print(f"  {r} = inputs[{input_index}];")
                input_index += 1
            case ["add", str(r), int(v)]:
                print(f"  {r} += {v};")
            case ["add", str(r1), str(r2)]:
                print(f"  {r1} += {r2};")
            case ["mul", str(r), int(v)]:
                print(f"  {r} *= {v};")
            case ["mul", str(r1), str(r2)]:
                print(f"  {r1} *= {r2};")
            case ["div", str(r), int(v)]:
                print(f"  {r} /= {v};")
            case ["mod", str(r), int(v)]:
                print(f"  {r} %= {v};")
            case ["eql", str(r), int(v)]:
                print(f"  {r} = ({r} == {v}) ? 1 : 0;")
            case ["eql", str(r1), str(r2)]:
                print(f"  {r1} = ({r1} == {r2}) ? 1 : 0;")
    print("  return z;")
    print("}")
                


def execute(program, input):
    input = list(input)
    registers = {"w": 0, "x": 0, "y": 0, "z": 0}
    for instruction in program:
        match instruction:
            case ["inp", str(r)]:
                registers[r] = input.pop(0)
            case ["add", str(r), int(v)]:
                registers[r] += v
            case ["add", str(r1), str(r2)]:
                registers[r1] += registers[r2]
            case ["mul", str(r), int(v)]:
                registers[r] *= v
            case ["mul", str(r1), str(r2)]:
                registers[r1] *= registers[r2]
            case ["div", str(r), int(v)]:
                registers[r] //= v
            case ["mod", str(r), int(v)]:
                registers[r] %= v
            case ["eql", str(r), int(v)]:
                registers[r] = int(registers[r] == v)
            case ["eql", str(r1), str(r2)]:
                registers[r1] = int(registers[r1] == registers[r2])
    return registers


def model_numbers():
    for a in range(9,0,-1):
        for b in range(9,0,-1):
            for c in range(9,0,-1):
                for d in range(9,0,-1):
                    for e in range(9,0,-1):
                        for f in range(9,0,-1):
                            for g in range(9,0,-1):
                                for h in range(9,0,-1):
                                    for i in range(9,0,-1):
                                        for j in range(9,0,-1):
                                            for k in range(9,0,-1):
                                                for l in range(9,0,-1):
                                                    for m in range(9,0,-1):
                                                        for n in range(9,0,-1):
                                                            yield [a,b,c,d,e,f,g,h,i,j,k,l,m,n]


def part1():
    program = load()
    max_model_number = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i, model_number in enumerate(model_numbers()):
        if i % 1_000_000 == 0:
            print(time(), model_number)
        registers = execute(program, model_number)
        if registers["z"] == 0:
            print("VALID:", model_number)
            max_model_number = max(max_model_number, model_number)


if __name__ == "__main__":
    generate_alu(load())
