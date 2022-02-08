#!/usr/bin/env python


import re

from more_itertools import windowed


def read_input(name):
    return [line.strip() for line in open(name).readlines()]


def is_abba_sequence(s):
    return s[0] != s[1] and s[0] == s[3] and s[1] == s[2]


def supernet_sequences(address):
    return re.split(r'\[\w+\]', address)


def hypernet_sequences(address):
    return re.findall(r'\[(\w+)\]', address)


def contains_abba_sequences(parts):
    for part in parts:
        for s in windowed(part, 4):
            if is_abba_sequence(s):
                return True
    return False


def is_aba_sequence(s):
    return s[0] != s[1] and s[0] == s[2]


def aba_sequences(parts):
    for part in parts:
        for s in windowed(part, 3):
            if is_aba_sequence(s):
                yield "".join(s)


def supports_tls(address):
    return contains_abba_sequences(supernet_sequences(address)) \
        and not contains_abba_sequences(hypernet_sequences(address))


def aba2bab(s):
    return s[1] + s[0] + s[1]


def supports_ssl(address):
    abas = list(aba_sequences(supernet_sequences(address)))
    babs = list(aba_sequences(hypernet_sequences(address)))
    for aba in abas:
        if aba2bab(aba) in babs:
            return True
    return False


if __name__ == "__main__":
    print("Part one:", sum(supports_tls(address) for address in read_input("day7.input")))
    print("Part two:", sum(supports_ssl(address) for address in read_input("day7.input")))
