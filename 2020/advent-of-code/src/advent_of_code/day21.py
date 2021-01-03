#!/usr/bin/env python3

import re

def parse_line(line):
    matches = re.match(r"(.+) \(contains (.+)\)", line)
    return {"ingredients": set(matches[1].split()), "allergens": set(matches[2].split(", "))}

if __name__ == "__main__":

    foods = [parse_line(line) for line in open("../../resources/advent_of_code/2020/day21/input")]
    allergens = {}

    for _ in range(len(foods)):
        for a in set.union(*[food['allergens'] for food in foods]):
            ingredients = set.intersection(*[f['ingredients'] for f in foods if a in f['allergens']])
            if len(ingredients) == 1:
                i = list(ingredients)[0]
                allergens[a] = i
                for f in foods:
                    if a in f['allergens']:
                        f['allergens'].remove(a)
                    if i in f['ingredients']:
                        f['ingredients'].remove(i)

    answer1 = sum([len(f['ingredients']) for f in foods])
    print("ANSWER1:", answer1)

    answer2 = ",".join([allergens[i] for i in sorted(allergens.keys())])
    print("ANSWER2:", answer2)


