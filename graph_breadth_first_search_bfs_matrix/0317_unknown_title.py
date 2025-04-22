"""
LeetCode Problem #317: Shortest Distance from All Buildings

Problem Statement:
You are given an m x n grid of values 0, 1, or 2, where:

- Each 0 represents an empty land that you can pass by freely.
- Each 1 represents a building that you cannot pass through.
- Each 2 represents an obstacle that you cannot pass through.

You want to build a house on an empty land that minimizes the sum of the shortest distances from the house to all the buildings. You can only move up, down, left, and right.

Return the minimum sum of the shortest distances from the house to all the buildings. If it is not possible to build such a house according to the rules above, return -1.

Example 1:
Input: grid = [[1,0,2,0,1],
               [0,0,0,0,0],
               [0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2):
- The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.

Example 2:
Input: grid = [[1,0]]
Output: 1

Example 3:
Input: grid = [[1]]
Output: -1

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0, 1, or 2.
- There will be at least one building in the grid.
"""

from collections import deque

def shortestDistance(grid):
    if not grid or not grid[0]:
        return -1

    m, n = len(grid), len(grid[0])
    total_distances = [[0] * n for _ in range(m)]
    reachable_count = [[0] * n for _ in range(m)]
    building_count = sum(cell == 1 for row in grid for cell in row)

    def bfs(start_x, start_y):
        visited = [[False] * n for _ in range(m)]
        queue = deque([(start_x, start_y, 0)])
        visited[start_x][start_y] = True

        while queue:
            x, y, dist = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    total_distances[nx][ny] += dist + 1
                    reachable_count[nx][ny] += 1
                    queue.append((nx, ny, dist + 1))

    # Perform BFS from each building
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                bfs(i, j)

    # Find the minimum distance to all buildings
    min_distance = float('inf')
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0 and reachable_count[i][j] == building_count:
                min_distance = min(min_distance, total_distances[i][j])

    return min_distance if min_distance != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 0, 2, 0, 1],
             [0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0]]
    print(shortestDistance(grid1))  # Output: 7

    # Test Case 2
    grid2 = [[1, 0]]
    print(shortestDistance(grid2))  # Output: 1

    # Test Case 3
    grid3 = [[1]]
    print(shortestDistance(grid3))  # Output: -1

    # Test Case 4
    grid4 = [[1, 2, 0],
             [0, 0, 0],
             [0, 1, 0]]
    print(shortestDistance(grid4))  # Output: 6

"""
Time Complexity:
- BFS is performed from each building. If there are `k` buildings, and the grid size is `m x n`, 
  the BFS from each building takes O(m * n) time. Thus, the total time complexity is O(k * m * n).

Space Complexity:
- The space complexity is O(m * n) due to the visited array and the queue used in BFS.

Topic: Graph, Breadth-First Search (BFS), Matrix
"""