#!/usr/bin/python3
"""
Task 5. Text indentation
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    delimiters = {'.', '?', ':'}
    i = 0

    while i < len(text):
        if text[i] in delimiters:
            print(text[i] + "\n\n", end="")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        print(text[i], end="")
        i += 1
