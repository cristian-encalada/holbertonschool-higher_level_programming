#!/usr/bin/python3
def text_indentation(text):
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
