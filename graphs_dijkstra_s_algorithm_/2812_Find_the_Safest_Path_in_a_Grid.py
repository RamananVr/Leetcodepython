"""
LeetCode Problem #2812: Find the Safest Path in a Grid

Problem Statement:
You are given an `m x n` grid of integers `grid` where:
- Each cell in the grid represents the risk level of that cell.
- The risk level is a non-negative integer.

You need to find the safest path from the top-left corner (0, 0) to the bottom-right corner (m-1, n-1).
The safety of a path is defined as the minimum risk level of any cell in the path. Your goal is to maximize this safety value.

You can move in four possible directions: up, down, left, or right. You cannot move diagonally or move outside the grid.

Return the maximum safety value of any path from the top-left to the bottom-right corner.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `2 <= m, n <= 100`
- `0 <= grid[i][j] <= 10^6`
"""

from heapq import heappush, heappop

def maximumSafestPath(grid):
    """
    Finds the safest path in the grid using a modified Dijkstra's algorithm.

    :param grid: List[List[int]] - The grid of risk levels.
    :return: int - The maximum safety value of any path from top-left to bottom-right.
    """
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Priority queue for Dijkstra's algorithm (max-heap based on safety value)
    pq = [(-grid[0][0], 0, 0)]  # (-safety, row, col)
    visited = [[False] * n for _ in range(m)]
    visited[0][0] = True
    max_safety = grid[0][0]
    
    while pq:
        safety, x, y = heappop(pq)
        safety = -safety  # Convert back to positive safety value
        
        # If we reach the bottom-right corner, return the safety value
        if x == m - 1 and y == n - 1:
            return safety
        
        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                # Push the minimum safety value along the path
                heappush(pq, (-min(safety, grid[nx][ny]), nx, ny))
    
    return max_safety


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [5, 4, 5],
        [1, 2, 6],
        [7, 4, 6]
    ]
    print(maximumSafestPath(grid1))  # Expected Output: 4

    # Test Case 2
    grid2 = [
        [2, 2, 1],
        [1, 2, 2],
        [2, 1, 2]
    ]
    print(maximumSafestPath(grid2))  # Expected Output: 2

    # Test Case 3
    grid3 = [
        [3, 4, 6, 3, 4],
        [0, 2, 1, 1, 7],
        [8, 8, 3, 2, 7],
        [3, 2, 4, 9, 8],
        [4, 1, 2, 0, 0],
        [4, 6, 5, 4, 3]
    ]
    print(maximumSafestPath(grid3))  # Expected Output: 3


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses a priority queue to explore the grid. In the worst case, every cell in the grid is visited once.
- Each insertion or extraction from the priority queue takes O(log(m * n)), where m * n is the total number of cells.
- Therefore, the time complexity is O((m * n) * log(m * n)).

Space Complexity:
- The space complexity is dominated by the priority queue and the visited array.
- The priority queue can hold up to O(m * n) elements in the worst case.
- The visited array requires O(m * n) space.
- Therefore, the space complexity is O(m * n).

Topic: Graphs (Dijkstra's Algorithm)
"""