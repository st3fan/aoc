#!/usr/bin/env python3


INPUT = [192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12]


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


if __name__ == "__main__":
    
    print("Example:", knot_hash(list(range(5)), [3,4,1,5]))

    result = knot_hash(list(range(256)), INPUT)
    print("Part one:", result[0] * result[1])

    INPUT = [ord(c) for c in "192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12"] + [17, 31, 73, 47, 23]
    print("Part two:", sparse_to_dense_hash(knot_hash(list(range(256)), INPUT, rounds=64)).hex())

