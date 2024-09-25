#!/usr/bin/python3
"""
Module to calculate the perimeter of an island
in a 2D grid
"""


def island_perimeter(grid):
    """
    Function that returns the perimeter of the island
    described in grid.

    Args:
    grid (list of lists): 2D grid, 0 represents water and 1 represents land.

    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Check if the current cell is land
                # Check the top
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                # Check the bottom
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                # Check the left
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                # Check the right
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
