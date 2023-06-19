#!/usr/bin/python3
""" Task 11. N queens
"""
import sys


def is_safe(board, row, col):
    """ Check if a queen can be placed at the given position
       without attacking any other queens on the board
    """
    # Check the current column
    for i in range(row):
        if board[i] == col:
            return False

    # Check the upper-left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check the upper-right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row):
    """ Solve the N Queens problem recursively using backtracking
    """

    if row == N:
        # All queens have been placed, print the solution
        print_solution(board)
        return

    for col in range(N):
        if is_safe(board, row, col):
            # Place a queen at the current position
            board[row] = col
            solve_nqueens(board, row + 1)

            # Backtrack and remove the queen from the current position
            board[row] = -1


def print_solution(board):
    """ Print the solution in the format [[row, col], [row, col], ...]
    """
    solution = [[row, col] for row, col in enumerate(board)]
    print(solution)


def nqueens(N):
    """ Check if N is a valid integer
    """
    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board with -1 (no queens placed yet)
    board = [-1] * N

    # Solve the N Queens problem
    solve_nqueens(board, 0)


if __name__ == "__main__":
    # Check the number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command-line argument
    N = int(sys.argv[1])

    nqueens(N)
