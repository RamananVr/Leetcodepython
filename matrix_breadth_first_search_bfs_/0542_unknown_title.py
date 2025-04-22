"""
LeetCode Problem #542: 01 Matrix

Problem Statement:
Given an `m x n` binary matrix `mat`, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Constraints:
1. m == mat.length
2. n == mat[i].length
3. 1 <= m, n <= 10^4
4. 1 <= m * n <= 10^4
5. mat[i][j] is either 0 or 1.
6. There is at least one 0 in `mat`.

Example:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Explanation:
- The distance from cell (1, 1) to the nearest 0 is 1.
- The distance from cell (2, 1) to the nearest 0 is 2.
- All other cells already contain 0, so their distance is 0.

Approach:
We can solve this problem using a Breadth-First Search (BFS) approach. Start by adding all the cells with value 0 to a queue and initialize the distance for these cells as 0. Then, perform a multi-source BFS to calculate the distance for all other cells.

"""

from collections import deque
from typing import List

def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    # Dimensions of the matrix
    rows, cols = len(mat), len(mat[0])
    
    # Initialize the result matrix with a large value for cells with 1
    # and 0 for cells with 0
    dist = [[float('inf')] * cols for _ in range(rows)]
    queue = deque()
    
    # Add all 0 cells to the queue and set their distance to 0
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                dist[r][c] = 0
                queue.append((r, c))
    
    # Directions for moving up, down, left, right
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Perform BFS
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # If the new cell is within bounds and we find a shorter distance
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] > dist[r][c] + 1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
    
    return dist

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [[0,0,0],[0,1,0],[1,1,1]]
    print("Input:", mat1)
    print("Output:", updateMatrix(mat1))  # Expected: [[0,0,0],[0,1,0],[1,2,1]]

    # Test Case 2
    mat2 = [[0,1,1],[1,1,1],[1,1,0]]
    print("Input:", mat2)
    print("Output:", updateMatrix(mat2))  # Expected: [[0,1,2],[1,2,1],[1,1,0]]

    # Test Case 3
    mat3 = [[0,1],[1,1]]
    print("Input:", mat3)
    print("Output:", updateMatrix(mat3))  # Expected: [[0,1],[1,2]]

"""
Time Complexity:
- The BFS visits each cell at most once, and for each cell, we check its four neighbors.
- Therefore, the time complexity is O(m * n), where m is the number of rows and n is the number of columns.

Space Complexity:
- The space complexity is O(m * n) due to the `dist` matrix and the queue used for BFS.

Topic: Matrix, Breadth-First Search (BFS)
"""