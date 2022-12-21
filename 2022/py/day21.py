#!/usr/bin/env python


from typing import Any, Dict, List


def _smart_split(line: str) -> List[int | str]:
    result: list[int | str] = []
    for item in line.split():
        try:
            result.append(int(item))
        except:
            result.append(item)
    return result


def read_input() -> List[List[Any]]:
    def _parse_line(line: str) -> List[Any]:
        dst, rest = line.split(":")
        return [dst] + _smart_split(rest)

    return [_parse_line(line.strip()) for line in open("day21.txt").readlines()]


def part1():
    registers: Dict[str, int] = {}
    instructions: List[List[Any]] = read_input()

    while "root" not in registers:
        for instruction in instructions.copy():
            match instruction:
                case [dst, int(v)]:
                    registers[dst] = v
                case [dst, str(a), "+", str(b)]:
                    if a in registers and b in registers:
                        registers[dst] = registers[a] + registers[b]
                        instructions.remove(instruction)
                case [dst, str(a), "-", str(b)]:
                    if a in registers and b in registers:
                        registers[dst] = registers[a] - registers[b]
                        instructions.remove(instruction)
                case [dst, str(a), "*", str(b)]:
                    if a in registers and b in registers:
                        registers[dst] = registers[a] * registers[b]
                        instructions.remove(instruction)
                case [dst, str(a), "/", str(b)]:
                    if a in registers and b in registers:
                        registers[dst] = registers[a] // registers[b]
                        instructions.remove(instruction)
                case _:
                    raise Exception(f"Unknown instruction <{instruction}>")

    return registers["root"]


if __name__ == "__main__":
    for i in read_input():
        print(f"<{i}>")

    print("Part 1:", part1())
