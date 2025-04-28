"""
LeetCode Problem #2435: Paths in Matrix Whose Sum Is Divisible by K

Problem Statement:
You are given a 2D integer array `grid` of size `m x n` and an integer `k`. You need to find the number of paths in the grid such that the sum of the elements along the path is divisible by `k`. A path is defined as a sequence of cells starting from the top-left cell `(0, 0)` to the bottom-right cell `(m-1, n-1)` such that you can only move down or right at any point in time.

Return the number of such paths modulo `10^9 + 7`.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `0 <= grid[i][j] <= 100`
- `1 <= k <= 50`
"""

# Solution
def numberOfPaths(grid, k):
    MOD = 10**9 + 7
    m, n = len(grid), len(grid[0])
    
    # dp[i][j][r] represents the number of paths to cell (i, j) with a sum % k == r
    dp = [[[0] * k for _ in range(n)] for _ in range(m)]
    
    # Initialize the starting point
    dp[0][0][grid[0][0] % k] = 1
    
    for i in range(m):
        for j in range(n):
            for r in range(k):
                if dp[i][j][r] > 0:
                    # Move right
                    if j + 1 < n:
                        new_r = (r + grid[i][j + 1]) % k
                        dp[i][j + 1][new_r] = (dp[i][j + 1][new_r] + dp[i][j][r]) % MOD
                    # Move down
                    if i + 1 < m:
                        new_r = (r + grid[i + 1][j]) % k
                        dp[i + 1][j][new_r] = (dp[i + 1][j][new_r] + dp[i][j][r]) % MOD
    
    # The result is the number of paths to the bottom-right corner with sum % k == 0
    return dp[m - 1][n - 1][0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[5, 2, 4], [3, 0, 5], [0, 7, 2]]
    k1 = 3
    print(numberOfPaths(grid1, k1))  # Expected Output: 2

    # Test Case 2
    grid2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    k2 = 4
    print(numberOfPaths(grid2, k2))  # Expected Output: 10

    # Test Case 3
    grid3 = [[1, 2], [3, 4]]
    k3 = 2
    print(numberOfPaths(grid3, k3))  # Expected Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loops iterate over all cells in the grid, which is O(m * n).
- For each cell, we iterate over all possible remainders (0 to k-1), which is O(k).
- Thus, the total time complexity is O(m * n * k).

Space Complexity:
- The dp array has dimensions m x n x k, so the space complexity is O(m * n * k).
"""

# Topic: Dynamic Programming