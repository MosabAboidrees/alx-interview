#!/usr/bin/python3
"""
N Queens Puzzle solver using backtracking
"""

import sys


def print_solution(solution):
    """Prints each solution in the required format"""
    print([[i, row.index(1)] for i, row in enumerate(solution)])


def is_safe(board, row, col, N):
    """Checks if placing a queen on board[row][col] is safe"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens_util(board, col, N):
    """Recursively tries to place queens on the board"""
    if col >= N:
        print_solution(board)
        return True
    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, N) or res
            board[i][col] = 0
    return res


def solve_nqueens(N):
    """Sets up the board and calls the utility function"""
    board = [[0] * N for _ in range(N)]
    solve_nqueens_util(board, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve_nqueens(N)
