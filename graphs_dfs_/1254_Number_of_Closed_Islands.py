"""
LeetCode Problem #1254: Number of Closed Islands

Problem Statement:
Given a 2D grid consisting of 0s (land) and 1s (water), a closed island is a group of 0s 
completely surrounded by 1s in all four directions (up, down, left, right). A closed island 
cannot touch the grid boundary.

Return the number of closed islands.

Example 1:
Input: grid = [[1,1,1,1,0,1,1,1],
               [1,0,1,1,0,1,1,1],
               [1,0,0,1,1,1,1,1],
               [1,1,1,1,1,1,1,1]]
Output: 1

Example 2:
Input: grid = [[0,0,1,0,0],
               [0,0,0,0,1],
               [1,1,1,1,1]]
Output: 1

Example 3:
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,1,0,1,1],
               [1,0,1,1,0,1,1],
               [1,1,1,1,1,1,1]]
Output: 2

Constraints:
- 1 <= grid.length, grid[0].length <= 100
- grid[i][j] is either 0 or 1
"""

def closedIsland(grid):
    """
    Function to count the number of closed islands in a given grid.

    :param grid: List[List[int]] - 2D grid of 0s (land) and 1s (water)
    :return: int - Number of closed islands
    """
    def dfs(x, y):
        # If out of bounds, return False (not closed)
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        # If water or already visited, return True (closed so far)
        if grid[x][y] == 1:
            return True
        
        # Mark the cell as visited
        grid[x][y] = 1
        
        # Explore all four directions
        top = dfs(x - 1, y)
        bottom = dfs(x + 1, y)
        left = dfs(x, y - 1)
        right = dfs(x, y + 1)
        
        # Return True only if all directions are closed
        return top and bottom and left and right
    
    closed_islands = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Start DFS if we find unvisited land
            if grid[i][j] == 0:
                if dfs(i, j):
                    closed_islands += 1
    
    return closed_islands

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1,1,1,1,0,1,1,1],
             [1,0,1,1,0,1,1,1],
             [1,0,0,1,1,1,1,1],
             [1,1,1,1,1,1,1,1]]
    print(closedIsland(grid1))  # Output: 1

    # Test Case 2
    grid2 = [[0,0,1,0,0],
             [0,0,0,0,1],
             [1,1,1,1,1]]
    print(closedIsland(grid2))  # Output: 1

    # Test Case 3
    grid3 = [[1,1,1,1,1,1,1],
             [1,0,0,1,0,1,1],
             [1,0,1,1,0,1,1],
             [1,1,1,1,1,1,1]]
    print(closedIsland(grid3))  # Output: 2

    # Test Case 4
    grid4 = [[1,1,1,1,1],
             [1,0,1,0,1],
             [1,1,1,1,1]]
    print(closedIsland(grid4))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The DFS function visits each cell at most once. Therefore, the time complexity is O(m * n), 
  where m is the number of rows and n is the number of columns in the grid.

Space Complexity:
- The space complexity is O(m * n) in the worst case due to the recursion stack when performing DFS.

Topic: Graphs (DFS)
"""