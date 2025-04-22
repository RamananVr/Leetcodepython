"""
LeetCode Problem #980: Unique Paths III

Problem Statement:
You are given an `m x n` integer array `grid` where `grid[i][j]` could be:
- `1` representing the starting square. There is exactly one starting square.
- `2` representing the ending square. There is exactly one ending square.
- `0` representing empty squares we can walk over.
- `-1` representing obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, 
that walk over every non-obstacle square exactly once.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 20`
- `grid[i][j]` is either `-1`, `0`, `1`, or `2`.
- There is exactly one starting square and one ending square.
"""

from typing import List

def uniquePathsIII(grid: List[List[int]]) -> int:
    def dfs(x, y, remaining):
        # If out of bounds or on an obstacle, return 0
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == -1:
            return 0
        
        # If we reach the end square
        if grid[x][y] == 2:
            # Check if all non-obstacle squares have been visited
            return 1 if remaining == 0 else 0
        
        # Mark the current square as visited
        temp = grid[x][y]
        grid[x][y] = -1
        
        # Explore all 4 directions
        paths = (dfs(x + 1, y, remaining - 1) +
                 dfs(x - 1, y, remaining - 1) +
                 dfs(x, y + 1, remaining - 1) +
                 dfs(x, y - 1, remaining - 1))
        
        # Backtrack: unmark the current square
        grid[x][y] = temp
        
        return paths

    # Find the starting point and count the number of non-obstacle squares
    m, n = len(grid), len(grid[0])
    start_x = start_y = 0
    non_obstacle_count = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                start_x, start_y = i, j
            if grid[i][j] != -1:
                non_obstacle_count += 1
    
    # Start DFS from the starting point
    return dfs(start_x, start_y, non_obstacle_count - 1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 2, -1]]
    print(uniquePathsIII(grid1))  # Output: 2

    # Test Case 2
    grid2 = [[1, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 2]]
    print(uniquePathsIII(grid2))  # Output: 4

    # Test Case 3
    grid3 = [[0, 1],
             [2, 0]]
    print(uniquePathsIII(grid3))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The DFS explores all possible paths in the grid. In the worst case, there are O(m * n) cells, 
  and each cell can be visited once in each path. Thus, the time complexity is O(4^(m*n)), 
  where 4 represents the four possible directions.

Space Complexity:
- The space complexity is O(m * n) due to the recursion stack in the DFS.

Topic: Backtracking
"""