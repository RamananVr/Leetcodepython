"""
LeetCode Problem #778: Swim in Rising Water

You are given an n x n integer matrix `grid` where each value `grid[i][j]` represents the elevation at that point `(i, j)`.

The rain starts to fall. At time `t`, the depth of the water everywhere is `t`. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of the destination square is at most `t`. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time `t` such that you can swim to the bottom right square (n-1, n-1) from the top left square (0, 0).

Constraints:
- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 50`
- `0 <= grid[i][j] < n^2`
- Each value `grid[i][j]` is unique.

Example:
Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you can only swim in the top left cell, because the water level is 0.
At time 1, you can swim to the bottom left cell, as the water level is 1.
At time 2, the top right cell is accessible.
At time 3, you can finally swim to the bottom right cell.
"""

from heapq import heappush, heappop

def swimInWater(grid):
    """
    Finds the minimum time required to swim from the top-left to the bottom-right of the grid.

    :param grid: List[List[int]] - The elevation grid.
    :return: int - The minimum time required.
    """
    n = len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    min_heap = [(grid[0][0], 0, 0)]  # (elevation, x, y)
    visited.add((0, 0))
    max_time = 0

    while min_heap:
        elevation, x, y = heappop(min_heap)
        max_time = max(max_time, elevation)
        if x == n - 1 and y == n - 1:
            return max_time
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                heappush(min_heap, (grid[nx][ny], nx, ny))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[0, 2], [1, 3]]
    print(swimInWater(grid1))  # Output: 3

    # Test Case 2
    grid2 = [[0, 1, 2, 3, 4],
             [24, 23, 22, 21, 5],
             [12, 13, 14, 15, 16],
             [11, 17, 18, 19, 20],
             [10, 9, 8, 7, 6]]
    print(swimInWater(grid2))  # Output: 16

    # Test Case 3
    grid3 = [[3, 2, 1],
             [0, 4, 5],
             [6, 7, 8]]
    print(swimInWater(grid3))  # Output: 8

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses a priority queue (min-heap) to explore the grid. Each cell is pushed and popped from the heap once.
- Pushing and popping from the heap takes O(log(n^2)) time, where n^2 is the total number of cells.
- Thus, the overall time complexity is O(n^2 * log(n^2)).

Space Complexity:
- The space complexity is O(n^2) due to the visited set and the heap, which can store up to n^2 elements.

Topic: Graphs (Dijkstra's Algorithm, BFS with Priority Queue)
"""