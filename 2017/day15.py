#!/usr/bin/env python3


from itertools import count, islice


if __name__ == "__main__":

    # Part 1

    def generator(start, factor):
        n = start
        while True:
            n = (n * factor) % 2147483647
            yield n
        matches = 0

    matches = 0
    for a, b in islice(zip(generator(873, 16807), generator(583, 48271)), 40000000):
        if a & 0xffff == b & 0xffff:
            matches += 1

    print("Part one:", matches)

    # Part 2

    def generator2(start, factor, modulus):
        n = start
        while True:
            n = (n * factor) % 2147483647
            if n % modulus == 0:
                yield n

    matches = 0
    for a, b in islice(zip(generator2(873, 16807, 4), generator2(583, 48271, 8)), 5000000):
        if a & 0xffff == b & 0xffff:
            matches += 1

    print("Part two:", matches)
