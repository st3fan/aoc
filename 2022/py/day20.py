#!/usr/bin/env python


from dataclasses import dataclass
from typing import List


@dataclass(frozen=True, eq=False)
class Number:
    value: int


def read_input(multiplier: int = 1) -> List[Number]:
    return [Number(int(line.strip()) * multiplier) for line in open("day20.txt").readlines()]


def _decrypt(encrypted: List[Number], rounds: int) -> int:
    decrypted: List[Number] = encrypted.copy()

    for _ in range(rounds):
        for number in encrypted:
            current_index = decrypted.index(number)
            if number.value != 0:
                if number.value > 0:
                    del decrypted[current_index]
                    new_index = (current_index + number.value) % len(decrypted)
                    decrypted.insert(new_index, number)
                if number.value < 0:
                    del decrypted[current_index]
                    new_index = (current_index + number.value) % len(decrypted)
                    if new_index == 0:
                        decrypted.append(number)
                    else:
                        decrypted.insert(new_index, number)

    for n in encrypted:
        if n.value == 0:
            zero = n

            zero_index = decrypted.index(zero)
            return (
                decrypted[(zero_index + 1000) % len(decrypted)].value
                + decrypted[(zero_index + 2000) % len(decrypted)].value
                + decrypted[(zero_index + 3000) % len(decrypted)].value
            )

    raise Exception("Can't happen")


def part1() -> int:
    return _decrypt(read_input(), rounds=1)


def part2() -> int:
    return _decrypt(read_input(multiplier=811589153), rounds=10)


if __name__ == "__main__":
    print("Part 1:", part1())
    print("Part 2:", part2())
