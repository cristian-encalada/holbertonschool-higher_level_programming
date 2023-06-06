#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = matrix.copy()
    squares = [[x**2 for x in row] for row in squares]
    return squares
