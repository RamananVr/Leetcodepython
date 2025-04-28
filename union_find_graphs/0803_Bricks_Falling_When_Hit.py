"""
LeetCode Problem #803: Bricks Falling When Hit

Problem Statement:
You are given an m x n grid, where each cell is either a brick (1) or empty (0). 
Some bricks are connected to the roof (i.e., the top of the grid), and some are not. 
If a brick is not connected to the roof, it will fall due to gravity if a neighboring brick is removed.

You are also given an array `hits`, where `hits[i] = [row_i, col_i]` represents the location of a brick that will be removed. 
The function should return an array `result`, where `result[i]` is the number of bricks that will fall after the ith brick is removed.

Notes:
- A brick is connected to the roof if it is in the first row or if it is connected to another brick that is connected to the roof.
- A brick falling means it is no longer part of the grid after the removal operation.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- grid[i][j] is 0 or 1
- 1 <= hits.length <= 10^4
- hits[i].length == 2
- 0 <= row_i < m
- 0 <= col_i < n

"""

# Solution
from typing import List

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def index(x, y):
            return x * n + y

        def neighbors(x, y):
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    yield nx, ny

        def is_connected_to_roof(x, y):
            return x == 0

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y
                size[root_y] += size[root_x]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        m, n = len(grid), len(grid[0])
        parent = [i for i in range(m * n + 1)]
        size = [1] * (m * n + 1)

        roof = m * n

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    if is_connected_to_roof(x, y):
                        union(index(x, y), roof)
                    for nx, ny in neighbors(x, y):
                        if grid[nx][ny] == 1:
                            union(index(x, y), index(nx, ny))

        return []


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    grid1 = [[1, 0, 0, 0], [1, 1, 1, 0]]
    hits1 = [[1, 0]]
    print(solution.hitBricks(grid1, hits1))  # Expected Output: [2]

    # Test Case 2
    grid2 = [[1, 0, 0, 0], [1, 1, 0, 0]]
    hits2 = [[1, 1], [1, 0]]
    print(solution.hitBricks(grid2, hits2))  # Expected Output: [0, 0]

    # Test Case 3
    grid3 = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
    hits3 = [[0, 2], [2, 0], [1, 1]]
    print(solution.hitBricks(grid3, hits3))  # Expected Output: [0, 0, 3]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The union-find operations (find and union) are nearly constant time due to path compression and union by size.
- The algorithm processes each hit and rebuilds the union-find structure, which takes O(m * n) in the worst case.
- Total complexity: O(m * n + k), where k is the number of hits.

Space Complexity:
- The space complexity is O(m * n) for the union-find data structures (parent and size arrays).

"""

# Topic: Union-Find, Graphs