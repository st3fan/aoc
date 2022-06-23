#!/usr/bin/env python3


from collections import Counter


def load_template():
    return open("day14.template").read().strip()


def load_rules():
    def parse_rule(line):
        c = line.split()
        return c[0], c[2]
    return dict([parse_rule(line) for line in open("day14.rules").readlines()])


def step1(template, rules):
    result = []
    for a, b in zip(template[:-1], template[1:]):
        if len(result):
            result.pop()
        result.append(a)
        result.append(rules[a+b])
        result.append(b)
    return "".join(result)


def part1():
    template = load_template()
    rules = load_rules()
    for _ in range(10):
        template = step1(template, rules)
    c = Counter(template).most_common()
    return c[0][1] - c[-1][1]


def step2(counter, rules):
    new_counter = Counter()
    for p, n in counter.items():
        a = p[0] + rules[p] + p[1]
        new_counter[a[0]+a[1]] += n
        new_counter[a[1]+a[2]] += n
    return new_counter


def score(template, counter):   
    atoms = Counter()
    for p, n in counter.items():
        atoms[p[0]] += n
    atoms[template[-1]] += 1
    return max(atoms.values()) - min(atoms.values())


def part2():
    template = load_template()
    rules = load_rules()

    counter = Counter()
    for a, b in zip(template[:-1], template[1:]):
        counter[a + b] += 1

    for _ in range(40):
        counter = step2(counter, rules)

    return score(template, counter)


if __name__ == "__main__":
    print(part1())
    print(part2())
