"""
LeetCode Problem #1336: "Path With Minimum Effort"

Problem Statement:
You are given an m x n grid `heights` where `heights[row][col]` represents the height of the cell at (row, col).
You want to find a path from the top-left cell to the bottom-right cell with the minimum effort.

A path's effort is the maximum absolute difference in heights between two consecutive cells of the path.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Constraints:
- m == heights.length
- n == heights[i].length
- 1 <= m, n <= 100
- 1 <= heights[i][j] <= 10^6
"""

import heapq

def minimumEffortPath(heights):
    """
    Finds the minimum effort required to travel from the top-left cell to the bottom-right cell.

    :param heights: List[List[int]] - 2D grid of heights
    :return: int - Minimum effort required
    """
    def is_valid(x, y):
        return 0 <= x < m and 0 <= y < n

    m, n = len(heights), len(heights[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    effort = [[float('inf')] * n for _ in range(m)]
    effort[0][0] = 0
    min_heap = [(0, 0, 0)]  # (current effort, x, y)

    while min_heap:
        current_effort, x, y = heapq.heappop(min_heap)
        if (x, y) == (m - 1, n - 1):
            return current_effort
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                next_effort = max(current_effort, abs(heights[nx][ny] - heights[x][y]))
                if next_effort < effort[nx][ny]:
                    effort[nx][ny] = next_effort
                    heapq.heappush(min_heap, (next_effort, nx, ny))
    return -1  # Should never reach here

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    heights1 = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    print(minimumEffortPath(heights1))  # Expected Output: 2

    # Test Case 2
    heights2 = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    print(minimumEffortPath(heights2))  # Expected Output: 1

    # Test Case 3
    heights3 = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
    print(minimumEffortPath(heights3))  # Expected Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses Dijkstra's shortest path approach with a priority queue.
- The number of cells in the grid is m * n.
- Each cell is processed once, and for each cell, we check up to 4 neighbors.
- The heap operations (push and pop) take O(log(m * n)).
- Therefore, the overall time complexity is O((m * n) * log(m * n)).

Space Complexity:
- The space complexity is dominated by the `effort` matrix and the priority queue.
- The `effort` matrix takes O(m * n) space.
- The priority queue can contain up to m * n elements, taking O(m * n) space.
- Therefore, the overall space complexity is O(m * n).

Topic: Graphs
"""