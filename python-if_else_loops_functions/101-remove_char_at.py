#!/usr/bin/python3
def remove_char_at(str, n):
    removed = ""
    for i in range(len(str)):
        if i != n:
            removed = removed + str[i]
    return (removed)
