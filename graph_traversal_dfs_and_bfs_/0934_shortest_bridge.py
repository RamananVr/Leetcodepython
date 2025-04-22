"""
LeetCode Question #934: Shortest Bridge

Problem Statement:
You are given an n x n binary matrix grid where 1 represents land and 0 represents water. 
An island is a group of 1's connected 4-directionally (horizontal or vertical). 
You may assume that exactly two islands exist in grid.

You want to find the shortest bridge between the two islands. 
A bridge is defined as a path of 0's (water) connecting the two islands such that no 0's in the path are diagonally connected. 
You may only change a 0 to a 1 to connect the two islands.

Return the length of the shortest bridge.

Constraints:
- n == grid.length == grid[i].length
- 2 <= n <= 100
- grid[i][j] is either 0 or 1.
- There are exactly two islands in grid.
"""

from collections import deque

def shortestBridge(grid):
    def dfs(x, y):
        """Perform DFS to mark the first island."""
        if x < 0 or y < 0 or x >= n or y >= n or grid[x][y] != 1:
            return
        grid[x][y] = -1  # Mark as visited
        island.append((x, y))
        for dx, dy in directions:
            dfs(x + dx, y + dy)

    def bfs():
        """Perform BFS to find the shortest bridge."""
        queue = deque(island)
        steps = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1:  # Found the second island
                            return steps
                        elif grid[nx][ny] == 0:  # Expand the bridge
                            grid[nx][ny] = -1  # Mark as visited
                            queue.append((nx, ny))
            steps += 1
        return -1  # Should never reach here

    n = len(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    island = []

    # Step 1: Find the first island and mark it
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i, j)
                break
        if island:
            break

    # Step 2: Perform BFS to find the shortest bridge
    return bfs()

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [0, 1],
        [1, 0]
    ]
    print(shortestBridge(grid1))  # Output: 1

    # Test Case 2
    grid2 = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    print(shortestBridge(grid2))  # Output: 2

    # Test Case 3
    grid3 = [
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1]
    ]
    print(shortestBridge(grid3))  # Output: 1

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The DFS step visits all cells of the first island, which takes O(n^2) in the worst case.
   - The BFS step explores the grid to find the shortest bridge, which also takes O(n^2) in the worst case.
   - Overall time complexity: O(n^2).

2. Space Complexity:
   - The space used by the `island` list and the BFS queue is proportional to the number of cells, which is O(n^2) in the worst case.
   - Overall space complexity: O(n^2).

Topic: Graph Traversal (DFS and BFS)
"""