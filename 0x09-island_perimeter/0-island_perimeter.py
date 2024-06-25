#!/usr/bin/python3
"""
handling 2D arrays/lists
"""


def island_perimeter(grid):
    """
    function calculates the perimeter of an island
    """
    perimeter = 0
    connection = 0
    row_len = len(grid)
    col_len = len(grid[0])
    for row in range(0, row_len):
        for col in range(0, col_len):
            # we check if the current cell is a land cell
            # we add 4 to perimeter
            if grid[row][col] == 1:
                perimeter += 4
                # we check if the cell has a neighbour at the top
                # if it does, we increment the connection by 1
                if row > 0 and grid[row - 1][col] == 1:
                    connection += 1
                # we check if the cell has a neighbour at the left
                # if it does, we increment the connection by 1
                if col > 0 and grid[row][col - 1] == 1:
                    connection += 1
    # connection is * 2 since it is accounted twice
    return perimeter - (connection * 2)

# another solution I could use
    # for row in range(len(grid)):
    #     for col in range(len(grid[row])):
    #         if grid[row][col] == 1:
    #             if row == 0 or grid[row - 1][col] == 0:
    #                 perimeter += 1
    #             if row == len(grid) - 1 or grid[row + 1][col] == 0:
    #                 perimeter += 1
    #             if col == 0 or grid[row][col - 1] == 0:
    #                 perimeter += 1
    #             if col == len(grid[row]) - 1 or grid[row][col + 1] == 0:
    #                 perimeter += 1
    # return perimeter
