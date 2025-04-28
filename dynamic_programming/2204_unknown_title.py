"""
LeetCode Problem #2204: Minimum Path Cost in a Grid

Problem Statement:
You are given a 2D grid of integers `grid` and an integer array `moveCost` where `grid[i][j]` represents the cost of stepping on the cell `(i, j)` and `moveCost[k]` represents the cost of moving from a cell with value `k` to any cell in the next row.

You can start from any cell in the first row and move to any cell in the next row. Return the minimum path cost of traveling from the top row to the bottom row.

Constraints:
- `grid.length == m`
- `grid[i].length == n`
- `2 <= m, n <= 50`
- `0 <= grid[i][j] < moveCost.length`
- `1 <= moveCost.length <= 100`
- `1 <= moveCost[k] <= 100`
"""

# Solution
def minPathCost(grid, moveCost):
    """
    Calculate the minimum path cost in the grid.

    :param grid: List[List[int]], the grid of costs
    :param moveCost: List[int], the cost of moving between rows
    :return: int, the minimum path cost
    """
    m, n = len(grid), len(grid[0])
    dp = grid[0][:]  # Initialize dp with the first row costs

    for i in range(1, m):
        new_dp = [float('inf')] * n
        for j in range(n):
            for k in range(n):
                new_dp[k] = min(new_dp[k], dp[j] + moveCost[grid[i - 1][j]] + grid[i][k])
        dp = new_dp

    return min(dp)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    moveCost1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(minPathCost(grid1, moveCost1))  # Expected Output: 12

    # Test Case 2
    grid2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    moveCost2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(minPathCost(grid2, moveCost2))  # Expected Output: 12

    # Test Case 3
    grid3 = [[5, 3], [4, 0], [2, 1]]
    moveCost3 = [7, 1, 3, 2, 4, 10]
    print(minPathCost(grid3, moveCost3))  # Expected Output: 17

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop runs for `m - 1` iterations (number of rows minus 1).
- The inner loops iterate over `n` (number of columns) and `n` again for each cell.
- Therefore, the total time complexity is O(m * n^2).

Space Complexity:
- We use a `dp` array of size `n` to store the minimum costs for the current row.
- The space complexity is O(n).
"""

# Topic: Dynamic Programming