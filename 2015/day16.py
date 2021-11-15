#!/usr/bin/env python3


KNOWNS = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def matches1(knowns, aunt):
    for k, v in aunt.items():
        if knowns[k] != v:
            return False
    return True


def matches2(knowns, aunt):
    for k, v in aunt.items():
        match k:
            case "cats" | "trees":
                if not knowns[k] > v:
                    return False
            case "pomeranians" | "goldfish":
                if not knowns[k] < v:
                    return False
            case _:
                if knowns[k] != v:
                    return False
    return True


def load_aunts():
    aunts = {}
    with open("day16.input") as fp:
        for line in (line.strip() for line in fp.readlines()):
            c = int(line[4:].split(":", 1)[0])
            properties = {}
            for name, value in [s.split(": ") for s in line.split(": ", 1)[1].split(", ")]:
                properties[name] = int(value)
            aunts[c] = properties
    return aunts


def main():
    # Part 1
    aunts = load_aunts()
    for n in range(1,501):
        if not matches1(KNOWNS, aunts[n]):
            del aunts[n]
    print("Part one:", list(aunts.keys())[0])

    # Part 2
    aunts = load_aunts()
    for n in range(1,501):
        if not matches2(KNOWNS, aunts[n]):
            del aunts[n]
    print(aunts)
    print("Part two:", list(aunts.keys())[0])


if __name__ == "__main__":
    main()

