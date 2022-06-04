#!/usr/bin/env python3


import re


def increment(s):
    l = list(reversed(s))
    carry = True
    for i in range(len(l)):
        if carry:
            l[i] = chr(ord(l[i])+1)
            if l[i] == "{":
                l[i] = "a"
                carry = True
            else:
                carry = False
        else:
            break
    return "".join(reversed(l))


def contains_bad_characters(password):
    for c in ("i", "o", "l"):
        if c in password:
            return True


def has_unique_pairs(password):
    return len(set(re.findall(r"([a-z])\1", password))) >= 2


def has_incrementing_triplet(password):
    for i in range(0, len(password)-2):
        s = [ord(e) for e in password[i:i+3]]
        if s[1] == s[0]+1 and s[2] == s[1]+1:
            return True


def valid(password):
    if contains_bad_characters(password):
        return False
    if not has_unique_pairs(password):
        return False
    if not has_incrementing_triplet(password):
        return False
    return True


if __name__ == "__main__":

    password = "vzbxkghb"
    while True:
        password = increment(password)
        if valid(password):
            break
    print("Part one:", password)

    while True:
        password = increment(password)
        if valid(password):
            break
    print("Part two:", password)
