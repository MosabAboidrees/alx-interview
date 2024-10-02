#!/usr/bin/python3
"""A script to determine Pascal's triangle for any number"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n
    """
    triangle = []  # Initialize the triangle as an empty list

    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return triangle

    # Loop through each level (row) of the triangle
    for row_number in range(n):
        current_row = []  # Initialize the current row

        # Loop through each element (column) in the current row
        for col_number in range(row_number + 1):
            # The first and last elements of each row are always 1
            if col_number == 0 or col_number == row_number:
                current_row.append(1)
            else:
                # Compute the inner values by adding elements from the previous row
                current_row.append(
                    triangle[row_number - 1][col_number - 1] + 
                    triangle[row_number - 1][col_number]
                )

        # Append the current row to the triangle
        triangle.append(current_row)

    # Return the final triangle
    return triangle
