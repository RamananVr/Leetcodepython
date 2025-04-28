"""
LeetCode Problem #1162: As Far from Land as Possible

Problem Statement:
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, 
return the maximum distance from the nearest land cell to a water cell. If no land or water exists 
in the grid, return -1.

The distance used in this problem is the Manhattan distance: 
distance between (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

Constraints:
- 1 <= n <= 100
- grid[i][j] is 0 or 1

Example:
Input: grid = [[0,1,0],[0,0,0],[1,0,0]]
Output: 2
Explanation: The cell (2, 2) is the farthest from land with a distance of 2.

"""

from collections import deque

def maxDistance(grid):
    """
    Finds the maximum distance from the nearest land cell to a water cell in the grid.

    :param grid: List[List[int]] - A 2D grid of 0s (water) and 1s (land)
    :return: int - The maximum distance, or -1 if no valid distance exists
    """
    n = len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque()

    # Add all land cells to the queue
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                queue.append((i, j))

    # If there are no land or no water cells, return -1
    if len(queue) == 0 or len(queue) == n * n:
        return -1

    max_distance = -1

    # Perform BFS from all land cells
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                grid[nx][ny] = grid[x][y] + 1  # Update distance
                max_distance = max(max_distance, grid[nx][ny] - 1)
                queue.append((nx, ny))

    return max_distance


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[0, 1, 0], [0, 0, 0], [1, 0, 0]]
    print(maxDistance(grid1))  # Output: 2

    # Test Case 2
    grid2 = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
    print(maxDistance(grid2))  # Output: 4

    # Test Case 3
    grid3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print(maxDistance(grid3))  # Output: -1

    # Test Case 4
    grid4 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(maxDistance(grid4))  # Output: -1


"""
Time and Space Complexity Analysis:

Time Complexity:
- The BFS traversal visits each cell in the grid at most once. Since the grid has n x n cells, 
  the time complexity is O(n^2).

Space Complexity:
- The space complexity is O(n^2) due to the queue used in BFS and the grid itself.

Topic: Breadth-First Search (BFS), Matrix
"""