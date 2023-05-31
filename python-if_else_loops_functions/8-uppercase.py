#!/usr/bin/python3
def uppercase(str):
    converted = ""
    for c in str:
        if 'a' <= c <= 'z':
            c = chr(ord(c) + ord('A') - ord('a'))
        converted += c
    print(converted)
