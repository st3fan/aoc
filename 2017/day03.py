#!/usr/bin/env python3


from aoc import around, nth, manhattan_distance
from itertools import count, cycle


def spiral():
    directions = cycle([(1, 0), (0, 1), (-1, 0), (0, -1)])

    current = (0,0)
    yield current
    
    for i in count(start=1):
        for _ in range(2):
            direction = next(directions)
            for j in range(i):
                current = (current[0] + direction[0], current[1] + direction[1])
                yield current
        

if __name__ == "__main__":

    # Part 1

    print("Part one:", manhattan_distance(nth(spiral(), 265149-1)))

    # Part 2

    def value_for_square(seen, p):
        if p == (0,0):
            return 1
        return sum(seen.get(q, 0) for q in around(p))
            
    seen = {}
    for p in spiral():
        seen[p] = value_for_square(seen, p)
        if seen[p] > 265149:
            print("Part two:", seen[p])
            break

