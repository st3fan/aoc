#!/usr/bin/env python3


import json


if __name__ == "__main__":

    input = [line.strip() for line in open("day08.input").readlines()]

    # Part 1

    raw_length = sum(len(literal) for literal in input)
    print(raw_length)

    decoded_length = sum(len(eval(literal)) for literal in input)
    print(decoded_length)

    print("Part one:", raw_length - decoded_length)

    # Part 2

