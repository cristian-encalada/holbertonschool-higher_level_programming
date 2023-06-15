#!/usr/bin/python3
try:
    result = int(float('-inf'))
except OverflowError as e:
    print("Error type:", type(e).__name__)
    print("Error message:", str(e))
