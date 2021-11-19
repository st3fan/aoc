#!/usr/bin/env python3


import random
from collections import defaultdict


def read_input(path):
    with open(path) as fp:
        replacements = defaultdict(list)
        for line in (line.strip() for line in fp.readlines()):
            if " => " in line:
                a, b = line.split(" => ")
                replacements[a].append(b)
            elif len(line) != 0:
                return replacements, line


def replace(src, s, start, end):
    return s.join([src[:start], src[end:]])


def main():
    # Part 1

    replacements, medicine = read_input("day19.input")

    result = set()
    for i in range(len(medicine)):
        m = medicine[i]
        if m in replacements:
            for r in replacements[m]:
                result.add(replace(medicine, r, i, i+1))
        if i < len(medicine):
            m = medicine[i:i+2]
            if m in replacements:
                for r in replacements[m]:
                    result.add(replace(medicine, r, i, i+2))
    print("Part one:", len(result))

    # Part 2 - I wonder if the puzzle input generator made a mistake
    # here because this "reverse replacement" solution only works
    # when I randomize the replacements. I get the right answer but
    # it takes a few thousand tries.

    replacements, medicine = read_input("day19.input")

    def part2(medicine, replacements):
        reverse_replacements = {}
        for k, v in replacements.items():
            for e in replacements[k]:
                reverse_replacements[e] = k

        reverse_replacements_keys = list(reverse_replacements.keys())
        random.shuffle(reverse_replacements_keys)

        steps = 0
        while medicine != "e":
            m = medicine
            for r in reverse_replacements_keys:
                if r in medicine:
                    medicine = medicine.replace(r, reverse_replacements[r], 1)
                    steps += 1
            if m == medicine:
                # No changes so we're locked in a loop
                return None
        return steps

    for n in range(1, 1_000_000):
        if steps := part2(medicine, replacements):
            print(f"Part two: {steps} (with {n} shuffles)")
            break

if __name__ == "__main__":
    random.seed()
    main()
