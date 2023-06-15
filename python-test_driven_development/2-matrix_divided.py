#!/usr/bin/python3
"""
Task 1. Divide a matrix
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div
    """
    if any(not all(isinstance(i, (int, float)) for i in n) for n in matrix):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    """Use of lambda function and list comprehension"""
    new_matrix = [list(map(lambda x: round(x / div, 2), n)) for n in matrix]
    return new_matrix
