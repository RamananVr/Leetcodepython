"""
LeetCode Problem #2936: Problem Statement

Given a 2D grid of size `m x n` where each cell contains an integer, your task is to find the maximum sum of any path from the top-left corner to the bottom-right corner of the grid. You can only move either down or right at any point in time.

Write a function `maxPathSum(grid: List[List[int]]) -> int` that takes the grid as input and returns the maximum sum of any path.

Constraints:
- `1 <= m, n <= 100`
- `-1000 <= grid[i][j] <= 1000`

Example:
Input: grid = [[5, 3, 2], [1, 4, 1], [1, 5, 3]]
Output: 16
Explanation: The path 5 → 3 → 4 → 5 → 3 gives the maximum sum of 16.
"""

from typing import List

def maxPathSum(grid: List[List[int]]) -> int:
    """
    Function to calculate the maximum path sum in a grid.
    """
    m, n = len(grid), len(grid[0])
    
    # Create a DP table to store the maximum path sums
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the top-left corner
    dp[0][0] = grid[0][0]
    
    # Fill the first row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    
    # Fill the first column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    
    # Fill the rest of the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    
    # The bottom-right corner contains the maximum path sum
    return dp[m - 1][n - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[5, 3, 2], [1, 4, 1], [1, 5, 3]]
    print(maxPathSum(grid1))  # Output: 16

    # Test Case 2
    grid2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(maxPathSum(grid2))  # Output: 29

    # Test Case 3
    grid3 = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
    print(maxPathSum(grid3))  # Output: -21

    # Test Case 4
    grid4 = [[1]]
    print(maxPathSum(grid4))  # Output: 1

    # Test Case 5
    grid5 = [[1, 2], [1, 1]]
    print(maxPathSum(grid5))  # Output: 4

"""
Time Complexity:
- The algorithm iterates through each cell of the grid once, so the time complexity is O(m * n), where m is the number of rows and n is the number of columns.

Space Complexity:
- The space complexity is O(m * n) due to the DP table. However, this can be optimized to O(n) if we only keep the current and previous rows in memory.

Topic: Dynamic Programming (DP)
"""