#!/usr/bin/env python


from dataclasses import dataclass
from typing import Dict, List, Optional, Self


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    contents: Dict[str, File | Self]


def _smart_split(line: str) -> List[int | str]:
    result: list[int | str] = []
    for item in line.split():
        try:
            result.append(int(item))
        except:
            result.append(item)
    return result


def read_input() -> Directory:
    root = Directory("/", {})
    path: List[Directory] = [root]
    for line in [line.strip() for line in open("day7.txt").readlines()]:
        match _smart_split(line):
            case ["$", "cd", "/"]:
                pass
            case ["$", "cd", ".."]:
                path.pop()
            case ["$", "cd", str(name)]:
                path.append(path[-1].contents[name])  # type: ignore
            case ["$", "ls"]:
                pass
            case ["dir", str(name)]:
                if name not in path[-1].contents:
                    path[-1].contents[name] = Directory(name, {})
            case [int(size), str(name)]:
                if name not in path[-1].contents:
                    path[-1].contents[name] = File(name, size)
            case _:
                raise Exception(f"Unexpected input <{line}>")
    return root


def _directory_size(directory: Directory) -> int:
    size: int = 0
    for entry in directory.contents.values():
        match entry:
            case Directory():
                size += _directory_size(entry)
            case File():
                size += entry.size
    return size


def part1() -> int:
    def _part1(directory: Directory, total_size: int = 0) -> int:
        for entry in directory.contents.values():
            if isinstance(entry, Directory):
                if (size := _directory_size(entry)) < 100000:
                    total_size = _part1(entry, total_size + size)
                else:
                    total_size = _part1(entry, total_size)
        return total_size

    return _part1(read_input())


def part2() -> int:
    def _part2(directory: Directory, sizes: List[int] = []) -> List[int]:
        sizes.append(_directory_size(directory))
        for entry in directory.contents.values():
            if isinstance(entry, Directory):
                _part2(entry, sizes)
        return sizes

    root = read_input()
    space_needed = 30000000 - (70000000 - _directory_size(root))

    all_sizes = _part2(root)
    all_sizes.sort()

    for n in all_sizes:
        if n >= space_needed:
            return n
    return 0


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
