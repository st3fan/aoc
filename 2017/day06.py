#!/usr/bin/env python3


INPUT = (14,0,15,12,11,11,3,5,1,6,8,4,9,1,8,4)


def redistribute(banks):
    banks = list(banks)
    index = banks.index(max(banks))

    value = banks[index]
    banks[index] = 0

    for _ in range(value):
        index += 1
        if index == len(banks):
            index = 0
        banks[index] += 1

    return tuple(banks)


if __name__ == "__main__":

    # Part 1

    seen = set()
    banks = INPUT
    cycles = 0

    while banks not in seen:
        seen.add(banks)
        banks = redistribute(banks)
        cycles += 1

    print("Part one:", cycles)

    # Part 2

    cycles = 0
    seen = set()

    while banks not in seen:
        seen.add(banks)
        banks = redistribute(banks)
        cycles += 1

    print("Part two:", cycles)
