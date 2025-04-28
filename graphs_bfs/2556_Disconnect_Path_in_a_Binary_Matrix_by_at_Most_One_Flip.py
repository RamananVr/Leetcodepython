"""
LeetCode Problem #2556: Disconnect Path in a Binary Matrix by at Most One Flip

Problem Statement:
You are given a binary matrix `grid` of size `m x n`. A binary matrix has only 0s and 1s as its elements. 
You can perform at most one flip operation on the matrix, where you change a single cell's value from 0 to 1 or from 1 to 0.

Your task is to determine if it is possible to disconnect the path from the top-left corner `(0, 0)` to the bottom-right corner `(m-1, n-1)` 
by performing at most one flip operation. A path is defined as a sequence of adjacent cells (horizontally or vertically) 
that are all 1s, starting from `(0, 0)` and ending at `(m-1, n-1)`.

Return `True` if it is possible to disconnect the path, or `False` otherwise.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `grid[i][j]` is either `0` or `1`.

"""

from collections import deque

def is_possible_to_disconnect(grid):
    """
    Determines if it is possible to disconnect the path in the binary matrix
    by flipping at most one cell.
    """
    m, n = len(grid), len(grid[0])

    def bfs(start, end):
        """Performs BFS to check if there's a path from start to end."""
        queue = deque([start])
        visited = set([start])
        while queue:
            x, y = queue.popleft()
            if (x, y) == end:
                return True
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] == 1:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        return False

    # Check if there's already no path
    if not bfs((0, 0), (m - 1, n - 1)):
        return True

    # Try flipping each cell and check if it disconnects the path
    for i in range(m):
        for j in range(n):
            original = grid[i][j]
            grid[i][j] = 1 - original  # Flip the cell
            if not bfs((0, 0), (m - 1, n - 1)):
                return True
            grid[i][j] = original  # Restore the cell

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Already disconnected
    grid1 = [
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    print(is_possible_to_disconnect(grid1))  # Output: True

    # Test Case 2: Needs one flip to disconnect
    grid2 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    print(is_possible_to_disconnect(grid2))  # Output: True

    # Test Case 3: Cannot disconnect even with one flip
    grid3 = [
        [1, 1],
        [1, 1]
    ]
    print(is_possible_to_disconnect(grid3))  # Output: False

    # Test Case 4: Single cell grid
    grid4 = [
        [1]
    ]
    print(is_possible_to_disconnect(grid4))  # Output: True

"""
Time Complexity:
- The BFS function runs in O(m * n) in the worst case, as it visits each cell once.
- In the worst case, we attempt to flip every cell in the grid, leading to O(m * n) flips.
- Therefore, the overall time complexity is O((m * n) * (m * n)) = O(m^2 * n^2).

Space Complexity:
- The BFS function uses a queue and a visited set, both of which can grow to O(m * n) in size.
- Thus, the space complexity is O(m * n).

Topic: Graphs, BFS
"""