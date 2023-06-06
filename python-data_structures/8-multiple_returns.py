#!/usr/bin/python3
def multiple_returns(sentence):
    c = sentence[0]
    str_len = len(sentence) if sentence else None
    return str_len, c
