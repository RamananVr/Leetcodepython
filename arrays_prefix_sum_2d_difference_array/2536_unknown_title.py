"""
LeetCode Problem #2536: Increment Submatrices by One

Problem Statement:
You are given a 2D integer matrix `mat` of size `m x n` initialized with all 0's. 
You are also given a 2D integer array `queries` where each `queries[i] = [row1, col1, row2, col2]` 
describes a submatrix whose top-left corner is `(row1, col1)` and bottom-right corner is `(row2, col2)`.

For each query, increment all the elements of the submatrix by 1.

Return the matrix `mat` after performing all the queries.

Constraints:
- `1 <= m, n <= 500`
- `1 <= queries.length <= 10^4`
- `0 <= row1 <= row2 < m`
- `0 <= col1 <= col2 < n`
"""

def rangeAddQueries(m: int, n: int, queries: list[list[int]]) -> list[list[int]]:
    """
    Increment submatrices in a 2D matrix based on the given queries.
    """
    # Initialize the matrix with zeros
    mat = [[0] * n for _ in range(m)]
    
    # Apply the 2D difference array technique
    for row1, col1, row2, col2 in queries:
        mat[row1][col1] += 1
        if col2 + 1 < n:
            mat[row1][col2 + 1] -= 1
        if row2 + 1 < m:
            mat[row2 + 1][col1] -= 1
        if row2 + 1 < m and col2 + 1 < n:
            mat[row2 + 1][col2 + 1] += 1
    
    # Compute prefix sums row-wise
    for i in range(m):
        for j in range(1, n):
            mat[i][j] += mat[i][j - 1]
    
    # Compute prefix sums column-wise
    for j in range(n):
        for i in range(1, m):
            mat[i][j] += mat[i - 1][j]
    
    return mat

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    m, n = 3, 3
    queries = [[0, 0, 1, 1], [1, 1, 2, 2]]
    print(rangeAddQueries(m, n, queries))
    # Expected Output: [[1, 1, 0], [1, 2, 1], [0, 1, 1]]

    # Test Case 2
    m, n = 4, 4
    queries = [[0, 0, 3, 3], [1, 1, 2, 2]]
    print(rangeAddQueries(m, n, queries))
    # Expected Output: [[1, 1, 1, 1], [1, 2, 2, 1], [1, 2, 2, 1], [1, 1, 1, 1]]

    # Test Case 3
    m, n = 2, 2
    queries = [[0, 0, 0, 0], [1, 1, 1, 1]]
    print(rangeAddQueries(m, n, queries))
    # Expected Output: [[1, 0], [0, 1]]

"""
Time Complexity:
- Processing the queries: O(len(queries))
- Computing row-wise prefix sums: O(m * n)
- Computing column-wise prefix sums: O(m * n)
- Total: O(len(queries) + m * n)

Space Complexity:
- The space used by the matrix `mat`: O(m * n)
- Total: O(m * n)

Topic: Arrays, Prefix Sum, 2D Difference Array
"""