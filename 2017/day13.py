#!/usr/bin/env python3


from dataclasses import dataclass


@dataclass
class Layer:
    dept: int
    rang: int
    scanner_position: int = 0
    scanner_direction: bool = True # True is down, False is up

    def tick(self):
        if self.scanner_direction == True:
            self.scanner_position += 1
            if self.scanner_position > (self.rang-1):
                self.scanner_direction = False
                self.scanner_position -= 2
        else:
            self.scanner_position -= 1
            if self.scanner_position == -1:
                self.scanner_direction = True
                self.scanner_position = 1

    def severity(self):
        return self.dept * self.rang

    def position_at(self, t):
        return (t + self.dept) % ((self.rang - 1) * 2)

    def caught_at(self, t):
        return self.position_at(t) == 0


if __name__ == "__main__":

    # Part 1

    layers = {}
    with open("day13.input") as fp:
        for line in [line.strip() for line in fp.readlines()]:
            dept, rang = line.split(": ")
            layers[int(dept)] = Layer(int(dept), int(rang))

    total_severity = 0

    # Each picosecond, the packet moves one layer forward (its first move
    # takes it into layer 0), and then the scanners move one step.

    for layer_index in range(max(layers.keys())):
        if layer_index in layers:
            # If there is a scanner at the top of the layer as your packet enters
            # it, you are caught. (If a scanner moves into the top of its layer
            # while you are there, you are not caught: it doesn't have time to
            # notice you before you leave.)
            layer = layers[layer_index]
            if layer.scanner_position == 0:
                total_severity += layer.severity()

        # The scanners move one step
        for layer in layers.values():
            layer.tick()

    print("Part one:", total_severity)

    # Part 2

    layers = {}
    with open("day13.input") as fp:
        for line in [line.strip() for line in fp.readlines()]:
            dept, rang = line.split(": ")
            layers[int(dept)] = Layer(int(dept), int(rang))

    for delay in range(5_000_000):
        # A lazy generator here is 10x faster than a list comprehension
        if not any(layer.caught_at(delay) for layer in layers.values()):
            break
    print("Part two:", delay)


