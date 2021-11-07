#!/usr/bin/env python3


INPUT = 304


if __name__ == "__main__":

    # Part 1

    ring = [0]
    pos = 0

    for n in range(1, 2018):
        pos = (pos + INPUT) % len(ring)
        ring.insert(pos+1, n)
        pos = (pos + 1) % len(ring)

    print(ring[(pos+1) % len(ring)])

    # Part 2

    ring = [0]
    pos = 0

    for n in range(1, 50000000):
        pos = (pos + INPUT) % len(ring)
        ring.insert(pos+1, n)
        pos = (pos + 1) % len(ring)

    print(ring[(pos+1) % len(ring)])

