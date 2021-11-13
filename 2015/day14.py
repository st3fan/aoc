#!/usr/bin/env python3


from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Reindeer:
    name: str
    speed: int
    fly: int
    rest: int

    @classmethod
    def from_description(cls, description):
        """Dancer can fly 37 km/s for 1 seconds, but then must rest for 36 seconds"""
        c = description.split()
        return cls(c[0], int(c[3]), int(c[6]), int(c[13]))

    def distance_at(self, t):
        cycles = t // (self.fly + self.rest)
        distance = cycles * self.fly * self.speed
        remaining = t % (self.fly + self.rest)
        distance += min(remaining, self.fly) * self.speed
        return distance


def main():
    reindeer = [Reindeer.from_description(line) for line in open("day14.input").readlines()]

    # Part 1
    
    print("Part one:", max(r.distance_at(2503) for r in reindeer))

    # Part 2

    points = defaultdict(int)
    for t in range(1, 2504):
        distances = [r.distance_at(t) for r in reindeer]
        m = max(distances)
        i = distances.index(m)
        points[reindeer[i].name] += 1

    print("Part two:", max(points.values()))


if __name__ == "__main__":
    main()

