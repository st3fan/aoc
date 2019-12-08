#!/usr/bin/env python3

WIDTH  = 25
HEIGHT = 6
SIZE   = WIDTH * HEIGHT


def count_digits(layer, digit):
    total = 0
    for d in layer:
        if d == digit:
            total += 1
    return total


def first_visible_pixel(layers, x, y):
    for layer in layers:
        if layer[y*WIDTH+x] in ('0', '1'):
            return layer[y*WIDTH+x]
    print("FAIL?")

def colorize(pixel):
    if pixel == '1':
        return u"\u2588"
    return ' '

if __name__ == "__main__":

    with open("day08.data") as f:
        data = f.read()
    layers = [data[n*SIZE:(n+1)*SIZE] for n in range(len(data) // SIZE)]

    # Part One
    
    found_idx, min_digits = 0, 9999
    for idx, layer in enumerate(layers):
        n = count_digits(layer, '0')
        if n < min_digits:
            found_idx = idx
            min_digits = n

    layer = layers[found_idx]

    print("Part one:", count_digits(layer, '1') * count_digits(layer, '2'))

    # Part Two

    print("Part two:")
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(colorize(first_visible_pixel(layers, x, y)), end="")
        print()
