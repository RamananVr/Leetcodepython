"""
LeetCode Problem #695: Max Area of Island

Problem Statement:
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally 
(horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0],[0,0,1,1,0,0,0,0],[0,0,1,1,0,0,0,0],[0,0,0,0,0,0,0,0]]
Output: 4

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0 or 1.
"""

def maxAreaOfIsland(grid):
    """
    Finds the maximum area of an island in the given grid.

    :param grid: List[List[int]] - 2D binary matrix representing the grid
    :return: int - Maximum area of an island
    """
    def dfs(x, y):
        # Base case: Out of bounds or water cell
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
            return 0
        
        # Mark the cell as visited
        grid[x][y] = 0
        
        # Explore all 4 directions and calculate the area
        area = 1
        area += dfs(x + 1, y)  # Down
        area += dfs(x - 1, y)  # Up
        area += dfs(x, y + 1)  # Right
        area += dfs(x, y - 1)  # Left
        
        return area
    
    max_area = 0
    
    # Iterate through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If we find land, perform DFS to calculate the area
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(i, j))
    
    return max_area

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: No island
    grid1 = [[0,0,0,0,0,0,0,0]]
    print(maxAreaOfIsland(grid1))  # Output: 0

    # Test Case 2: Single island
    grid2 = [[0,0,0,0,0,0,0,0],
             [0,0,1,1,0,0,0,0],
             [0,0,1,1,0,0,0,0],
             [0,0,0,0,0,0,0,0]]
    print(maxAreaOfIsland(grid2))  # Output: 4

    # Test Case 3: Multiple islands
    grid3 = [[0,0,1,0,0],
             [0,1,1,0,0],
             [0,0,0,1,1],
             [0,0,0,1,1]]
    print(maxAreaOfIsland(grid3))  # Output: 4

    # Test Case 4: Entire grid is one island
    grid4 = [[1,1,1],
             [1,1,1],
             [1,1,1]]
    print(maxAreaOfIsland(grid4))  # Output: 9

    # Test Case 5: Disconnected small islands
    grid5 = [[1,0,0,0,1],
             [0,0,0,0,0],
             [1,0,0,0,1]]
    print(maxAreaOfIsland(grid5))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The DFS function visits each cell at most once. Therefore, the time complexity is O(m * n), 
  where m is the number of rows and n is the number of columns in the grid.

Space Complexity:
- The space complexity is O(m * n) in the worst case due to the recursion stack when the entire grid is one large island.

Topic: Graph (DFS)
"""