#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('too far')
            result = a ** b
            result += i
        except Exception:
            result = a + b
        finally:
            return result
