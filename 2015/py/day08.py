#!/usr/bin/env python3


from ast import literal_eval
import json


def encode(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

def decode(s):
    return literal_eval(s) # So lazy


if __name__ == "__main__":

    input = [line.strip() for line in open("day08.input").readlines()]

    # Part 1

    raw_length = sum(len(literal) for literal in input)
    decoded_length = sum(len(decode(literal)) for literal in input)

    print("Part one:", raw_length - decoded_length)

    # Part 2

    encoded_length = sum(len(encode(literal)) for literal in input)
    print("Part two:", encoded_length - raw_length)

