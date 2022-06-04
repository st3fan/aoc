#!/usr/bin/env python3


from itertools import permutations


def main():
    guests = set() # of names
    pairs = {} # of (guest,guest) -> happiness

    with open("day13.input") as fp:
        for line in (line.strip(".\r\n").split() for line in fp.readlines()):
            happiness = int(line[3])
            if line[2] == "lose":
                happiness = -happiness
            guests.add(line[0])
            pairs[(line[0], line[10])] = happiness

    # Part 1

    max_happiness = 0
    for l in permutations(list(guests)):
        l = list(l)
        gains = 0
        for i in range(0, len(l)):
            gains += pairs[(l[i], l[(i+1) % len(l)])]
            gains += pairs[(l[i], l[i-1])]
        max_happiness = max(max_happiness, gains)

    print("Part one:", max_happiness)

    # Part 2

    for guest in guests:
        pairs[("Stefan", guest)] = 0
        pairs[(guest, "Stefan")] = 0
    guests.add("Stefan")

    max_happiness = 0
    for l in permutations(list(guests)):
        l = list(l)
        gains = 0
        for i in range(0, len(l)):
            gains += pairs[(l[i], l[(i+1) % len(l)])]
            gains += pairs[(l[i], l[i-1])]
        max_happiness = max(max_happiness, gains)

    print("Part two:", max_happiness)


if __name__ == "__main__":
    main()

