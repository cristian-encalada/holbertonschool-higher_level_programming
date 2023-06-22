#!/usr/bin/python3
"""Task 2. Append to a file
"""


def append_write(filename="", text=""):
    """Append a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        content = f.write(text)
        return len(text)
