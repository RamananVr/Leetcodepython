"""
LeetCode Problem #1992: Find All Groups of Farmland

Problem Statement:
You are given a 2D integer array `land` where `land[i][j]` is either 0 (representing a barren land) or 1 (representing a farmland). 
A group of farmland is a rectangular area of contiguous 1's such that every cell in the group is part of the rectangle and all cells outside the rectangle are 0's.

Your task is to find all groups of farmland. A group of farmland is represented as a rectangular area by the coordinates of its top-left corner 
and bottom-right corner: `[r1, c1, r2, c2]`. 

Return a 2D array containing the coordinates of all groups of farmland. If there are no groups of farmland, return an empty array. 
You may return the answer in any order.

Constraints:
- `m == land.length`
- `n == land[i].length`
- `1 <= m, n <= 300`
- `land[i][j]` is either 0 or 1.
- Groups of farmland are rectangular in shape.

Example 1:
Input: land = [[1,0,0],[0,1,1],[0,1,1]]
Output: [[0,0,0,0],[1,1,2,2]]
Explanation:
- The first group of farmland starts at (0, 0) and ends at (0, 0).
- The second group of farmland starts at (1, 1) and ends at (2, 2).

Example 2:
Input: land = [[1,1],[1,1]]
Output: [[0,0,1,1]]
Explanation:
- The group of farmland starts at (0, 0) and ends at (1, 1).

Example 3:
Input: land = [[0]]
Output: []
Explanation:
- There are no groups of farmland.
"""

from typing import List

def findFarmland(land: List[List[int]]) -> List[List[int]]:
    def dfs(r, c):
        """Perform DFS to find the bottom-right corner of the farmland."""
        nonlocal bottom_right_r, bottom_right_c
        if r < 0 or r >= rows or c < 0 or c >= cols or land[r][c] == 0:
            return
        # Mark the cell as visited
        land[r][c] = 0
        # Update the bottom-right corner
        bottom_right_r = max(bottom_right_r, r)
        bottom_right_c = max(bottom_right_c, c)
        # Explore all four directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    rows, cols = len(land), len(land[0])
    result = []

    for r in range(rows):
        for c in range(cols):
            if land[r][c] == 1:  # Found the top-left corner of a farmland
                top_left_r, top_left_c = r, c
                bottom_right_r, bottom_right_c = r, c
                dfs(r, c)
                result.append([top_left_r, top_left_c, bottom_right_r, bottom_right_c])

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    land1 = [[1, 0, 0], [0, 1, 1], [0, 1, 1]]
    print(findFarmland(land1))  # Expected Output: [[0, 0, 0, 0], [1, 1, 2, 2]]

    # Test Case 2
    land2 = [[1, 1], [1, 1]]
    print(findFarmland(land2))  # Expected Output: [[0, 0, 1, 1]]

    # Test Case 3
    land3 = [[0]]
    print(findFarmland(land3))  # Expected Output: []

    # Test Case 4
    land4 = [[1, 0, 1], [0, 0, 0], [1, 1, 1]]
    print(findFarmland(land4))  # Expected Output: [[0, 0, 0, 0], [0, 2, 0, 2], [2, 0, 2, 2]]

# Time Complexity Analysis:
# - The algorithm visits each cell of the grid at most once. Therefore, the time complexity is O(m * n), 
#   where m is the number of rows and n is the number of columns.

# Space Complexity Analysis:
# - The space complexity is O(m * n) in the worst case due to the recursion stack in the DFS.

# Topic: Arrays, Depth-First Search (DFS)