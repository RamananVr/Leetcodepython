"""
LeetCode Question #2898: Problem Statement

Given a 2D grid of size m x n, where each cell contains an integer representing the height of the terrain, 
determine the minimum effort required to travel from the top-left corner (0, 0) to the bottom-right corner (m-1, n-1). 
The effort between two adjacent cells is defined as the absolute difference in their heights. 

You can move up, down, left, or right. Your goal is to minimize the maximum effort required during the path.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- 1 <= grid[i][j] <= 10^6

Example:
Input: grid = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The path with the minimum effort is (1 → 2 → 2 → 2 → 5), and the maximum effort required is 2.

Input: grid = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The path with the minimum effort is (1 → 2 → 3 → 4 → 5), and the maximum effort required is 1.

Input: grid = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: The path with the minimum effort is (1 → 1 → 1 → 1 → 1), and the maximum effort required is 0.
"""

from heapq import heappush, heappop

def minimumEffortPath(grid):
    """
    Finds the minimum effort required to travel from the top-left corner to the bottom-right corner of the grid.

    :param grid: List[List[int]] - 2D grid of terrain heights
    :return: int - Minimum effort required
    """
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    effort = [[float('inf')] * n for _ in range(m)]
    effort[0][0] = 0
    min_heap = [(0, 0, 0)]  # (effort, x, y)

    while min_heap:
        current_effort, x, y = heappop(min_heap)
        if (x, y) == (m - 1, n - 1):
            return current_effort
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                next_effort = max(current_effort, abs(grid[nx][ny] - grid[x][y]))
                if next_effort < effort[nx][ny]:
                    effort[nx][ny] = next_effort
                    heappush(min_heap, (next_effort, nx, ny))
    return -1  # Should never reach here

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    print(minimumEffortPath(grid1))  # Output: 2

    # Test Case 2
    grid2 = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    print(minimumEffortPath(grid2))  # Output: 1

    # Test Case 3
    grid3 = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
    print(minimumEffortPath(grid3))  # Output: 0

"""
Time and Space Complexity Analysis

Time Complexity:
- The algorithm uses Dijkstra's shortest path approach with a priority queue.
- Each cell is visited at most once, and for each cell, we process its neighbors.
- The total number of cells is m * n, and the priority queue operations (push and pop) take O(log(m * n)).
- Therefore, the time complexity is O(m * n * log(m * n)).

Space Complexity:
- The space complexity is dominated by the effort matrix and the priority queue.
- The effort matrix takes O(m * n) space, and the priority queue can contain up to O(m * n) elements.
- Therefore, the space complexity is O(m * n).

Topic: Graphs
"""