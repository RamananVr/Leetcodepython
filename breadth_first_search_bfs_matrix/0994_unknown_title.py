"""
LeetCode Problem #994: Rotting Oranges

You are given an m x n grid where each cell can have one of three values:
    - 0 representing an empty cell,
    - 1 representing a fresh orange, or
    - 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1

Example 3:
Input: grid = [[0,2]]
Output: 0

Constraints:
    - m == grid.length
    - n == grid[i].length
    - 1 <= m, n <= 10
    - grid[i][j] is 0, 1, or 2
"""

from collections import deque

def orangesRotting(grid):
    """
    Function to calculate the minimum time required for all fresh oranges to rot.
    
    :param grid: List[List[int]] - 2D grid representing the state of oranges
    :return: int - Minimum time required, or -1 if impossible
    """
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0

    # Initialize the queue with all rotten oranges and count fresh oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # (row, col, time)
            elif grid[r][c] == 1:
                fresh_count += 1

    # Directions for 4-neighbor adjacency
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    minutes = 0

    # BFS to rot adjacent fresh oranges
    while queue:
        r, c, minutes = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2  # Mark orange as rotten
                fresh_count -= 1
                queue.append((nr, nc, minutes + 1))

    # If there are still fresh oranges left, return -1
    return minutes if fresh_count == 0 else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[2,1,1],[1,1,0],[0,1,1]]
    print(orangesRotting(grid1))  # Output: 4

    # Test Case 2
    grid2 = [[2,1,1],[0,1,1],[1,0,1]]
    print(orangesRotting(grid2))  # Output: -1

    # Test Case 3
    grid3 = [[0,2]]
    print(orangesRotting(grid3))  # Output: 0

    # Test Case 4
    grid4 = [[0,0,0],[0,0,0],[0,0,0]]
    print(orangesRotting(grid4))  # Output: 0

    # Test Case 5
    grid5 = [[1,2]]
    print(orangesRotting(grid5))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
    - The algorithm performs a Breadth-First Search (BFS) on the grid.
    - In the worst case, we visit each cell once, so the time complexity is O(m * n), 
      where m is the number of rows and n is the number of columns.

Space Complexity:
    - The space complexity is determined by the queue used for BFS.
    - In the worst case, the queue can contain all the cells in the grid, so the space complexity is O(m * n).

Topic: Breadth-First Search (BFS), Matrix
"""