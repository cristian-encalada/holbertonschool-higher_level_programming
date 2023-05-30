#!/usr/bin/python3
# end='' avoids inserting a newline after each printed character
for lc_letter in range(97, 123):
    if lc_letter != 101 and lc_letter != 113:
        print("{:c}".format(lc_letter), end='')
