#!/usr/bin/env python3


from dataclasses import dataclass
from itertools import chain, cycle, groupby


def read_input(path):
    with open(path) as fp:
        for t, v in zip(cycle(("F", "S")), fp.read().strip()):
            yield t, int(v)


def build_disk_map(path) -> list[int | None]:
    disk_map: list[int | None] = []
    file_id = 0
    for type, length in read_input(path):
        match type, length:
            case "F", length:
                disk_map += [file_id] * length
                file_id += 1
            case "S", length:
                disk_map += [None] * length
    return disk_map


def compact_disk_map(disk_map: list[int | None]) -> list[int | None]:
    r = reversed([v for v in disk_map if v is not None])
    n = sum(v is not None for v in disk_map)
    compacted: list[int] = []
    free: list[None] = []
    for v in disk_map:
        if v is None:
            compacted.append(next(r))
            free.append(None)
        else:
            compacted.append(v)
            free.append(None)
        if len(free) == n:
            break
    return compacted + free


@dataclass
class Chunk:
    value: int | None
    length: int
    seen: bool

    def to_list(self) -> list[int | None]:
        return [self.value] * self.length


def next_unseen(chunks: list[Chunk], start: int) -> int | None:
    """From right to left find the next file chunk not seen yet"""
    for i in range(start - 1, -1, -1):
        if chunks[i].value is not None and not chunks[i].seen:
            return i


def find_space(chunks: list[Chunk], length: int) -> int | None:
    """Find the first space chunk that has room for a file of length"""
    for i, c in enumerate(chunks):
        if c.value is None and c.length >= length:
            return i


def optimiz_disk_map(disk_map: list[int | None]) -> list[int | None]:
    chunks: list[Chunk] = []
    for _, g in groupby(disk_map):
        g = list(g)
        chunks.append(Chunk(g[0], len(g), False))

    last_seen_index = len(chunks)

    while True:
        # Find the next unseen file chunk
        if (srci := next_unseen(chunks, last_seen_index)) is None:
            break  # None left, we're done

        last_seen_index = srci + 1

        srcc = chunks[srci]

        # Replace the unseen chunk with free space. Worst case it will go back in there.
        chunks[srci] = Chunk(None, srcc.length, False)

        # Find the first space where this chunk fits. May be its original space.
        if (dsti := find_space(chunks, srcc.length)) is not None:
            dstc = chunks[dsti]
            # Replace it and maybe add some space
            chunks[dsti] = srcc
            if srcc.length < dstc.length:
                chunks.insert(dsti + 1, Chunk(None, dstc.length - srcc.length, False))

        # Mark this chunk as seen
        srcc.seen = True

    # Flatten the chunks into a list
    return list(chain.from_iterable(c.to_list() for c in chunks))


def checksum_disk_map(disk_map: list[int | None]) -> int:
    return sum(i * v for i, v in enumerate(disk_map) if v is not None)


if __name__ == "__main__":
    print("Part1:", checksum_disk_map(compact_disk_map(build_disk_map("day9.txt"))))
    print("Part2:", checksum_disk_map(optimiz_disk_map(build_disk_map("day9.txt"))))
