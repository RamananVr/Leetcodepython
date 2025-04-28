"""
LeetCode Problem #64: Minimum Path Sum

Problem Statement:
Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.

You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
Explanation: Because the path 1 → 2 → 3 → 6 minimizes the sum.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 200`
- `0 <= grid[i][j] <= 100`
"""

# Clean, Correct Python Solution
def minPathSum(grid):
    """
    Finds the minimum path sum from top-left to bottom-right in a grid.

    :param grid: List[List[int]] - 2D grid of non-negative integers
    :return: int - Minimum path sum
    """
    m, n = len(grid), len(grid[0])
    
    # Initialize the DP table
    dp = [[0] * n for _ in range(m)]
    
    # Base case: Top-left corner
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
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    
    # Return the value at the bottom-right corner
    return dp[m - 1][n - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(minPathSum(grid1))  # Output: 7

    # Test Case 2
    grid2 = [[1, 2, 3], [4, 5, 6]]
    print(minPathSum(grid2))  # Output: 12

    # Test Case 3
    grid3 = [[1]]
    print(minPathSum(grid3))  # Output: 1

    # Test Case 4
    grid4 = [[1, 2], [1, 1]]
    print(minPathSum(grid4))  # Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through each cell in the grid once.
- There are `m * n` cells in the grid.
- Therefore, the time complexity is O(m * n).

Space Complexity:
- The algorithm uses a DP table of size `m x n`.
- Therefore, the space complexity is O(m * n).
- Note: If we optimize the space by using a single row or column, the space complexity can be reduced to O(min(m, n)).
"""

# Topic: Dynamic Programming