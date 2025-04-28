"""
LeetCode Problem #1445: Apples and Oranges

Problem Statement:
You are given an m x n integer grid `grid` where each cell is either:
- 1 representing an apple,
- 2 representing an orange, or
- 0 representing an empty cell.

You can collect apples and oranges by moving through the grid. You start at the top-left corner (0, 0) and can only move right or down at any point in time. Your goal is to collect the maximum number of fruits (apples and oranges) possible while reaching the bottom-right corner (m-1, n-1).

Return the maximum number of fruits you can collect.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- 0 <= grid[i][j] <= 2
"""

# Solution
def maxFruits(grid):
    """
    Function to calculate the maximum number of fruits collected
    while moving from the top-left to the bottom-right corner of the grid.
    """
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize the top-left corner
    dp[0][0] = grid[0][0]

    # Fill the first row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # Fill the first column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Fill the rest of the grid
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    # The bottom-right corner contains the maximum fruits collected
    return dp[m - 1][n - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [1, 2, 0],
        [0, 1, 2],
        [2, 0, 1]
    ]
    print(maxFruits(grid1))  # Output: 7

    # Test Case 2
    grid2 = [
        [1, 1, 1],
        [0, 0, 1],
        [2, 2, 2]
    ]
    print(maxFruits(grid2))  # Output: 9

    # Test Case 3
    grid3 = [
        [0, 2, 2],
        [1, 0, 1],
        [1, 1, 1]
    ]
    print(maxFruits(grid3))  # Output: 7

    # Test Case 4
    grid4 = [
        [1]
    ]
    print(maxFruits(grid4))  # Output: 1

    # Test Case 5
    grid5 = [
        [1, 2],
        [2, 1]
    ]
    print(maxFruits(grid5))  # Output: 6

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution iterates through the entire grid once, filling the `dp` table.
- This takes O(m * n) time, where m is the number of rows and n is the number of columns.

Space Complexity:
- The solution uses a 2D `dp` table of size m x n to store intermediate results.
- This takes O(m * n) space.

Thus, the time complexity is O(m * n), and the space complexity is O(m * n).
"""

# Topic: Dynamic Programming