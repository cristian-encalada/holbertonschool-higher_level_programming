#!/usr/bin/python3
"""Task 12. Pascal's Triangle
"""


def pascal_triangle(n):
    """Return a list of lists of integers representing the Pascal’s triangle
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]  # Base case

    array = pascal_triangle(n - 1)  # Call pascal_triangle() using recursion
    prev_row = array[-1]
    row = [1]  # Start with 1

    for i in range(1, len(prev_row)):
        row.append(prev_row[i - 1] + prev_row[i])  # Calculate the sum

    row.append(1)  # End with 1
    array.append(row)

    return array
