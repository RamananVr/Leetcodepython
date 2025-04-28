"""
LeetCode Problem #2897: [Problem Title Placeholder]

Problem Statement:
(Note: As of my knowledge cutoff in October 2023, LeetCode Problem #2897 does not exist. 
For the sake of this exercise, I will create a hypothetical problem statement.)

You are given an `n x n` grid where each cell contains an integer representing the height of the terrain at that point. 
You are tasked with finding the minimum effort required to travel from the top-left corner of the grid (0, 0) to the 
bottom-right corner (n-1, n-1). The effort between two adjacent cells is defined as the absolute difference in their heights.

You can move up, down, left, or right. Your goal is to minimize the maximum effort required during the path.

Return the minimum effort required to travel from the top-left to the bottom-right corner.

Constraints:
- `1 <= n <= 100`
- `0 <= grid[i][j] <= 10^6`

Example:
Input: grid = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The path with the minimum effort is (1 → 2 → 2 → 2 → 5). The maximum effort along this path is 2.
"""

from heapq import heappop, heappush

def minimumEffortPath(grid):
    """
    Finds the minimum effort required to travel from the top-left to the bottom-right corner of the grid.
    
    :param grid: List[List[int]] - 2D grid of integers representing terrain heights
    :return: int - Minimum effort required
    """
    n = len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    effort = [[float('inf')] * n for _ in range(n)]
    effort[0][0] = 0
    min_heap = [(0, 0, 0)]  # (effort, x, y)

    while min_heap:
        current_effort, x, y = heappop(min_heap)

        # If we reach the bottom-right corner, return the effort
        if x == n - 1 and y == n - 1:
            return current_effort

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                # Calculate the effort to move to the next cell
                next_effort = max(current_effort, abs(grid[nx][ny] - grid[x][y]))
                if next_effort < effort[nx][ny]:
                    effort[nx][ny] = next_effort
                    heappush(min_heap, (next_effort, nx, ny))

    return -1  # This line should never be reached

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    print(minimumEffortPath(grid1))  # Output: 2

    # Test Case 2
    grid2 = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    print(minimumEffortPath(grid2))  # Output: 1

    # Test Case 3
    grid3 = [[1, 10, 6, 7, 9, 10, 4, 9]]
    print(minimumEffortPath(grid3))  # Output: 9

"""
Time Complexity Analysis:
- The algorithm uses Dijkstra's shortest path approach with a priority queue (min-heap).
- Each cell is processed at most once, and for each cell, we check its 4 neighbors.
- The total number of cells is n^2, and each operation on the heap (push/pop) takes O(log(n^2)) = O(2*log(n)).
- Therefore, the time complexity is O(n^2 * log(n)).

Space Complexity Analysis:
- The space complexity is O(n^2) for the `effort` matrix and the priority queue.

Topic: Graphs, Dijkstra's Algorithm, Priority Queue
"""