#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for num in row:  # row[-1] is the last element of the current row
                print("{:d}".format(num), end=' ' if num < row[-1] else '')
            print()
