"""
LeetCode Problem #2290: Minimum Obstacle Removal to Reach Corner

Problem Statement:
You are given a 2D integer array `grid` of size `m x n`. Each cell is either 0 (empty) or 1 (obstacle). 
You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles you need to remove to reach the bottom-right corner 
(i.e., grid[m-1][n-1]) from the top-left corner (i.e., grid[0][0]).

Note:
- You cannot move outside the boundaries of the grid.
- It is guaranteed that the bottom-right corner is reachable.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- grid[i][j] is either 0 or 1
"""

from collections import deque

def minimumObstacles(grid):
    """
    Finds the minimum number of obstacles to remove to reach the bottom-right corner of the grid.
    
    :param grid: List[List[int]] - 2D grid where 0 represents empty cells and 1 represents obstacles.
    :return: int - Minimum number of obstacles to remove.
    """
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Priority queue for 0-1 BFS
    dq = deque([(0, 0, 0)])  # (row, col, obstacles_removed)
    visited = [[False] * n for _ in range(m)]
    
    while dq:
        row, col, obstacles_removed = dq.popleft()
        
        # If we reach the bottom-right corner, return the number of obstacles removed
        if row == m - 1 and col == n - 1:
            return obstacles_removed
        
        # Mark the current cell as visited
        if visited[row][col]:
            continue
        visited[row][col] = True
        
        # Explore neighbors
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                if grid[nr][nc] == 0:
                    dq.appendleft((nr, nc, obstacles_removed))  # Prioritize empty cells
                else:
                    dq.append((nr, nc, obstacles_removed + 1))  # Add obstacle removal cost

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[0, 1, 1], [1, 1, 0], [1, 1, 0]]
    print(minimumObstacles(grid1))  # Expected Output: 2

    # Test Case 2
    grid2 = [[0, 0, 0], [0, 1, 1], [0, 0, 0]]
    print(minimumObstacles(grid2))  # Expected Output: 0

    # Test Case 3
    grid3 = [[0, 1], [1, 0]]
    print(minimumObstacles(grid3))  # Expected Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses 0-1 BFS, where each cell is processed at most once.
- For a grid of size m x n, the total number of cells is m * n.
- Each cell has at most 4 neighbors, so the time complexity is O(m * n).

Space Complexity:
- The space complexity is O(m * n) due to the `visited` array and the deque used for BFS.

Topic: Graphs, Breadth-First Search (BFS), 0-1 BFS
"""