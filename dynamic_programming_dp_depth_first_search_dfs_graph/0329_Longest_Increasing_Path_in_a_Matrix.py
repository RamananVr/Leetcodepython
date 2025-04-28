"""
LeetCode Problem #329: Longest Increasing Path in a Matrix

Problem Statement:
Given an `m x n` integers matrix, return the length of the longest increasing path in the matrix.

From each cell, you can either move in four directions: left, right, up, or down. 
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Constraints:
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 200`
- `0 <= matrix[i][j] <= 2^31 - 1`
"""

from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        memo = [[-1] * cols for _ in range(rows)]
        
        def dfs(x, y):
            if memo[x][y] != -1:
                return memo[x][y]
            
            max_length = 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] > matrix[x][y]:
                    max_length = max(max_length, 1 + dfs(nx, ny))
            
            memo[x][y] = max_length
            return max_length
        
        longest_path = 0
        for i in range(rows):
            for j in range(cols):
                longest_path = max(longest_path, dfs(i, j))
        
        return longest_path

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    matrix1 = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]
    print(solution.longestIncreasingPath(matrix1))  # Output: 4 (Path: 1 -> 2 -> 6 -> 9)

    # Test Case 2
    matrix2 = [
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1]
    ]
    print(solution.longestIncreasingPath(matrix2))  # Output: 4 (Path: 3 -> 4 -> 5 -> 6)

    # Test Case 3
    matrix3 = [[1]]
    print(solution.longestIncreasingPath(matrix3))  # Output: 1 (Path: 1)

"""
Time Complexity:
- The `dfs` function is called once for each cell in the matrix, and each call explores up to 4 neighbors.
- Since we use memoization, each cell is processed only once.
- Therefore, the time complexity is O(m * n), where `m` is the number of rows and `n` is the number of columns.

Space Complexity:
- The space complexity is O(m * n) for the memoization table.
- Additionally, the recursion stack can go as deep as the number of cells in the worst case, which is O(m * n).
- Thus, the overall space complexity is O(m * n).

Topic: Dynamic Programming (DP), Depth-First Search (DFS), Graph
"""