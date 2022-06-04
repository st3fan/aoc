#!/usr/bin/env python3


import hashlib


INPUT = "bgvyzdsv"


def main():
    
    # Part 1

    for i in range(1, 999999):
        if hashlib.md5(f"{INPUT}{i}".encode('ascii')).hexdigest().startswith("00000"):
            break
    print("Part one:", i)

    for i in range(1, 999999999):
        if hashlib.md5(f"{INPUT}{i}".encode('ascii')).hexdigest().startswith("000000"):
            break
    print("Part two:", i)


if __name__ == "__main__":
    main()

