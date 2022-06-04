#!/usr/bin/env python3


from dataclasses import dataclass


@dataclass
class Dimensions:
    l: int
    w: int
    h: int

    def paper_needed(self):
        sides = [self.l*self.w, self.w*self.h, self.h*self.l]
        return 2*sum(sides) + min(sides)

    def ribbon_needed(self):
        sides = sorted([self.l, self.w, self.h])
        return sides[0]*2 + sides[1]*2 + (self.l * self.w * self.h)


def main():
    lines = (line.strip() for line in open("day02.input").readlines())
    input = [Dimensions(*[int(e) for e in line.split("x")]) for line in lines]
    
    print("Part one:", sum(d.paper_needed() for d in input))

    print("Part two:", sum(d.ribbon_needed() for d in input))


if __name__ == "__main__":
    main()
