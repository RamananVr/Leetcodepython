"""
LeetCode Question #1293: Shortest Path in a Grid with Obstacles Elimination

Problem Statement:
You are given an `m x n` integer matrix `grid` where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper-left corner (0, 0) to the lower-right corner (m-1, n-1) given that you can eliminate at most `k` obstacles. If it is not possible to find such a walk, return -1.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 40`
- `1 <= k <= m * n`
- `grid[i][j]` is either 0 or 1.
- `grid[0][0] == 0`
- `grid[m-1][n-1] == 0`
"""

from collections import deque

def shortestPath(grid, k):
    """
    Finds the shortest path in a grid with at most k obstacle eliminations.

    :param grid: List[List[int]] - The grid of 0s and 1s.
    :param k: int - Maximum number of obstacles that can be eliminated.
    :return: int - Minimum number of steps to reach the bottom-right corner, or -1 if not possible.
    """
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, 0, 0, k)])  # (x, y, steps, remaining eliminations)
    visited = set([(0, 0, k)])  # (x, y, remaining eliminations)

    while queue:
        x, y, steps, remaining_k = queue.popleft()

        # If we reach the bottom-right corner, return the number of steps
        if x == m - 1 and y == n - 1:
            return steps

        # Explore all 4 possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Check if the new position is within bounds
            if 0 <= nx < m and 0 <= ny < n:
                new_k = remaining_k - grid[nx][ny]

                # If we have enough eliminations left and haven't visited this state
                if new_k >= 0 and (nx, ny, new_k) not in visited:
                    visited.add((nx, ny, new_k))
                    queue.append((nx, ny, steps + 1, new_k))

    # If we exhaust the queue without finding a path, return -1
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
    k1 = 1
    print(shortestPath(grid1, k1))  # Expected Output: 6

    # Test Case 2
    grid2 = [[0, 1, 1], [1, 1, 1], [1, 0, 0]]
    k2 = 1
    print(shortestPath(grid2, k2))  # Expected Output: -1

    # Test Case 3
    grid3 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    k3 = 1
    print(shortestPath(grid3, k3))  # Expected Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The worst-case scenario involves visiting every cell in the grid with all possible values of `k`.
- There are `m * n` cells, and for each cell, there are at most `k` states to consider.
- Each state is processed in O(1) time, so the overall time complexity is O(m * n * k).

Space Complexity:
- The space complexity is dominated by the `visited` set and the `queue`.
- The size of the `visited` set is O(m * n * k), and the queue can also grow to O(m * n * k) in the worst case.
- Thus, the space complexity is O(m * n * k).

Topic: Breadth-First Search (BFS)
"""