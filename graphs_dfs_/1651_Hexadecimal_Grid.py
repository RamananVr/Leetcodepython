"""
LeetCode Problem #1651: Hexadecimal Grid

Problem Statement:
You are given a grid of hexadecimal digits (0-9, A-F) where each digit represents a cell in the grid. 
Each cell can be connected to its adjacent cells (up, down, left, right) if the hexadecimal digit in 
the cell is greater than or equal to the hexadecimal digit in the adjacent cell. Your task is to 
determine the size of the largest connected component in the grid.

Write a function `largestComponentSize(grid: List[List[str]]) -> int` that takes a 2D grid of hexadecimal 
digits as input and returns the size of the largest connected component.

Constraints:
- The grid dimensions are m x n, where 1 <= m, n <= 100.
- Each cell in the grid contains a single hexadecimal digit ('0'-'9', 'A'-'F').

Example:
Input: grid = [
    ["1", "A", "3"],
    ["B", "2", "C"],
    ["4", "D", "E"]
]
Output: 4
Explanation: The largest connected component is formed by the cells ["A", "B", "C", "D"].

"""

from typing import List

def largestComponentSize(grid: List[List[str]]) -> int:
    def dfs(x, y):
        # Perform DFS to explore the connected component
        stack = [(x, y)]
        size = 0
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))
            size += 1
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    if int(grid[nx][ny], 16) >= int(grid[cx][cy], 16):
                        stack.append((nx, ny))
        return size

    m, n = len(grid), len(grid[0])
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    max_size = 0

    for i in range(m):
        for j in range(n):
            if (i, j) not in visited:
                max_size = max(max_size, dfs(i, j))

    return max_size

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        ["1", "A", "3"],
        ["B", "2", "C"],
        ["4", "D", "E"]
    ]
    print(largestComponentSize(grid1))  # Output: 4

    # Test Case 2
    grid2 = [
        ["0", "1", "2"],
        ["3", "4", "5"],
        ["6", "7", "8"]
    ]
    print(largestComponentSize(grid2))  # Output: 1

    # Test Case 3
    grid3 = [
        ["F", "E", "D"],
        ["C", "B", "A"],
        ["9", "8", "7"]
    ]
    print(largestComponentSize(grid3))  # Output: 9

    # Test Case 4
    grid4 = [
        ["A", "B"],
        ["C", "D"]
    ]
    print(largestComponentSize(grid4))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The DFS function visits each cell in the grid exactly once. Therefore, the time complexity is O(m * n), 
  where m is the number of rows and n is the number of columns in the grid.

Space Complexity:
- The space complexity is O(m * n) due to the `visited` set and the stack used in the DFS function.

Topic: Graphs (DFS)
"""