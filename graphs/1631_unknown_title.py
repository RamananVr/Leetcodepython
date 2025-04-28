"""
LeetCode Problem #1631: Path With Minimum Effort

Problem Statement:
You are given an m x n grid `heights` where `heights[i][j]` represents the height of the cell (i, j). 
You want to find a path from the top-left cell to the bottom-right cell with the minimum effort.

A path's effort is the maximum absolute difference in heights between two consecutive cells of the path.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Constraints:
- m == heights.length
- n == heights[i].length
- 1 <= m, n <= 100
- 1 <= heights[i][j] <= 10^6
"""

from heapq import heappop, heappush

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
    min_heap = [(0, 0, 0)]  # (current_effort, x, y)

    while min_heap:
        current_effort, x, y = heappop(min_heap)
        if (x, y) == (m - 1, n - 1):
            return current_effort
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                next_effort = max(current_effort, abs(heights[nx][ny] - heights[x][y]))
                if next_effort < effort[nx][ny]:
                    effort[nx][ny] = next_effort
                    heappush(min_heap, (next_effort, nx, ny))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    heights1 = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    print(minimumEffortPath(heights1))  # Expected Output: 2

    # Test Case 2
    heights2 = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    print(minimumEffortPath(heights2))  # Expected Output: 1

    # Test Case 3
    heights3 = [[1, 10, 6, 7, 9, 10, 4, 9]]
    print(minimumEffortPath(heights3))  # Expected Output: 9

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses Dijkstra's shortest path approach with a priority queue.
- Each cell is processed once, and for each cell, we check its 4 neighbors.
- The total number of cells is m * n, and the priority queue operations (push/pop) are logarithmic in size.
- Therefore, the time complexity is O(m * n * log(m * n)).

Space Complexity:
- The space complexity is dominated by the `effort` matrix and the priority queue.
- The `effort` matrix takes O(m * n) space.
- The priority queue can contain up to O(m * n) elements in the worst case.
- Therefore, the space complexity is O(m * n).

Topic: Graphs
"""