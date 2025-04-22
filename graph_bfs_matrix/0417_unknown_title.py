"""
LeetCode Problem #417: Pacific Atlantic Water Flow

Problem Statement:
There is an `m x n` rectangular island grid where each cell represents the elevation of the island. 
The Pacific ocean touches the island's left and top edges, and the Atlantic ocean touches the island's 
right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with an 
equal or lower elevation.

Return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [
  [1, 2, 2, 3, 5],
  [3, 2, 3, 4, 4],
  [2, 4, 5, 3, 1],
  [6, 7, 1, 4, 5],
  [5, 1, 1, 2, 4]
]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The result is sorted in lexicographical order.

Example 2:
Input: heights = [[1]]
Output: [[0,0]]

Constraints:
- m == heights.length
- n == heights[i].length
- 1 <= m, n <= 200
- 0 <= heights[i][j] <= 10^5
"""

from collections import deque

def pacificAtlantic(heights):
    if not heights or not heights[0]:
        return []

    rows, cols = len(heights), len(heights[0])
    pacific_reachable = set()
    atlantic_reachable = set()

    def bfs(starts, reachable):
        queue = deque(starts)
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                        (nr, nc) not in reachable and
                        heights[nr][nc] >= heights[r][c]):
                    reachable.add((nr, nc))
                    queue.append((nr, nc))

    # Initialize BFS for both oceans
    pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
    atlantic_starts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

    bfs(pacific_starts, pacific_reachable)
    bfs(atlantic_starts, atlantic_reachable)

    # Find cells reachable by both oceans
    return list(pacific_reachable & atlantic_reachable)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    heights1 = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]
    print(pacificAtlantic(heights1))  # Expected: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

    # Test Case 2
    heights2 = [[1]]
    print(pacificAtlantic(heights2))  # Expected: [[0,0]]

# Time Complexity Analysis:
# Let m = number of rows, n = number of columns.
# - BFS is performed twice (once for Pacific and once for Atlantic).
# - Each BFS visits each cell at most once.
# - Total time complexity: O(m * n).

# Space Complexity Analysis:
# - Space is used for the BFS queue and the reachable sets.
# - Total space complexity: O(m * n).

# Topic: Graph, BFS, Matrix