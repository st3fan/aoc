#!/usr/bin/env python3


from dataclasses import dataclass


def readlines(path, fn = lambda x: x):
    with open(path) as fp:
        return [fn(line.strip()) for line in fp.readlines()]

#


@dataclass(order=True)
class Range:
    start: int
    end: int

    @classmethod
    def from_string(cls, s):
        """Create a Range from a string with format 1234-5678"""
        elements = s.split("-")
        return cls(int(elements[0]), int(elements[1]))

    def overlaps_with(self, r):
        """Return True if this range overlaps with the given range"""
        return (r.start >= self.start and r.start <= self.end) or (r.end >= self.start and r.end <= self.end) or (self.end+1 == r.start)

    def merge(self, r):
        """Merge this range with the other range. Returns a new range or None of the ranges do not overlap"""
        #if self.overlaps_with(r):
        return Range(min(self.start, r.start), max(self.end, r.end))


def optimize_ranges(ranges):
    """Merge the overlapping ranges"""
    optimized = []
    for r in sorted(ranges):
        for i, x in enumerate(optimized):
            if x.overlaps_with(r):
                optimized[i] = optimized[i].merge(r)
                break
        else:
            optimized.append(r)
    return optimized


def part1():
    ranges = optimize_ranges(readlines("day20.input", Range.from_string))
    for i in range(len(ranges)-1):
        if (ranges[i+1].start - ranges[i].end) > 1:
            return ranges[i].end+1


def part2():
    total = 0
    ranges = optimize_ranges(readlines("day20.input", Range.from_string))
    for i in range(len(ranges)-1):
        total += ranges[i+1].start - ranges[i].end - 1
    return total


def main():
    print("Part one:", part1())
    print("Part two:", part2())


if __name__ == "__main__":
    main()

