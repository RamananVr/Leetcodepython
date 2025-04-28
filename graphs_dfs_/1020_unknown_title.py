"""
LeetCode Problem #1020: Number of Enclaves

Problem Statement:
You are given an `m x n` binary matrix `grid`, where `0` represents a sea cell and `1` represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in `grid` for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:
Input: grid = [[0,0,0,0],
               [1,0,1,0],
               [0,1,1,0],
               [0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and cannot walk off the boundary.

Example 2:
Input: grid = [[0,1,1,0],
               [0,0,1,0],
               [0,0,1,0],
               [0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 500`
- `grid[i][j]` is either `0` or `1`.

"""

from typing import List

def numEnclaves(grid: List[List[int]]) -> int:
    def dfs(x, y):
        # If out of bounds or at a sea cell, return
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
            return
        # Mark the cell as visited by setting it to 0
        grid[x][y] = 0
        # Explore all 4 directions
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

    m, n = len(grid), len(grid[0])

    # Step 1: Remove all land cells connected to the boundary
    for i in range(m):
        for j in range(n):
            if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == 1:
                dfs(i, j)

    # Step 2: Count the remaining land cells
    return sum(grid[i][j] == 1 for i in range(m) for j in range(n))


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[0, 0, 0, 0],
             [1, 0, 1, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0]]
    print(numEnclaves(grid1))  # Output: 3

    # Test Case 2
    grid2 = [[0, 1, 1, 0],
             [0, 0, 1, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 0]]
    print(numEnclaves(grid2))  # Output: 0

    # Test Case 3
    grid3 = [[1, 1, 1],
             [1, 0, 1],
             [1, 1, 1]]
    print(numEnclaves(grid3))  # Output: 1

    # Test Case 4
    grid4 = [[0, 0, 0],
             [0, 1, 0],
             [0, 0, 0]]
    print(numEnclaves(grid4))  # Output: 1


"""
Time Complexity Analysis:
- The DFS function visits each cell at most once. Therefore, the time complexity is O(m * n), where m is the number of rows and n is the number of columns in the grid.

Space Complexity Analysis:
- The space complexity is O(m * n) in the worst case due to the recursion stack in DFS.

Topic: Graphs (DFS)
"""