#!/usr/bin/env python


from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Dict, Generator, List, Self, Tuple


class Category(StrEnum):
    SEED = auto()
    SOIL = auto()
    FERTILIZER = auto()
    WATER = auto()
    LIGHT = auto()
    TEMPERATURE = auto()
    HUMIDITY = auto()
    LOCATION = auto()


@dataclass
class Range:
    dst: int
    src: int
    len: int

    @classmethod
    def from_str(cls, s: str) -> Self:
        d, s, l = s.split()
        return cls(int(d), int(s), int(l))

    def map_location(self, location: int) -> int | None:
        if location >= self.src and location <= (self.src + self.len):
            return self.dst + (location - self.src)
        return None


def find_location(
    mappings, src_category: Category, dst_category: Category, location: int
) -> int:
    for r in mappings[(src_category, dst_category)]:
        if dst_location := r.map_location(location):
            return dst_location
    return location


def find_final_location(mappings, location: int) -> int:
    location = find_location(mappings, Category.SEED, Category.SOIL, location)
    location = find_location(mappings, Category.SOIL, Category.FERTILIZER, location)
    location = find_location(mappings, Category.FERTILIZER, Category.WATER, location)
    location = find_location(mappings, Category.WATER, Category.LIGHT, location)
    location = find_location(mappings, Category.LIGHT, Category.TEMPERATURE, location)
    location = find_location(
        mappings, Category.TEMPERATURE, Category.HUMIDITY, location
    )
    location = find_location(mappings, Category.HUMIDITY, Category.LOCATION, location)
    return location


def parse_seed_numbers(s: str) -> List[int]:
    return [int(v) for v in s.split()[1:]]


def parse_mapping(s: str) -> Tuple[Category, Category, List[Range]]:
    header, ranges = s.strip().split(":")
    mapping, _ = header.split()
    src_cat, dst_cat = mapping.split("-to-")
    src_cat = Category[src_cat.upper()]
    dst_cat = Category[dst_cat.upper()]
    return (src_cat, dst_cat, [Range.from_str(s) for s in ranges.strip().split("\n")])


def read_input() -> Tuple[Dict, List]:
    # from day5_test import MAPPINGS, SEED_NUMBERS
    # return (MAPPINGS, SEED_NUMBERS)

    input = open("day5.txt").read()
    sections = input.split("\n\n")
    mappings = {}
    for section in sections[1:]:
        src_cat, dst_cat, ranges = parse_mapping(section)
        mappings[(src_cat, dst_cat)] = ranges
    return mappings, parse_seed_numbers(sections[0])


def part1() -> int:
    mappings, seed_numbers = read_input()
    return min(find_final_location(mappings, n) for n in seed_numbers)


if __name__ == "__main__":
    print("Part 1:", part1())
