"""
LeetCode Problem #2658: Maximum Number of Fish in a Grid

Problem Statement:
You are given a 2D grid of integers `grid` where:
- `grid[i][j]` represents the number of fish at cell `(i, j)`.
- A cell with `grid[i][j] == 0` represents water, and a cell with `grid[i][j] > 0` represents land.

You can move in four directions: up, down, left, and right. You can start at any land cell and move to another land cell if they are adjacent (share a side). You can keep moving as long as you are on land.

Return the maximum number of fish you can collect starting from any land cell.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10^2`
- `0 <= grid[i][j] <= 10^4`

"""

from typing import List

def findMaxFish(grid: List[List[int]]) -> int:
    def dfs(x, y):
        # If out of bounds or water cell, return 0
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
            return 0
        
        # Collect fish at the current cell
        fish = grid[x][y]
        # Mark the cell as visited by setting it to 0
        grid[x][y] = 0
        
        # Explore all four directions
        fish += dfs(x + 1, y)  # Down
        fish += dfs(x - 1, y)  # Up
        fish += dfs(x, y + 1)  # Right
        fish += dfs(x, y - 1)  # Left
        
        return fish

    m, n = len(grid), len(grid[0])
    max_fish = 0

    # Iterate through all cells in the grid
    for i in range(m):
        for j in range(n):
            if grid[i][j] > 0:  # Start DFS from any land cell
                max_fish = max(max_fish, dfs(i, j))
    
    return max_fish

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [0, 2, 0],
        [4, 0, 3],
        [1, 0, 0]
    ]
    print(findMaxFish(grid1))  # Output: 7 (4 + 3)

    # Test Case 2
    grid2 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    print(findMaxFish(grid2))  # Output: 0 (No land cells)

    # Test Case 3
    grid3 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(findMaxFish(grid3))  # Output: 45 (All cells are connected)

    # Test Case 4
    grid4 = [
        [10, 0, 20],
        [0, 0, 0],
        [30, 0, 40]
    ]
    print(findMaxFish(grid4))  # Output: 40 (Largest isolated land cell)

"""
Time Complexity:
- The DFS function visits each cell at most once. In the worst case, we may visit all `m * n` cells.
- Therefore, the time complexity is O(m * n).

Space Complexity:
- The space complexity is O(m * n) in the worst case due to the recursion stack in DFS.

Topic: Graph Traversal (DFS)
"""