"""
LeetCode Problem #2978: [Problem Title Placeholder]

Problem Statement:
(Note: As of my knowledge cutoff in October 2023, LeetCode Problem #2978 does not exist. 
For the sake of this exercise, I will create a hypothetical problem statement.)

You are given a 2D grid of integers where each cell represents the height of a terrain. 
You are tasked with finding the minimum effort required to travel from the top-left corner 
of the grid to the bottom-right corner. The effort between two adjacent cells is defined 
as the absolute difference in their heights. Your goal is to minimize the maximum effort 
along the path.

You can move up, down, left, or right between adjacent cells.

Write a function `minimumEffortPath(grid: List[List[int]]) -> int` that returns the minimum 
effort required to travel from the top-left to the bottom-right corner.

Constraints:
- `1 <= grid.length, grid[0].length <= 100`
- `0 <= grid[i][j] <= 10^6`
"""

from typing import List
import heapq

def minimumEffortPath(grid: List[List[int]]) -> int:
    """
    Finds the minimum effort required to travel from the top-left to the bottom-right corner of the grid.
    """
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Min-heap to store (effort, x, y)
    heap = [(0, 0, 0)]  # (effort, row, col)
    efforts = [[float('inf')] * cols for _ in range(rows)]
    efforts[0][0] = 0
    
    while heap:
        current_effort, x, y = heapq.heappop(heap)
        
        # If we reach the bottom-right corner, return the effort
        if x == rows - 1 and y == cols - 1:
            return current_effort
        
        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                # Calculate the effort to move to the neighbor
                next_effort = max(current_effort, abs(grid[nx][ny] - grid[x][y]))
                if next_effort < efforts[nx][ny]:
                    efforts[nx][ny] = next_effort
                    heapq.heappush(heap, (next_effort, nx, ny))
    
    return -1  # This line should never be reached

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    print(minimumEffortPath(grid1))  # Expected Output: 2

    # Test Case 2
    grid2 = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    print(minimumEffortPath(grid2))  # Expected Output: 1

    # Test Case 3
    grid3 = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
    print(minimumEffortPath(grid3))  # Expected Output: 0

"""
Time Complexity:
- The algorithm uses Dijkstra's shortest path approach with a priority queue.
- Each cell is processed at most once, and for each cell, we explore up to 4 neighbors.
- The total number of operations is O((rows * cols) * log(rows * cols)) due to the heap operations.

Space Complexity:
- The space complexity is O(rows * cols) for the `efforts` matrix and the heap.

Topic: Graphs, Dijkstra's Algorithm, Priority Queue
"""