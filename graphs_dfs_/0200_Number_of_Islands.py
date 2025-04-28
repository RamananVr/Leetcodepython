"""
LeetCode Problem #200: Number of Islands

Problem Statement:
Given an `m x n` 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is '0' or '1'.
"""

def numIslands(grid):
    """
    Function to count the number of islands in a given grid.

    :param grid: List[List[str]] - 2D grid of '1's (land) and '0's (water)
    :return: int - Number of islands
    """
    if not grid:
        return 0

    def dfs(i, j):
        # If out of bounds or at a water cell, return
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        # Mark the current cell as visited
        grid[i][j] = '0'
        # Explore all 4 directions
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    num_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':  # Found an unvisited land cell
                num_islands += 1
                dfs(i, j)  # Perform DFS to mark the entire island
    return num_islands

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(numIslands(grid1))  # Output: 1

    # Test Case 2
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(numIslands(grid2))  # Output: 3

    # Test Case 3
    grid3 = [
        ["1", "0", "1", "0", "1"],
        ["0", "0", "0", "0", "0"],
        ["1", "0", "1", "0", "1"]
    ]
    print(numIslands(grid3))  # Output: 5

"""
Time Complexity:
- The grid is traversed once, and each cell is visited at most once during the DFS.
- Therefore, the time complexity is O(m * n), where m is the number of rows and n is the number of columns.

Space Complexity:
- The space complexity is O(m * n) in the worst case due to the recursion stack when the grid is filled with land.

Topic: Graphs (DFS)
"""