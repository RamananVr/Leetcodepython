"""
LeetCode Problem #2713: Maximum Strictly Increasing Cells in a Matrix

Problem Statement:
Given a 1-indexed `m x n` integer matrix `mat`, you can select any cell in the matrix as your starting point.

From any cell `(i, j)`, you can move to any other cell `(x, y)` where either:
- `x = i` and `y != j` (same row, different column), or
- `y = j` and `x != i` (same column, different row).

You can only move to a cell `(x, y)` if `mat[x][y] > mat[i][j]` (the value is strictly greater).

Return the maximum number of cells you can visit in the matrix (including the starting cell).

Constraints:
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 10^5`
- `1 <= m * n <= 10^5`
- `-10^5 <= mat[i][j] <= 10^5`
"""

from collections import defaultdict
import bisect

def maxIncreasingCells(mat):
    """
    Finds the maximum number of strictly increasing cells using DFS with memoization.
    
    :param mat: List[List[int]] - 2D matrix
    :return: int - Maximum number of cells in strictly increasing path
    """
    m, n = len(mat), len(mat[0])
    memo = {}
    
    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        max_path = 1  # At least the current cell
        current_val = mat[i][j]
        
        # Try all cells in the same row
        for col in range(n):
            if col != j and mat[i][col] > current_val:
                max_path = max(max_path, 1 + dfs(i, col))
        
        # Try all cells in the same column
        for row in range(m):
            if row != i and mat[row][j] > current_val:
                max_path = max(max_path, 1 + dfs(row, j))
        
        memo[(i, j)] = max_path
        return max_path
    
    result = 0
    for i in range(m):
        for j in range(n):
            result = max(result, dfs(i, j))
    
    return result

def maxIncreasingCellsOptimized(mat):
    """
    Optimized solution using topological sorting and dynamic programming.
    
    :param mat: List[List[int]] - 2D matrix
    :return: int - Maximum number of cells in strictly increasing path
    """
    m, n = len(mat), len(mat[0])
    
    # Create a list of all cells with their values and positions
    cells = []
    for i in range(m):
        for j in range(n):
            cells.append((mat[i][j], i, j))
    
    # Sort cells by value
    cells.sort()
    
    # dp[i][j] represents the maximum path length starting from cell (i, j)
    dp = [[0] * n for _ in range(m)]
    
    # Keep track of maximum values in each row and column
    row_max = [0] * m
    col_max = [0] * n
    
    # Process cells in increasing order of values
    i = 0
    while i < len(cells):
        # Process all cells with the same value together
        same_value_cells = []
        current_value = cells[i][0]
        
        while i < len(cells) and cells[i][0] == current_value:
            same_value_cells.append((cells[i][1], cells[i][2]))
            i += 1
        
        # Calculate dp values for all cells with the same value
        for r, c in same_value_cells:
            dp[r][c] = max(row_max[r], col_max[c]) + 1
        
        # Update row and column maximums
        for r, c in same_value_cells:
            row_max[r] = max(row_max[r], dp[r][c])
            col_max[c] = max(col_max[c], dp[r][c])
    
    # Find the maximum value in dp
    result = 0
    for i in range(m):
        for j in range(n):
            result = max(result, dp[i][j])
    
    return result

def maxIncreasingCellsSegmentTree(mat):
    """
    Solution using coordinate compression and segment trees for optimization.
    
    :param mat: List[List[int]] - 2D matrix
    :return: int - Maximum number of cells in strictly increasing path
    """
    m, n = len(mat), len(mat[0])
    
    # Group cells by value
    value_to_cells = defaultdict(list)
    for i in range(m):
        for j in range(n):
            value_to_cells[mat[i][j]].append((i, j))
    
    # Sort unique values
    unique_values = sorted(value_to_cells.keys())
    
    # dp[i][j] = maximum path length ending at cell (i, j)
    dp = [[1] * n for _ in range(m)]
    
    # For each row and column, maintain the maximum dp value seen so far
    row_max = [0] * m
    col_max = [0] * n
    
    for value in unique_values:
        cells = value_to_cells[value]
        new_dp_values = []
        
        # Calculate new dp values for all cells with this value
        for r, c in cells:
            new_val = max(row_max[r], col_max[c]) + 1
            new_dp_values.append(new_val)
        
        # Update dp and maximums
        for i, (r, c) in enumerate(cells):
            dp[r][c] = new_dp_values[i]
            row_max[r] = max(row_max[r], dp[r][c])
            col_max[c] = max(col_max[c], dp[r][c])
    
    # Return the maximum value in dp
    return max(max(row) for row in dp)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat = [[3, 1], [3, 4]]
    print(f"Matrix: {mat}")
    print(f"maxIncreasingCells: {maxIncreasingCells(mat)}")  # Output: 2
    print(f"maxIncreasingCellsOptimized: {maxIncreasingCellsOptimized(mat)}")  # Output: 2
    print(f"maxIncreasingCellsSegmentTree: {maxIncreasingCellsSegmentTree(mat)}")  # Output: 2
    print()

    # Test Case 2
    mat = [[1, 1], [1, 1]]
    print(f"Matrix: {mat}")
    print(f"maxIncreasingCells: {maxIncreasingCells(mat)}")  # Output: 1
    print(f"maxIncreasingCellsOptimized: {maxIncreasingCellsOptimized(mat)}")  # Output: 1
    print(f"maxIncreasingCellsSegmentTree: {maxIncreasingCellsSegmentTree(mat)}")  # Output: 1
    print()

    # Test Case 3
    mat = [[3, 1, 6], [-9, 5, 7]]
    print(f"Matrix: {mat}")
    print(f"maxIncreasingCells: {maxIncreasingCells(mat)}")  # Output: 4
    print(f"maxIncreasingCellsOptimized: {maxIncreasingCellsOptimized(mat)}")  # Output: 4
    print(f"maxIncreasingCellsSegmentTree: {maxIncreasingCellsSegmentTree(mat)}")  # Output: 4
    print()

    # Test Case 4
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Matrix: {mat}")
    print(f"maxIncreasingCells: {maxIncreasingCells(mat)}")  # Output: 5
    print(f"maxIncreasingCellsOptimized: {maxIncreasingCellsOptimized(mat)}")  # Output: 5
    print(f"maxIncreasingCellsSegmentTree: {maxIncreasingCellsSegmentTree(mat)}")  # Output: 5
    print()

    # Test Case 5
    mat = [[1]]
    print(f"Matrix: {mat}")
    print(f"maxIncreasingCells: {maxIncreasingCells(mat)}")  # Output: 1
    print(f"maxIncreasingCellsOptimized: {maxIncreasingCellsOptimized(mat)}")  # Output: 1

    # Validation
    assert maxIncreasingCellsOptimized([[3, 1], [3, 4]]) == 2
    assert maxIncreasingCellsSegmentTree([[1, 1], [1, 1]]) == 1
    assert maxIncreasingCellsOptimized([[3, 1, 6], [-9, 5, 7]]) == 4
    print("All test cases passed!")

"""
Time Complexity Analysis:
DFS with Memoization:
- Time complexity: O(m * n * (m + n)) in the worst case.

Optimized DP:
- Time complexity: O(m * n * log(m * n)) due to sorting.

Space Complexity Analysis:
- Space complexity: O(m * n) for memoization/DP tables and auxiliary data structures.

Topic: Dynamic Programming, Matrix, Topological Sort, DFS
"""
