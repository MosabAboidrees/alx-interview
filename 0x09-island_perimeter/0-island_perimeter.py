#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.
    Args:
        grid (list of list of ints):
        A list of lists where 1 represents land
        and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4

                # Subtract 2 for each adjacent land cell
                # (vertical and horizontal)
                if row > 0 and grid[row - 1][col] == 1:  # Check cell above
                    perimeter -= 2
                    # Check cell to the left
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
