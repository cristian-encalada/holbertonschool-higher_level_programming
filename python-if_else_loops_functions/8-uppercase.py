#!/usr/bin/python3
def islower(c):
    return ord(c) in range(ord('a'), ord('z') + 1)


def uppercase(str):
    converted = ""
    for c in str:
        if islower(c):
            c = chr(ord(c) + ord('A') - ord('a'))
        converted += c
    print(converted)
