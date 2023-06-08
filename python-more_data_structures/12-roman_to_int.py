def roman_to_int(roman_string):
    num = 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for char in roman_string:
        num += d[char]
    return num
