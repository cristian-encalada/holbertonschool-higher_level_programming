#!/usr/bin/python3
"""Task 0. Read file
"""


def read_file(filename=""):
    """Read a text file (UTF8) and print it to stdout
    """
    with open(filename, 'r', encoding="utf-8") as file:
        content = file.read()
        print(content, end='')
