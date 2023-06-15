#!/usr/bin/python3
try:
    result = int(float('inf'))
except OverflowError as e:
    print("Error type:", type(e).__name__)
    print("Error message:", str(e))
try:
    result = int(float('-inf'))
except OverflowError as e:
    print("Error type:", type(e).__name__)
    print("Error message:", str(e))
try:
    result = int(float('NaN'))
except OverflowError as e:
    print("Error type:", type(e).__name__)
    print("Error message:", str(e))
