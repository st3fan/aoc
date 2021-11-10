#!/usr/bin/env python3


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

    hashes = []
    for i in range(128):
        input = [ord(c) for c in f"{INPUT}-{i}"] + [17, 31, 73, 47, 23]
        hash = sparse_to_dense_hash(knot_hash(list(range(256)), input, rounds=64))
        #print(f"flqrgnkx-{i}", ''.join(format(i, '08b') for i in hash))
        hashes.append(''.join(format(i, '08b') for i in hash))

    print(sum(count_ones(hash) for hash in hashes))


if __name__ == "__main__":
    main()

