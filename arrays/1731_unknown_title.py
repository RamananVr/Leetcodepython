"""
LeetCode Problem #1731: The Problem Statement

Problem Statement:
You are given a 2D grid of size m x n representing a map of land and water, where:
- '1' represents land
- '0' represents water

The grid is surrounded by water on all sides (i.e., there is a border of water around the grid). 
The grid is guaranteed to be rectangular.

Your task is to calculate the perimeter of the land in the grid. The perimeter is defined as the 
total length of the edges that are adjacent to water or the grid boundary.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- grid[i][j] is either '0' or '1'

Example:
Input: grid = [
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 1, 0, 0]
]
Output: 16

Explanation:
The perimeter is calculated by summing up all the edges of land cells that are adjacent to water or the grid boundary.
"""

# Solution
def islandPerimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.

    :param grid: List[List[int]] - 2D grid representing land and water
    :return: int - perimeter of the island
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Land cell
                # Check all four sides
                if r == 0 or grid[r - 1][c] == 0:  # Top
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:  # Bottom
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:  # Left
                    perimeter += 1
                if c == cols - 1 or grid[r][c + 1] == 0:  # Right
                    perimeter += 1

    return perimeter

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    print(islandPerimeter(grid1))  # Output: 16

    # Test Case 2
    grid2 = [
        [1]
    ]
    print(islandPerimeter(grid2))  # Output: 4

    # Test Case 3
    grid3 = [
        [1, 0],
        [1, 0]
    ]
    print(islandPerimeter(grid3))  # Output: 6

    # Test Case 4
    grid4 = [
        [1, 1],
        [1, 1]
    ]
    print(islandPerimeter(grid4))  # Output: 8

"""
Time and Space Complexity Analysis:

Time Complexity:
The algorithm iterates through every cell in the grid once. For each cell, it performs a constant amount of work 
to check its neighbors. Therefore, the time complexity is O(m * n), where m is the number of rows and n is the 
number of columns in the grid.

Space Complexity:
The algorithm uses a constant amount of extra space, as it only stores the perimeter variable and the dimensions 
of the grid. Therefore, the space complexity is O(1).

Topic: Arrays
"""