"""
LeetCode Problem #1463: Cherry Pickup II

Problem Statement:
You are given a `rows x cols` matrix `grid` representing a field of cherries where `grid[i][j]` is the number of cherries that you can collect from the cell `(i, j)`.

You have two robots that can collect cherries for you:
- Robot #1 is located at the top-left corner `(0, 0)`, and
- Robot #2 is located at the top-right corner `(0, cols-1)`.

Return the maximum number of cherries collection using both robots by following the rules below:
1. From a cell `(i, j)`, Robot #1 can move to `(i + 1, j - 1)`, `(i + 1, j)`, or `(i + 1, j + 1)`.
2. From a cell `(i, j)`, Robot #2 can move to `(i + 1, j - 1)`, `(i + 1, j)`, or `(i + 1, j + 1)`.
3. When any robot passes through a cell, it collects all the cherries, and the cell becomes empty.
4. If both robots occupy the same cell, only one of them collects the cherries.
5. Both robots start at the first row and can move simultaneously. They cannot move outside the grid at any point.

Return the maximum number of cherries the two robots can collect.

Constraints:
- `rows == grid.length`
- `cols == grid[i].length`
- `2 <= rows, cols <= 70`
- `0 <= grid[i][j] <= 100`
"""

# Solution
from functools import lru_cache

def cherryPickup(grid):
    rows, cols = len(grid), len(grid[0])

    @lru_cache(None)
    def dp(row, col1, col2):
        # If either robot is out of bounds, return 0
        if col1 < 0 or col1 >= cols or col2 < 0 or col2 >= cols:
            return 0

        # Current cherries collected
        cherries = grid[row][col1]
        if col1 != col2:
            cherries += grid[row][col2]

        # If we are at the last row, return the cherries collected
        if row == rows - 1:
            return cherries

        # Move to the next row
        max_cherries = 0
        for new_col1 in [col1 - 1, col1, col1 + 1]:
            for new_col2 in [col2 - 1, col2, col2 + 1]:
                max_cherries = max(max_cherries, dp(row + 1, new_col1, new_col2))

        return cherries + max_cherries

    # Start the robots at (0, 0) and (0, cols - 1)
    return dp(0, 0, cols - 1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [3, 1, 1],
        [2, 5, 1],
        [1, 5, 5],
        [2, 1, 1]
    ]
    print(cherryPickup(grid1))  # Expected Output: 24

    # Test Case 2
    grid2 = [
        [1, 0, 0, 0, 0, 0, 1],
        [2, 0, 0, 0, 0, 3, 0],
        [2, 0, 9, 0, 0, 0, 0],
        [0, 3, 0, 5, 4, 0, 0],
        [1, 0, 2, 3, 0, 0, 6]
    ]
    print(cherryPickup(grid2))  # Expected Output: 28

    # Test Case 3
    grid3 = [
        [1, 1],
        [1, 1]
    ]
    print(cherryPickup(grid3))  # Expected Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function `dp(row, col1, col2)` is called for every combination of `row`, `col1`, and `col2`.
- There are `rows` rows and `cols * cols` possible combinations of `col1` and `col2`.
- For each state, we explore 9 possible moves (3 for `col1` and 3 for `col2`).
- Thus, the time complexity is O(rows * cols^2 * 9) = O(rows * cols^2).

Space Complexity:
- The space complexity is determined by the memoization table, which stores results for O(rows * cols^2) states.
- Thus, the space complexity is O(rows * cols^2).
"""

# Topic: Dynamic Programming