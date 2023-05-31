#!/usr/bin/python3
def islower(c):
    return ord(c) in range(ord('a'), ord('z') + 1)


def uppercase(str):
    for c in str:
        if islower(c):
            c = chr(ord(c) - 32)
        print(c, end='')
    print()
