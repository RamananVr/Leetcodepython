"""
LeetCode Problem #711: Number of Distinct Islands II

Problem Statement:
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally 
(up, down, left, right). You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (slid), rotated (90, 180, 270 degrees), 
or reflected (mirrored) to equal the other.

Return the number of distinct islands.

Example 1:
Input: grid = [[1,1,0,0,0],
               [1,1,0,0,0],
               [0,0,0,1,1],
               [0,0,0,1,1]]
Output: 1

Example 2:
Input: grid = [[1,1,0,1,1],
               [1,0,0,0,0],
               [0,0,0,0,1],
               [1,1,0,1,1]]
Output: 3

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0 or 1.
"""

from typing import List

class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        def dfs(x, y, island):
            grid[x][y] = 0
            island.append((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    dfs(nx, ny, island)

        def normalize(island):
            shapes = []
            for reflection in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                for rotation in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    transformed = [(x * reflection[0] * rotation[0] + y * reflection[1] * rotation[1],
                                    x * reflection[0] * rotation[1] + y * reflection[1] * rotation[0]) for x, y in island]
                    transformed.sort()
                    base_x, base_y = transformed[0]
                    shapes.append(tuple((x - base_x, y - base_y) for x, y in transformed))
            return min(shapes)

        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        unique_islands = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island = []
                    dfs(i, j, island)
                    normalized_island = normalize(island)
                    unique_islands.add(normalized_island)

        return len(unique_islands)

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    grid1 = [[1, 1, 0, 0, 0],
             [1, 1, 0, 0, 0],
             [0, 0, 0, 1, 1],
             [0, 0, 0, 1, 1]]
    print(solution.numDistinctIslands2(grid1))  # Output: 1

    # Test Case 2
    grid2 = [[1, 1, 0, 1, 1],
             [1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1],
             [1, 1, 0, 1, 1]]
    print(solution.numDistinctIslands2(grid2))  # Output: 3

    # Test Case 3
    grid3 = [[1, 1, 0, 0],
             [1, 0, 0, 0],
             [0, 0, 1, 1],
             [0, 0, 1, 1]]
    print(solution.numDistinctIslands2(grid3))  # Output: 2

"""
Time Complexity:
- The DFS traversal visits each cell once, so the time complexity for DFS is O(m * n), where m and n are the dimensions of the grid.
- Normalizing the island involves sorting and generating transformations, which is O(k * log(k)) for each island, where k is the size of the island.
- In the worst case, all cells are part of islands, so the total complexity is O(m * n * log(k)).

Space Complexity:
- The space complexity is O(m * n) for the recursion stack in DFS and storing the island shapes.

Topic: Graph, DFS, Hashing
"""