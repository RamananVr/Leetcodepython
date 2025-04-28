"""
LeetCode Problem #2328: Number of Increasing Paths in a Grid

Problem Statement:
You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions (up, down, left, right). Return the number of strictly increasing paths in the grid such that you can start and end at any cell. Since the answer may be very large, return it modulo 10^9 + 7.

A path is strictly increasing if and only if each subsequent cell in the path has a value strictly greater than the previous cell.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 1000
- 1 <= grid[i][j] <= 10^5
"""

from functools import lru_cache

def countPaths(grid):
    """
    Function to count the number of strictly increasing paths in a grid.

    :param grid: List[List[int]] - 2D grid of integers
    :return: int - Number of strictly increasing paths modulo 10^9 + 7
    """
    MOD = 10**9 + 7
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    @lru_cache(None)
    def dfs(x, y):
        # Start with 1 because the cell itself is a valid path
        count = 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > grid[x][y]:
                count += dfs(nx, ny)
                count %= MOD
        return count

    result = 0
    for i in range(m):
        for j in range(n):
            result += dfs(i, j)
            result %= MOD

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 1], [3, 4]]
    print(countPaths(grid1))  # Expected Output: 8

    # Test Case 2
    grid2 = [[1], [2], [3]]
    print(countPaths(grid2))  # Expected Output: 6

    # Test Case 3
    grid3 = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
    print(countPaths(grid3))  # Expected Output: 45

    # Test Case 4
    grid4 = [[1, 2], [3, 4]]
    print(countPaths(grid4))  # Expected Output: 10

"""
Time Complexity:
- The function uses memoization to avoid redundant calculations. Each cell is visited once, and for each cell, we explore up to 4 directions.
- Let m = number of rows, n = number of columns. The time complexity is O(m * n).

Space Complexity:
- The space complexity is O(m * n) due to the memoization cache and the recursion stack.

Topic: Dynamic Programming (DP), Depth-First Search (DFS), Memoization
"""