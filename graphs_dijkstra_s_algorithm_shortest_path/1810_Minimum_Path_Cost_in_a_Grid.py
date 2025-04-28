"""
LeetCode Problem #1810: Minimum Path Cost in a Grid

Problem Statement:
You are given a 2D grid of size m x n, where each cell in the grid has a non-negative integer cost associated with it. 
You are also given a start cell (sx, sy) and a destination cell (dx, dy). You can move up, down, left, or right, 
but you cannot move diagonally or move outside the grid. Your task is to find the minimum cost to travel from the 
start cell to the destination cell.

If it is not possible to reach the destination cell, return -1.

Constraints:
- The grid is a 2D list of integers with dimensions m x n.
- 1 <= m, n <= 100
- 0 <= grid[i][j] <= 1000
- The start and destination cells are valid cells within the grid.

Example:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]], start = (0,0), destination = (2,2)
Output: 7
Explanation: The minimum cost path is 1 → 3 → 1 → 1 → 1, with a total cost of 7.
"""

from heapq import heappop, heappush
from typing import List, Tuple

def minPathCost(grid: List[List[int]], start: Tuple[int, int], destination: Tuple[int, int]) -> int:
    """
    Finds the minimum cost to travel from the start cell to the destination cell in a grid.
    """
    m, n = len(grid), len(grid[0])
    sx, sy = start
    dx, dy = destination

    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Priority queue for Dijkstra's algorithm
    pq = [(grid[sx][sy], sx, sy)]  # (current_cost, x, y)
    visited = set()

    while pq:
        cost, x, y = heappop(pq)

        # If we reach the destination, return the cost
        if (x, y) == (dx, dy):
            return cost

        # Mark the current cell as visited
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                heappush(pq, (cost + grid[nx][ny], nx, ny))

    # If we exhaust the queue without reaching the destination, return -1
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    start1 = (0, 0)
    destination1 = (2, 2)
    print(minPathCost(grid1, start1, destination1))  # Output: 7

    # Test Case 2
    grid2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start2 = (0, 0)
    destination2 = (2, 2)
    print(minPathCost(grid2, start2, destination2))  # Output: 21

    # Test Case 3
    grid3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    start3 = (0, 0)
    destination3 = (2, 2)
    print(minPathCost(grid3, start3, destination3))  # Output: 4

    # Test Case 4 (Unreachable destination)
    grid4 = [[1, 1, 1], [1, 1000, 1], [1, 1, 1]]
    start4 = (0, 0)
    destination4 = (1, 1)
    print(minPathCost(grid4, start4, destination4))  # Output: -1

"""
Time Complexity:
- The algorithm uses Dijkstra's algorithm, which processes each cell at most once.
- The priority queue operations (push and pop) take O(log(m * n)).
- Therefore, the overall time complexity is O((m * n) * log(m * n)).

Space Complexity:
- The space complexity is O(m * n) due to the priority queue and visited set.

Topic: Graphs, Dijkstra's Algorithm, Shortest Path
"""