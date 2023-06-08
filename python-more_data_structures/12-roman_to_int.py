#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    num = 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i, char in enumerate(roman_string):
        if i > 0 and d[char] > d[roman_string[i-1]]:
            num += d[char] - (d[roman_string[i-1]] * 2)
        else:
            num += d[char]
    return num
