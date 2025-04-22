"""
LeetCode Problem #694: Number of Distinct Islands

Problem Statement:
You are given an `m x n` binary matrix `grid`. An island is a group of `1`s (representing land) connected 4-directionally (horizontal or vertical). 
You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.

Example 1:
Input: grid = [
  [1,1,0,0,0],
  [1,1,0,0,0],
  [0,0,0,1,1],
  [0,0,0,1,1]
]
Output: 1

Example 2:
Input: grid = [
  [1,1,0,1,1],
  [1,0,0,0,0],
  [0,0,0,0,1],
  [1,1,0,1,1]
]
Output: 3

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `grid[i][j]` is either `0` or `1`.
"""

from typing import List

def numDistinctIslands(grid: List[List[int]]) -> int:
    def dfs(x, y, origin_x, origin_y):
        # Mark the cell as visited
        grid[x][y] = 0
        # Record the relative position of the cell
        shape.add((x - origin_x, y - origin_y))
        # Explore all 4 directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                dfs(nx, ny, origin_x, origin_y)

    # Initialize variables
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    unique_shapes = set()

    # Iterate through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:  # Found an unvisited land cell
                shape = set()
                dfs(i, j, i, j)  # Perform DFS to record the shape
                unique_shapes.add(frozenset(shape))  # Add the shape to the set of unique shapes

    return len(unique_shapes)

# Example Test Cases
if __name__ == "__main__":
    grid1 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]
    ]
    print(numDistinctIslands(grid1))  # Output: 1

    grid2 = [
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1]
    ]
    print(numDistinctIslands(grid2))  # Output: 3

    grid3 = [
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ]
    print(numDistinctIslands(grid3))  # Output: 2

# Time Complexity Analysis:
# - The DFS function visits each cell of the grid at most once. Therefore, the time complexity is O(m * n), 
#   where m is the number of rows and n is the number of columns in the grid.
# - The space complexity is O(m * n) in the worst case due to the recursion stack and the storage of shapes.

# Space Complexity Analysis:
# - The space complexity is O(m * n) due to the storage of the shapes in the `unique_shapes` set and the recursion stack.

# Topic: Graphs, Depth-First Search (DFS)