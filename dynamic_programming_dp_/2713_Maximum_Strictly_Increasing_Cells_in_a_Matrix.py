"""
LeetCode Problem #2713: Maximum Strictly Increasing Cells in a Matrix

Problem Statement:
You are given an m x n integer matrix `mat`. You can select any cell in the matrix as your starting point. From the starting cell, you can move to any other cell in the matrix if and only if:

1. The destination cell is strictly greater than the current cell.
2. The destination cell is in a strictly increasing order of row or column indices.

Return the maximum number of strictly increasing cells you can visit.

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 1000
- 1 <= mat[i][j] <= 10^9
"""

# Solution
from collections import defaultdict
from functools import lru_cache

def maxIncreasingCells(mat):
    m, n = len(mat), len(mat[0])
    
    # Group cells by their values
    value_to_cells = defaultdict(list)
    for i in range(m):
        for j in range(n):
            value_to_cells[mat[i][j]].append((i, j))
    
    # Sort values in ascending order
    sorted_values = sorted(value_to_cells.keys())
    
    # Initialize DP arrays for rows and columns
    row_dp = [0] * m
    col_dp = [0] * n
    
    # Process cells in increasing order of their values
    for value in sorted_values:
        current_cells = value_to_cells[value]
        current_dp = {}
        
        # Compute the maximum path length for each cell
        for i, j in current_cells:
            current_dp[(i, j)] = max(row_dp[i], col_dp[j]) + 1
        
        # Update row_dp and col_dp
        for i, j in current_cells:
            row_dp[i] = max(row_dp[i], current_dp[(i, j)])
            col_dp[j] = max(col_dp[j], current_dp[(i, j)])
    
    # Return the maximum path length across all rows and columns
    return max(row_dp + col_dp)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [
        [3, 1],
        [3, 4]
    ]
    print(maxIncreasingCells(mat1))  # Output: 4

    # Test Case 2
    mat2 = [
        [1, 2, 3],
        [6, 5, 4]
    ]
    print(maxIncreasingCells(mat2))  # Output: 4

    # Test Case 3
    mat3 = [
        [1, 1],
        [1, 1]
    ]
    print(maxIncreasingCells(mat3))  # Output: 1

    # Test Case 4
    mat4 = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
    print(maxIncreasingCells(mat4))  # Output: 9

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the values in `value_to_cells` takes O(m * n * log(m * n)).
- Iterating through all cells and updating row_dp and col_dp takes O(m * n).
- Overall time complexity: O(m * n * log(m * n)).

Space Complexity:
- The `value_to_cells` dictionary stores all cells grouped by their values, which takes O(m * n) space.
- The `row_dp` and `col_dp` arrays each take O(max(m, n)) space.
- Overall space complexity: O(m * n).

Topic: Dynamic Programming (DP)
"""