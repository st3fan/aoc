#!/usr/bin/env python3


PROGRAMS = list("abcdefghijklmnop")


def dance(programs, moves):
    for move in moves:
        match move:
            case ["s", int(x)]:
                programs = programs[-x:] + programs[:-x] 
            case ["x", int(x), int(y)]:
                programs[x],programs[y] = programs[y],programs[x]
            case ["p", str(x), str(y)]:
                x = programs.index(x)
                y = programs.index(y)
                programs[x],programs[y] = programs[y],programs[x]
            case _:
                raise Exception(f"Unknown move {move}")
    return programs


if __name__ == "__main__":

    moves = []
    for move in open("day16.input").read().strip().split(","):
        match move[0]:
            case "s":
                moves.append([move[0], int(move[1:])])
            case "x":
                moves.append([move[0]] + [int(e) for e in move[1:].split("/")])
            case "p":
                moves.append([move[0]] + move[1:].split("/"))

    # Part 1

    programs = dance(list(PROGRAMS), moves)
    print("Part one:", "".join(programs))

    # Part 2

    programs = list(PROGRAMS)
    for count in range(1, 100):
        programs = dance(programs, moves)
        if programs == PROGRAMS:
            break

    for _ in range(1000000000 % count):
        programs = dance(programs, moves)

    print("Part two:", "".join(programs))

