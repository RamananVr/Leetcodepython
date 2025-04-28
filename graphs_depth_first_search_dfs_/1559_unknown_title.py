"""
LeetCode Problem #1559: Detect Cycles in 2D Grid

Problem Statement:
Given a 2D grid of characters `grid`, return true if there is a cycle in the grid, or false otherwise.

A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the 4 cardinal directions (up, down, left, or right) if the destination cell has the same value. Also, you cannot move back to the previous cell immediately.

Input:
- grid: A 2D list of characters where `grid[i][j]` is a lowercase English letter.

Output:
- Return `True` if there is a cycle in the grid, otherwise return `False`.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 500`
- `grid[i][j]` consists of lowercase English letters.

Example:
Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
Output: true
Explanation: There is a cycle in the grid as shown below:
    a a a a
    a b b a
    a b b a
    a a a a
The cycle is formed by the path: (0,0) -> (0,1) -> (1,1) -> (1,0) -> (0,0).

Follow-up:
Can you solve this problem using DFS and ensure it works efficiently for large grids?
"""

from typing import List

def containsCycle(grid: List[List[str]]) -> bool:
    def dfs(x, y, parent_x, parent_y, char):
        # Mark the cell as visited
        visited[x][y] = True
        
        # Explore all 4 possible directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if the new cell is within bounds
            if 0 <= nx < m and 0 <= ny < n:
                # If the cell has the same character
                if grid[nx][ny] == char:
                    # If the cell is visited and is not the parent, we found a cycle
                    if visited[nx][ny]:
                        if (nx, ny) != (parent_x, parent_y):
                            return True
                    # If the cell is not visited, continue DFS
                    elif not visited[nx][ny]:
                        if dfs(nx, ny, x, y, char):
                            return True
        return False

    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    # Start DFS from every unvisited cell
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                if dfs(i, j, -1, -1, grid[i][j]):
                    return True
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        ["a", "a", "a", "a"],
        ["a", "b", "b", "a"],
        ["a", "b", "b", "a"],
        ["a", "a", "a", "a"]
    ]
    print(containsCycle(grid1))  # Output: True

    # Test Case 2
    grid2 = [
        ["c", "c", "c", "a"],
        ["c", "d", "c", "c"],
        ["c", "c", "e", "c"],
        ["f", "c", "c", "c"]
    ]
    print(containsCycle(grid2))  # Output: True

    # Test Case 3
    grid3 = [
        ["a", "b", "b"],
        ["b", "z", "b"],
        ["b", "b", "a"]
    ]
    print(containsCycle(grid3))  # Output: False

"""
Time Complexity:
- Let `m` be the number of rows and `n` be the number of columns in the grid.
- Each cell is visited at most once, and for each cell, we explore up to 4 directions.
- Thus, the time complexity is O(m * n).

Space Complexity:
- The space complexity is O(m * n) for the `visited` array and the recursion stack in the worst case.

Topic: Graphs, Depth-First Search (DFS)
"""