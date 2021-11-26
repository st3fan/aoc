

from itertools import count


INPUT_ROW = 3010
INPUT_COLUMN = 3019


def code_generator():
    code = 20151125
    while True:
        yield code
        code = (code * 252533) % 33554393


def position_generator():
    for row in count(start=1):
        for r, c in zip(range(row, 0, -1), range(1, row+1)):
            yield (r, c)


def part1():
    for position, code in zip(position_generator(), code_generator()):
        if position == (INPUT_ROW, INPUT_COLUMN):
            return code


def main():
    print("Part one:", part1())


if __name__ == "__main__":
    main()

