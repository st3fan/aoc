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

    # Part 2 - Unfortunately I pieced this together from Reddit

    pos = 0
    second = None

    for j in range(1, 50000000 // 2):
        check = (pos + INPUT) % j
        if check == 0:
            second = j
        pos = check + 1


    print("Part two:", second)

