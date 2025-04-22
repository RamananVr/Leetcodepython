"""
LeetCode Problem #463: Island Perimeter

Problem Statement:
You are given a 2D grid of integers `grid` where:
- `grid[i][j] == 1` represents land.
- `grid[i][j] == 0` represents water.

The grid is rectangular, with its width and height not exceeding 100. The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with a side length of 1. The island is connected horizontally or vertically.

Return the perimeter of the island.

Example:
Input: grid = [[0,1,0,0],
               [1,1,1,0],
               [0,1,0,0],
               [1,1,0,0]]
Output: 16

Constraints:
- `1 <= grid.length, grid[0].length <= 100`
- `grid[i][j]` is `0` or `1`.
"""

def islandPerimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.

    :param grid: List[List[int]] - 2D grid representing the map
    :return: int - perimeter of the island
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Land cell
                # Add 4 for the cell itself
                perimeter += 4

                # Subtract 1 for each adjacent land cell
                if r > 0 and grid[r - 1][c] == 1:  # Check top
                    perimeter -= 1
                if r < rows - 1 and grid[r + 1][c] == 1:  # Check bottom
                    perimeter -= 1
                if c > 0 and grid[r][c - 1] == 1:  # Check left
                    perimeter -= 1
                if c < cols - 1 and grid[r][c + 1] == 1:  # Check right
                    perimeter -= 1

    return perimeter

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[0, 1, 0, 0],
             [1, 1, 1, 0],
             [0, 1, 0, 0],
             [1, 1, 0, 0]]
    print(islandPerimeter(grid1))  # Output: 16

    # Test Case 2
    grid2 = [[1]]
    print(islandPerimeter(grid2))  # Output: 4

    # Test Case 3
    grid3 = [[1, 0]]
    print(islandPerimeter(grid3))  # Output: 4

    # Test Case 4
    grid4 = [[1, 1]]
    print(islandPerimeter(grid4))  # Output: 6

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through every cell in the grid once.
- If the grid has `m` rows and `n` columns, the time complexity is O(m * n).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""