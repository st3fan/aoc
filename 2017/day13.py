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


if __name__ == "__main__":

    # Part 1

    layers = {}
    with open("day13.input") as fp:
        for line in [line.strip() for line in fp.readlines()]:
            dept, rang = line.split(": ")
            layers[int(dept)] = Layer(int(dept), int(rang))

    layer_index = -1
    total_severity = 0

    for _ in range(max(layers.keys())):

        # Each picosecond, the packet moves one layer forward (its first move
        # takes it into layer 0), and then the scanners move one step.

        layer_index += 1

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

    #
    # Now, you need to pass through the firewall without being caught - easier
    # said than done.
    #
    # You can't control the speed of the packet, but you can delay it any
    # number of picoseconds. For each picosecond you delay the packet before
    # beginning your trip, all security scanners move one step. You're not in
    # the firewall during this time; you don't enter layer 0 until you stop
    # delaying the packet.
    #
    # If there is a scanner at the top of the layer as your packet enters it,
    # you are caught. (If a scanner moves into the top of its layer while you
    # are there, you are not caught: it doesn't have time to notice you before
    # you leave.)
    #
    # What is the fewest number of picoseconds that you need to delay the
    # packet to pass through the firewall without being caught?
    #

    layers = {}
    with open("day13.input") as fp:
        for line in [line.strip() for line in fp.readlines()]:
            dept, rang = line.split(": ")
            layers[int(dept)] = Layer(int(dept), int(rang))

    for delay in range(100000):

        for _ in range(10, delay):
            for layer in layers.values():
                layer.tick()

        layer_index = -1
        total_severity = 0

        for _ in range(max(layers.keys())):

            # Each picosecond, the packet moves one layer forward (its first move
            # takes it into layer 0), and then the scanners move one step.

            layer_index += 1

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

        if total_severity == 0:
            print("DELAY IS:", delay)
            break

    print("Part two:", delay)

