"""
LeetCode Problem #827: Making A Large Island

Problem Statement:
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
Return the size of the largest island in the grid after applying this operation.

An island is a group of 1s connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

Constraints:
- n == grid.length
- n == grid[i].length
- 1 <= n <= 500
- grid[i][j] is either 0 or 1.

Example 1:
Input: grid = [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s to form an island of area 3.

Example 2:
Input: grid = [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 to form an island of area 4.

Example 3:
Input: grid = [[1, 1], [1, 1]]
Output: 4
Explanation: There is no 0 to change, so the size of the island is 4.

"""

from collections import defaultdict

def largestIsland(grid):
    n = len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def dfs(x, y, island_id):
        """Perform DFS to calculate the size of the island and mark its cells."""
        stack = [(x, y)]
        size = 0
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))
            grid[cx][cy] = island_id
            size += 1
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 and (nx, ny) not in visited:
                    stack.append((nx, ny))
        return size

    # Step 1: Identify all islands and calculate their sizes
    visited = set()
    island_sizes = defaultdict(int)
    island_id = 2  # Start marking islands from ID 2 (since 0 and 1 are already used)
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and (i, j) not in visited:
                island_sizes[island_id] = dfs(i, j, island_id)
                island_id += 1

    # Step 2: Check each 0 cell to see the potential size of the island if converted to 1
    max_island_size = max(island_sizes.values(), default=0)  # Handle case where no islands exist
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                seen_islands = set()
                potential_size = 1  # Start with size 1 for the converted cell
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > 1:
                        island_id = grid[nx][ny]
                        if island_id not in seen_islands:
                            potential_size += island_sizes[island_id]
                            seen_islands.add(island_id)
                max_island_size = max(max_island_size, potential_size)

    return max_island_size


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 0], [0, 1]]
    print(largestIsland(grid1))  # Output: 3

    # Test Case 2
    grid2 = [[1, 1], [1, 0]]
    print(largestIsland(grid2))  # Output: 4

    # Test Case 3
    grid3 = [[1, 1], [1, 1]]
    print(largestIsland(grid3))  # Output: 4

    # Test Case 4
    grid4 = [[0, 0], [0, 0]]
    print(largestIsland(grid4))  # Output: 1

    # Test Case 5
    grid5 = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    print(largestIsland(grid5))  # Output: 5


"""
Time and Space Complexity Analysis:

Time Complexity:
- The DFS traversal to identify islands takes O(n^2) in the worst case, as we visit each cell once.
- For each 0 cell, we check its neighbors, which takes O(1) per cell. This results in an additional O(n^2) in the worst case.
- Overall, the time complexity is O(n^2).

Space Complexity:
- The `visited` set and `island_sizes` dictionary use O(n^2) space in the worst case.
- The recursion stack for DFS can also use O(n^2) space in the worst case.
- Overall, the space complexity is O(n^2).

Topic: Graphs, DFS
"""