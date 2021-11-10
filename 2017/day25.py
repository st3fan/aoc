#!/usr/bin/env python3


class Blueprint:
    def __init__(self):
        self.start_state = None
        self.steps = None
        self.instructions = {}


class Instruction:
    def __init__(self):
        self.expected_state = None
        self.expected_value = None
        self.write_value = None
        self.next_slot = None
        self.next_state = None


def parse_blueprint(path):
    blueprint = Blueprint()
    current_state = None
    for line in [line.strip(" .:-\r\n").split() for line in open(path).readlines()]:
        match line:
            case ["Begin", "in", "state", state]:
                blueprint.start_state = state
            case ["Perform", "a", "diagnostic", "checksum", "after", steps, "steps"]:
                blueprint.steps = int(steps)
            case ["In", "state", state]:
                current_state = state
            case ["If", "the", "current", "value", "is", value]:
                instruction = Instruction()
                instruction.expected_state = current_state
                instruction.expected_value = int(value)
            case ["Write", "the", "value", value]:
                instruction.write_value = int(value)
            case ["Move", "one", "slot", "to", "the", "right"]:
                instruction.next_slot = 1
            case ["Move", "one", "slot", "to", "the", "left"]:
                instruction.next_slot = -1
            case ["Continue", "with", "state", state]:
                instruction.next_state = state
                blueprint.instructions[(instruction.expected_state, instruction.expected_value)] = instruction
                instruction = None
    return blueprint


def main():
    blueprint = parse_blueprint("day25.input")

    # Part 1

    # A tape which contains 0 repeated infinitely to the left and right

    slots = [0] * 10000 # Does it matter?
    current_slot = 5000
    current_state = blueprint.start_state

    for _ in range(blueprint.steps):
        i = blueprint.instructions[(current_state, slots[current_slot])]
        slots[current_slot] = i.write_value
        current_slot = current_slot + i.next_slot
        current_state = i.next_state
    
    t = 0
    for c in slots:
        if c == 1:
            t += 1
    print("Part one:", t)


if __name__ == "__main__":
    main()

