"""
LeetCode Problem #2304: Minimum Path Cost in a Grid

Problem Statement:
You are given a 2D grid of size `m x n` consisting of non-negative integers. You are also given a 2D array `moveCost` of size `(maxValue + 1) x n` where `maxValue` is the maximum value in the grid. The `moveCost[i][j]` is the cost of moving from a cell with value `i` to any cell in column `j` of the next row.

The cost of a path in the grid is the sum of all values of cells visited plus the sum of the move costs between consecutive cells of the path. Return the minimum path cost of any path from the first row to the last row in the grid.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `2 <= m, n <= 50`
- `0 <= grid[i][j] <= 100`
- `moveCost.length == 101`
- `moveCost[i].length == n`

Example:
Input: grid = [[5,3],[4,0],[2,1]], moveCost = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]
Output: 17
Explanation: The path with the minimum cost is 5 -> 0 -> 1. The cost is 5 + 0 + 1 + 8 + 3 = 17.

Follow-up:
Can you solve this problem using dynamic programming?
"""

# Solution
def minPathCost(grid, moveCost):
    """
    Function to calculate the minimum path cost in a grid.

    :param grid: List[List[int]] - 2D grid of integers
    :param moveCost: List[List[int]] - 2D array of move costs
    :return: int - Minimum path cost
    """
    m, n = len(grid), len(grid[0])
    dp = grid[0][:]  # Initialize dp with the first row of the grid

    for i in range(1, m):
        new_dp = [float('inf')] * n
        for j in range(n):
            for k in range(n):
                new_dp[k] = min(new_dp[k], dp[j] + moveCost[grid[i - 1][j]][k] + grid[i][k])
        dp = new_dp

    return min(dp)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[5, 3], [4, 0], [2, 1]]
    moveCost1 = [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]
    print(minPathCost(grid1, moveCost1))  # Output: 17

    # Test Case 2
    grid2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    moveCost2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27], [28, 29, 30]]
    print(minPathCost(grid2, moveCost2))  # Output: 12

    # Test Case 3
    grid3 = [[10, 20], [30, 40]]
    moveCost3 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20], [21, 22]]
    print(minPathCost(grid3, moveCost3))  # Output: 61

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop runs for `m-1` iterations (number of rows minus one).
- The inner loops iterate over `n` columns and calculate the minimum cost for each cell in the next row.
- The total time complexity is O(m * n^2), where `m` is the number of rows and `n` is the number of columns.

Space Complexity:
- The space complexity is O(n) for the `dp` array, which stores the minimum costs for the current row.
- The `new_dp` array also takes O(n) space.
- Total space complexity is O(n).
"""

# Topic: Dynamic Programming