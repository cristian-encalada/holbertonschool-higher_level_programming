#!/usr/bin/python3
def multiple_returns(sentence):
    c = sentence[0] if sentence else None
    str_len = len(sentence) if sentence else 0
    return str_len, c
