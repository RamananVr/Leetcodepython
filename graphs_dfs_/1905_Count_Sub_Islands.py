"""
LeetCode Problem #1905: Count Sub Islands

Problem Statement:
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). 
An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells of this island in grid2.

Return the number of sub-islands in grid2.

Example 1:
Input: grid1 = [[1,1,1,0,0],
                [1,1,0,0,0],
                [1,0,0,1,1],
                [0,0,0,1,1]],
       grid2 = [[1,1,1,0,0],
                [0,1,0,0,0],
                [1,0,0,1,1],
                [0,0,0,1,1]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2. The 3 sub-islands are shown in green.

Example 2:
Input: grid1 = [[1,0,1,0,1],
                [1,1,1,1,0],
                [0,0,0,0,0],
                [1,1,1,1,1]],
       grid2 = [[1,0,1,0,0],
                [0,1,1,1,0],
                [0,0,0,0,0],
                [1,0,1,1,1]]
Output: 2
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2. The 2 sub-islands are shown in green.

Constraints:
- m == grid1.length == grid2.length
- n == grid1[i].length == grid2[i].length
- 1 <= m, n <= 500
- grid1[i][j] and grid2[i][j] are either 0 or 1.
"""

# Python Solution
from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i, j):
            # If out of bounds or water, stop the DFS
            if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] == 0:
                return True
            
            # Mark the cell as visited in grid2
            grid2[i][j] = 0
            
            # Check if this cell is part of a valid sub-island
            is_sub_island = grid1[i][j] == 1
            
            # Explore all 4 directions
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                is_sub_island = dfs(i + x, j + y) and is_sub_island
            
            return is_sub_island
        
        m, n = len(grid1), len(grid1[0])
        sub_islands = 0
        
        for i in range(m):
            for j in range(n):
                # Start DFS if we find land in grid2
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        sub_islands += 1
        
        return sub_islands

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    grid1 = [[1,1,1,0,0],
             [1,1,0,0,0],
             [1,0,0,1,1],
             [0,0,0,1,1]]
    grid2 = [[1,1,1,0,0],
             [0,1,0,0,0],
             [1,0,0,1,1],
             [0,0,0,1,1]]
    print(solution.countSubIslands(grid1, grid2))  # Output: 3

    # Test Case 2
    grid1 = [[1,0,1,0,1],
             [1,1,1,1,0],
             [0,0,0,0,0],
             [1,1,1,1,1]]
    grid2 = [[1,0,1,0,0],
             [0,1,1,1,0],
             [0,0,0,0,0],
             [1,0,1,1,1]]
    print(solution.countSubIslands(grid1, grid2))  # Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- The DFS function visits each cell in grid2 at most once. Therefore, the time complexity is O(m * n), where m and n are the dimensions of the grid.

Space Complexity:
- The space complexity is O(m * n) in the worst case due to the recursion stack in DFS.

Overall: Time Complexity = O(m * n), Space Complexity = O(m * n)
"""

# Topic: Graphs (DFS)