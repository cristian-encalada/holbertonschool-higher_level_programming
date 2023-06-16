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
    result = ''
    skip_space = True

    for char in text:
        if char == ' ' and skip_space:
            continue

        result += char
        skip_space = False

        if char in delimiters:
            result += '\n\n'
            skip_space = True

    print(result)
