"""
LeetCode Problem #1765: Map of Highest Peak

Problem Statement:
You are given an integer matrix `isWater` of size `m x n` that represents a map of land and water cells.

- If `isWater[i][j] == 0`, cell `(i, j)` is a land cell.
- If `isWater[i][j] == 1`, cell `(i, j)` is a water cell.

You must assign each cell a height in a way that satisfies the following conditions:
1. The height of each water cell is `0`.
2. The height difference between any two adjacent cells is at most `1`. Adjacent cells are cells that share a side.
3. The height of a land cell must be at least `1`.

Return an integer matrix `height` of size `m x n` where `height[i][j]` is the height of cell `(i, j)`.

Constraints:
- `1 <= m, n <= 1000`
- `isWater[i][j]` is `0` or `1`.
- There is at least one water cell.

"""

from collections import deque

def highestPeak(isWater):
    """
    Function to calculate the height map of the given grid.
    
    :param isWater: List[List[int]] - Input grid where 1 represents water and 0 represents land.
    :return: List[List[int]] - Output grid with heights assigned to each cell.
    """
    m, n = len(isWater), len(isWater[0])
    height = [[-1] * n for _ in range(m)]  # Initialize height matrix with -1
    queue = deque()  # BFS queue
    
    # Initialize water cells with height 0 and add them to the queue
    for i in range(m):
        for j in range(n):
            if isWater[i][j] == 1:
                height[i][j] = 0
                queue.append((i, j))
    
    # Directions for moving to adjacent cells (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Perform BFS to calculate heights
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                height[nx][ny] = height[x][y] + 1
                queue.append((nx, ny))
    
    return height

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    isWater1 = [[0, 1], [0, 0]]
    print(highestPeak(isWater1))
    # Expected Output: [[1, 0], [2, 1]]

    # Test Case 2
    isWater2 = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
    print(highestPeak(isWater2))
    # Expected Output: [[1, 1, 0], [2, 2, 1], [3, 3, 2]]

    # Test Case 3
    isWater3 = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
    print(highestPeak(isWater3))
    # Expected Output: [[0, 1, 2], [1, 2, 1], [2, 1, 0]]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The BFS traversal visits each cell exactly once. Since the grid has `m * n` cells, the time complexity is O(m * n).

Space Complexity:
- The `height` matrix requires O(m * n) space.
- The BFS queue can hold up to O(m * n) cells in the worst case.
- Therefore, the space complexity is O(m * n).

Topic: Breadth-First Search (BFS), Matrix
"""