#!/usr/bin/python3
"""
Task 6. Matrix multiplication
"""


def matrix_mul(m_a, m_b):
    """
    Multiply 2 matrices
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be lists of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be lists of lists")
    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_a can't be empty")

    rows_a = len(m_a)
    cols_a = len(m_a[0])
    rows_b = len(m_b)
    cols_b = len(m_b[0])

    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
