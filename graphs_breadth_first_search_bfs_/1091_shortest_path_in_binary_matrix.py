"""
LeetCode Question #1091: Shortest Path in Binary Matrix

Problem Statement:
Given an n x n binary matrix `grid`, return the length of the shortest clear path in the matrix. 
If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (0, 0) to the bottom-right cell (n-1, n-1) such that:
- All the visited cells of the path are 0.
- All adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of cells visited along the path.

Constraints:
- n == grid.length
- n == grid[i].length
- 1 <= n <= 100
- grid[i][j] is 0 or 1
"""

from collections import deque

def shortestPathBinaryMatrix(grid):
    """
    Finds the shortest path in a binary matrix from the top-left to the bottom-right corner.

    :param grid: List[List[int]] - The binary matrix
    :return: int - The length of the shortest path, or -1 if no path exists
    """
    n = len(grid)
    
    # If the start or end cell is blocked, return -1
    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return -1

    # Directions for 8-connected neighbors
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    # BFS initialization
    queue = deque([(0, 0, 1)])  # (row, col, path_length)
    grid[0][0] = 1  # Mark the starting cell as visited

    while queue:
        row, col, path_length = queue.popleft()
        
        # If we reach the bottom-right corner, return the path length
        if row == n-1 and col == n-1:
            return path_length
        
        # Explore all 8-connected neighbors
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0:
                queue.append((new_row, new_col, path_length + 1))
                grid[new_row][new_col] = 1  # Mark as visited

    # If no path is found, return -1
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: A clear path exists
    grid1 = [
        [0, 1],
        [1, 0]
    ]
    print(shortestPathBinaryMatrix(grid1))  # Output: 2

    # Test Case 2: No clear path exists
    grid2 = [
        [0, 1],
        [1, 1]
    ]
    print(shortestPathBinaryMatrix(grid2))  # Output: -1

    # Test Case 3: Larger grid with a clear path
    grid3 = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    print(shortestPathBinaryMatrix(grid3))  # Output: 4

    # Test Case 4: Start or end cell is blocked
    grid4 = [
        [1, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    print(shortestPathBinaryMatrix(grid4))  # Output: -1

"""
Time Complexity:
- The algorithm performs a Breadth-First Search (BFS) on the grid.
- In the worst case, we visit all n^2 cells of the grid exactly once.
- For each cell, we check up to 8 neighbors, which is a constant operation.
- Therefore, the time complexity is O(n^2).

Space Complexity:
- The space complexity is determined by the queue used in BFS.
- In the worst case, the queue can hold up to O(n^2) cells.
- Therefore, the space complexity is O(n^2).

Topic: Graphs, Breadth-First Search (BFS)
"""