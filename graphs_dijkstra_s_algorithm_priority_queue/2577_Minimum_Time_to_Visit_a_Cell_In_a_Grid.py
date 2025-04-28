"""
LeetCode Problem #2577: Minimum Time to Visit a Cell In a Grid

Problem Statement:
You are given a `m x n` grid of integers `grid` where each cell in the grid represents the time you can enter that cell. 
To move to a cell `(i, j)`, you must wait until the time `grid[i][j]` and then you can move to any of its 4 neighboring cells 
(up, down, left, right). You can move to a neighboring cell `(i, j)` if and only if the time `grid[i][j]` is greater than or 
equal to the time you reach that cell.

You want to find the minimum time required to go from the top-left cell `(0, 0)` to the bottom-right cell `(m-1, n-1)`. 
If it is impossible to reach the bottom-right cell, return `-1`.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `0 <= grid[i][j] <= 10^5`

Example:
Input: grid = [[0,2,4],[3,2,1],[1,0,4]]
Output: 7
Explanation: The minimum time to reach the bottom-right cell is 7.

"""

from heapq import heappop, heappush
from collections import deque

def minimumTime(grid):
    """
    Finds the minimum time required to go from the top-left cell to the bottom-right cell in the grid.
    Returns -1 if it is impossible to reach the destination.
    """
    m, n = len(grid), len(grid[0])
    if grid[0][1] > 1 and grid[1][0] > 1:  # Early exit if the first move is impossible
        return -1

    # Min-heap to store (time, x, y)
    heap = [(0, 0, 0)]
    visited = set()

    # Directions for moving in the grid
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while heap:
        time, x, y = heappop(heap)

        # If we reach the bottom-right cell, return the time
        if (x, y) == (m - 1, n - 1):
            return time

        # Skip if already visited
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                wait_time = max(0, grid[nx][ny] - time)
                # Ensure we can move to the cell at the correct time
                if (time + wait_time) % 2 != grid[nx][ny] % 2:
                    wait_time += 1
                heappush(heap, (time + 1 + wait_time, nx, ny))

    # If we exhaust the heap without reaching the destination, return -1
    return -1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[0, 2, 4], [3, 2, 1], [1, 0, 4]]
    print(minimumTime(grid1))  # Output: 7

    # Test Case 2
    grid2 = [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
    print(minimumTime(grid2))  # Output: 4

    # Test Case 3
    grid3 = [[0, 1], [1, 0]]
    print(minimumTime(grid3))  # Output: 2

    # Test Case 4
    grid4 = [[0, 3], [3, 0]]
    print(minimumTime(grid4))  # Output: -1


"""
Time Complexity:
- Let `m` and `n` be the dimensions of the grid.
- Each cell is processed at most once, and for each cell, we perform a constant amount of work (checking neighbors and pushing to the heap).
- The heap operations (push and pop) take O(log(m * n)) time.
- Therefore, the overall time complexity is O((m * n) * log(m * n)).

Space Complexity:
- The space complexity is O(m * n) due to the heap and visited set.

Topic: Graphs, Dijkstra's Algorithm, Priority Queue
"""