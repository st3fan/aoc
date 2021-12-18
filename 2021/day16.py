#!/usr/bin/env python3


import functools
import operator

from bitstring import ConstBitStream


class Packet:
    def __init__(self, bs):
        self.version = bs.read("uint:3")
        self.type = bs.read("uint:3")
    def value(self):
        raise Exception("value not implemented")


class LiteralPacket(Packet):
    def __init__(self, bs):
        super().__init__(bs)
        group = bs.read("uint:5")
        self._value = group & 0b1111
        while group & 0b10000:
            group = bs.read("uint:5")
            self._value <<= 4
            self._value |= (group & 0b1111)
    def value(self):
        return self._value


class OperatorPacket(Packet):
    def __init__(self, bs):
        super().__init__(bs)
        self.subpackets = []
        length_type = bs.read("uint:1")
        if length_type == 1:
            length = bs.read("uint:11")
            for _ in range(length):
                self.subpackets.append(read_packet(bs))
        else:
            length = bs.read("uint:15")
            end_pos = bs.pos + length
            while bs.pos < end_pos:
                self.subpackets.append(read_packet(bs))


class SumPacket(OperatorPacket):
    def value(self):
        return sum(p.value() for p in self.subpackets)


class ProductPacket(OperatorPacket):
    def value(self):
        return functools.reduce(operator.mul, [p.value() for p in self.subpackets])


class MinimumPacket(OperatorPacket):
    def value(self):
        return min(p.value() for p in self.subpackets)


class MaximumPacket(OperatorPacket):
    def value(self):
        return max(p.value() for p in self.subpackets)


class GreaterThanPacket(OperatorPacket):
    def value(self):
        return int(self.subpackets[0].value() > self.subpackets[1].value())


class LessThanPacket(OperatorPacket):
    def value(self):
        return int(self.subpackets[0].value() < self.subpackets[1].value())


class EqualToPacket(OperatorPacket):
    def value(self):
        return int(self.subpackets[0].value() == self.subpackets[1].value())


def read_packet(bs):
    _, type = bs.peeklist(["uint:3", "uint:3"])
    match type:
        case 0:
            return SumPacket(bs)
        case 1:
            return ProductPacket(bs)
        case 2:
            return MinimumPacket(bs)
        case 3:
            return MaximumPacket(bs)
        case 4:
            return LiteralPacket(bs)
        case 5:
            return GreaterThanPacket(bs)
        case 6:
            return LessThanPacket(bs)
        case 7:
            return EqualToPacket(bs)
        case _:
            raise Exception(f"Unknown packet type {type}")


def load_transmission():
    bs = ConstBitStream(bytes=bytes.fromhex(open("day16.input").read().strip()))
    return read_packet(bs)


def packet_versions(tr):
    yield tr.version
    if isinstance(tr, OperatorPacket):
        for subpacket in tr.subpackets:
            yield from packet_versions(subpacket)

def part1():
    tr = load_transmission()
    return sum(packet_versions(tr))


def part2():
    tr = load_transmission()
    return tr.value()


if __name__ == "__main__":
    print("Part one:", part1())
    print("Part two:", part2())

