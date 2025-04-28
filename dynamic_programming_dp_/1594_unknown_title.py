"""
LeetCode Problem #1594: Maximum Non-Negative Product in a Matrix

Problem Statement:
You are given a `m x n` matrix `grid`. Your task is to find the maximum non-negative product 
of a path in the matrix. The path can start from any cell in the first row and end at any cell 
in the last row. You can only move down or right at any point in time.

Return the maximum non-negative product modulo 10^9 + 7. If the maximum product is negative, 
return -1.

Constraints:
- `1 <= m, n <= 15`
- `-100 <= grid[i][j] <= 100`

Example:
Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
Output: -1
Explanation: It's not possible to get a non-negative product in the path.

Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
Output: 8
Explanation: The maximum non-negative product is obtained by the path 1 → 1 → 3 → 1.

Input: grid = [[1,3],[0,-4]]
Output: 0
Explanation: The maximum non-negative product is obtained by the path 1 → 0.

Topic: Dynamic Programming (DP)
"""

from typing import List

def maxProductPath(grid: List[List[int]]) -> int:
    MOD = 10**9 + 7
    m, n = len(grid), len(grid[0])
    
    # Initialize two DP matrices to store the max and min product at each cell
    max_dp = [[0] * n for _ in range(m)]
    min_dp = [[0] * n for _ in range(m)]
    
    # Base case: the starting cell
    max_dp[0][0] = min_dp[0][0] = grid[0][0]
    
    # Fill the first row
    for j in range(1, n):
        max_dp[0][j] = min_dp[0][j] = max_dp[0][j - 1] * grid[0][j]
    
    # Fill the first column
    for i in range(1, m):
        max_dp[i][0] = min_dp[i][0] = max_dp[i - 1][0] * grid[i][0]
    
    # Fill the rest of the DP tables
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] >= 0:
                max_dp[i][j] = max(max_dp[i - 1][j], max_dp[i][j - 1]) * grid[i][j]
                min_dp[i][j] = min(min_dp[i - 1][j], min_dp[i][j - 1]) * grid[i][j]
            else:
                max_dp[i][j] = min(min_dp[i - 1][j], min_dp[i][j - 1]) * grid[i][j]
                min_dp[i][j] = max(max_dp[i - 1][j], max_dp[i][j - 1]) * grid[i][j]
    
    # The result is the maximum product in the bottom-right corner
    result = max_dp[m - 1][n - 1]
    return result % MOD if result >= 0 else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]
    print(maxProductPath(grid1))  # Output: -1

    # Test Case 2
    grid2 = [[1, -2, 1], [1, -2, 1], [3, -4, 1]]
    print(maxProductPath(grid2))  # Output: 8

    # Test Case 3
    grid3 = [[1, 3], [0, -4]]
    print(maxProductPath(grid3))  # Output: 0

    # Test Case 4
    grid4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(maxProductPath(grid4))  # Output: 2016

"""
Time Complexity:
- O(m * n), where m is the number of rows and n is the number of columns in the grid.
- We iterate through each cell of the grid once to compute the DP values.

Space Complexity:
- O(m * n), for the two DP matrices (max_dp and min_dp) of size m x n.

Topic: Dynamic Programming (DP)
"""