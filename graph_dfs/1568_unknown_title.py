"""
LeetCode Problem #1568: Minimum Number of Days to Disconnect Island

Problem Statement:
You are given a 2D grid of 1s (land) and 0s (water). An island is a maximal 4-directionally connected group of 1s.

The grid is said to be "connected" if we can walk from any cell containing a 1 to any other cell containing a 1 through the grid (using only 4-directional moves). 

You are allowed to change at most one 1 in the grid to a 0, and you need to find the minimum number of days to disconnect the grid such that it is no longer connected. If the grid is already disconnected, return 0.

Constraints:
- 1 <= grid.length, grid[0].length <= 30
- grid[i][j] is either 0 or 1.

Example:
Input: grid = [[0,1,0],[1,1,1],[0,1,0]]
Output: 2
Explanation: We need at least 2 days to disconnect the island. In the first day, we can change grid[1][1] to 0, and the grid becomes:
[[0,1,0],
 [1,0,1],
 [0,1,0]]
In the second day, we can change grid[0][1] to 0, and the grid becomes:
[[0,0,0],
 [1,0,1],
 [0,1,0]]
The island is now disconnected.

"""

from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def is_connected(grid: List[List[int]]) -> bool:
            """Check if the grid is connected."""
            rows, cols = len(grid), len(grid[0])
            visited = [[False] * cols for _ in range(rows)]
            
            def dfs(x, y):
                if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == 0 or visited[x][y]:
                    return
                visited[x][y] = True
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    dfs(x + dx, y + dy)
            
            # Find the first land cell to start DFS
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1:
                        dfs(i, j)
                        # Check if there are any unvisited land cells
                        for x in range(rows):
                            for y in range(cols):
                                if grid[x][y] == 1 and not visited[x][y]:
                                    return False
                        return True
            return False  # No land cells, so it's disconnected
        
        def count_islands(grid: List[List[int]]) -> int:
            """Count the number of islands in the grid."""
            rows, cols = len(grid), len(grid[0])
            visited = [[False] * cols for _ in range(rows)]
            islands = 0
            
            def dfs(x, y):
                if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == 0 or visited[x][y]:
                    return
                visited[x][y] = True
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    dfs(x + dx, y + dy)
            
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1 and not visited[i][j]:
                        islands += 1
                        dfs(i, j)
            
            return islands
        
        # If the grid is already disconnected
        if not is_connected(grid):
            return 0
        
        # Try changing each land cell to water and check if it disconnects the grid
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if not is_connected(grid):
                        return 1
                    grid[i][j] = 1  # Restore the cell
        
        # If changing one cell doesn't work, it will take at least 2 days
        return 2

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    grid1 = [[0,1,0],[1,1,1],[0,1,0]]
    print(solution.minDays(grid1))  # Output: 2
    
    # Test Case 2
    grid2 = [[1,1]]
    print(solution.minDays(grid2))  # Output: 2
    
    # Test Case 3
    grid3 = [[1,0,1,0]]
    print(solution.minDays(grid3))  # Output: 0

"""
Time Complexity:
- The `is_connected` function performs a DFS, which takes O(R * C) time, where R is the number of rows and C is the number of columns.
- In the worst case, we may need to check all land cells (at most R * C cells), so the overall complexity is O((R * C)^2).

Space Complexity:
- The space complexity is O(R * C) due to the visited array used in the DFS.

Topic: Graph, DFS
"""