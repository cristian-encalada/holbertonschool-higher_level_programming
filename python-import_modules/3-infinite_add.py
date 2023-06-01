#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):  # Start at 1 to skip script name
            arg = sys.argv[i]
            result += int(arg)
    print(result)
