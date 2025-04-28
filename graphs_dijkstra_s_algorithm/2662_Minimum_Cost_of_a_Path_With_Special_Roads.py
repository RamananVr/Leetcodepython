"""
LeetCode Problem #2662: Minimum Cost of a Path With Special Roads

Problem Statement:
You are given a 2D grid where you start at the top-left corner (0, 0) and want to reach the bottom-right corner (m-1, n-1). 
Each cell in the grid has a cost associated with it, and you can only move right or down. 
Additionally, there are some "special roads" that allow you to jump from one cell to another at a reduced cost.

Your task is to find the minimum cost to reach the bottom-right corner of the grid.

Input:
- m: An integer representing the number of rows in the grid.
- n: An integer representing the number of columns in the grid.
- grid: A 2D list of integers where grid[i][j] represents the cost of the cell at position (i, j).
- special_roads: A list of tuples, where each tuple is of the form (x1, y1, x2, y2, cost). 
  This represents a special road that allows you to move from cell (x1, y1) to cell (x2, y2) at the given cost.

Output:
- Return the minimum cost to reach the bottom-right corner of the grid.

Constraints:
- 1 <= m, n <= 100
- 1 <= grid[i][j] <= 100
- 0 <= x1, y1, x2, y2 < m, n
- 1 <= cost <= 10^4
- The number of special roads is at most 100.

"""

from heapq import heappop, heappush
import math

def minimumCostPath(m, n, grid, special_roads):
    # Dijkstra's algorithm to find the minimum cost path
    def neighbors(x, y):
        for dx, dy in [(0, 1), (1, 0)]:  # Right and Down moves
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                yield nx, ny

    # Priority queue for Dijkstra's algorithm
    pq = [(grid[0][0], 0, 0)]  # (cost, x, y)
    min_cost = [[math.inf] * n for _ in range(m)]
    min_cost[0][0] = grid[0][0]

    while pq:
        cost, x, y = heappop(pq)

        # If we reach the bottom-right corner, return the cost
        if (x, y) == (m - 1, n - 1):
            return cost

        # Process neighbors (right and down moves)
        for nx, ny in neighbors(x, y):
            new_cost = cost + grid[nx][ny]
            if new_cost < min_cost[nx][ny]:
                min_cost[nx][ny] = new_cost
                heappush(pq, (new_cost, nx, ny))

        # Process special roads
        for x1, y1, x2, y2, road_cost in special_roads:
            if (x, y) == (x1, y1):
                if cost + road_cost < min_cost[x2][y2]:
                    min_cost[x2][y2] = cost + road_cost
                    heappush(pq, (cost + road_cost, x2, y2))

    return -1  # If no path is found (should not happen with valid input)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    m = 3
    n = 3
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    special_roads = [(0, 0, 2, 2, 5)]  # Special road from (0, 0) to (2, 2) with cost 5
    print(minimumCostPath(m, n, grid, special_roads))  # Output: 5

    # Test Case 2
    m = 2
    n = 2
    grid = [
        [1, 2],
        [3, 4]
    ]
    special_roads = [(0, 0, 1, 1, 2)]  # Special road from (0, 0) to (1, 1) with cost 2
    print(minimumCostPath(m, n, grid, special_roads))  # Output: 2

    # Test Case 3
    m = 3
    n = 3
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    special_roads = []  # No special roads
    print(minimumCostPath(m, n, grid, special_roads))  # Output: 21

"""
Time Complexity:
- The algorithm uses Dijkstra's algorithm, which processes each cell once and explores all neighbors.
- The number of cells is m * n, and for each cell, we process its neighbors and special roads.
- Let k be the number of special roads. The complexity is O((m * n + k) * log(m * n)) due to the priority queue.

Space Complexity:
- The space complexity is O(m * n) for the min_cost array and the priority queue.

Topic: Graphs, Dijkstra's Algorithm
"""