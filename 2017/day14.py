#!/usr/bin/env python3


from itertools import product


INPUT = "ljoxqyyw"


def make_grid(size):
    return [[0] * size] * size


def knot_hash(numbers, lengths, rounds=1):

    current = 0
    skip_size = 0

    for _ in range(rounds):

        for length in lengths:

            # Reverse the order of that length of elements in the list, starting with
            # the element at the current position.

            t = numbers[current:] + numbers[:current]
            t[:length] = reversed(t[:length])
            i = len(numbers) - current
            numbers = t[i:] + t[:i]

            # Move the current position forward by that length plus the skip size.
            # If the current position moves past the end of the list, it wraps
            # around to the front.

            current += length + skip_size
            current %= len(numbers)

            # Increase the skip size by one.

            skip_size += 1

    return numbers


def sparse_to_dense_hash(numbers):
    result = []
    for _ in range(16):
        t = 0
        for _ in range(16):
            t ^= numbers.pop(0)
        result.append(t)
    return bytes(result)


def count_ones(s):
    total = 0
    for c in s:
        if c == "1":
            total += 1
    return total


def main():

    # Part 1

    hashes = []
    for i in range(128):
        input = [ord(c) for c in f"{INPUT}-{i}"] + [17, 31, 73, 47, 23]
        hash = sparse_to_dense_hash(knot_hash(list(range(256)), input, rounds=64))
        hashes.append(''.join(format(i, '08b') for i in hash))

    print("Part one:", sum(count_ones(hash) for hash in hashes))

    # Part 2

    def adjecent(grid, x, y):
        result = []
        for xo, yo in [(-1,0), (1,0), (0,-1), (0,1)]:
            px = x + xo
            py = y + yo
            if px >= 0 and px <= 127 and py >= 0 and py <= 127:
                if grid[py][px] == '1':
                    yield (px, py)

    def mark_group(grid, group, locations):
        for x, y in locations:
            grid[y][x] = group
            if adj := adjecent(grid, x, y):
                mark_group(grid, group, adj)

    grid = [list(row) for row in hashes]
    group = 0

    for y, x in product(range(128), range(128)):
        if grid[y][x] == '1':
            group += 1
            grid[y][x] = group
            if adj := adjecent(grid, x, y):
                mark_group(grid, group, adj)

    print("Part two:", group)


if __name__ == "__main__":
    main()

