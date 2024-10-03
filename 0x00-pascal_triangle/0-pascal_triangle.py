#!/usr/bin/python3
"""A script to determine Pascal's triangle using recursion"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n
    """
    if n <= 0:
        return []

    # Recursive function to generate a single row in Pascal's triangle
    def generate_row(previous_row):
        row_length = len(previous_row) + 1
        new_row = [1] * row_length  # Initialize row with 1s
        for i in range(1, row_length - 1):
            # Fill inner values
            new_row[i] = previous_row[i - 1] + previous_row[i]
        return new_row

    # Base case: the first row is always [1]
    triangle = [[1]]

    # Generate each row recursively
    for i in range(1, n):
        # Generate next row from previous
        next_row = generate_row(triangle[i - 1])
        triangle.append(next_row)

    return triangle
