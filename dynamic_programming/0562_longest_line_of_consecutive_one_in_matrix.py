"""
LeetCode Question #562: Longest Line of Consecutive One in Matrix

Problem Statement:
Given an `m x n` binary matrix `mat`, return the length of the longest line of consecutive one in the matrix. 
The line could be horizontal, vertical, diagonal, or anti-diagonal.

Example 1:
Input: mat = [[0,1,1,0],
              [0,1,1,0],
              [0,0,0,1]]
Output: 3

Example 2:
Input: mat = [[1,1,1],
              [0,1,0],
              [1,1,1]]
Output: 3

Constraints:
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 10^4`
- `1 <= m * n <= 10^4`
- `mat[i][j]` is either `0` or `1`.
"""

def longestLine(mat):
    """
    Function to find the longest line of consecutive ones in a binary matrix.
    
    :param mat: List[List[int]] - The binary matrix
    :return: int - The length of the longest line of consecutive ones
    """
    if not mat or not mat[0]:
        return 0

    m, n = len(mat), len(mat[0])
    max_length = 0

    # Initialize DP arrays for horizontal, vertical, diagonal, and anti-diagonal
    dp_h = [[0] * n for _ in range(m)]  # Horizontal
    dp_v = [[0] * n for _ in range(m)]  # Vertical
    dp_d = [[0] * n for _ in range(m)]  # Diagonal
    dp_a = [[0] * n for _ in range(m)]  # Anti-diagonal

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                # Horizontal
                dp_h[i][j] = dp_h[i][j - 1] + 1 if j > 0 else 1
                # Vertical
                dp_v[i][j] = dp_v[i - 1][j] + 1 if i > 0 else 1
                # Diagonal
                dp_d[i][j] = dp_d[i - 1][j - 1] + 1 if i > 0 and j > 0 else 1
                # Anti-diagonal
                dp_a[i][j] = dp_a[i - 1][j + 1] + 1 if i > 0 and j < n - 1 else 1

                # Update the maximum length
                max_length = max(max_length, dp_h[i][j], dp_v[i][j], dp_d[i][j], dp_a[i][j])

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [[0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 1]]
    print(longestLine(mat1))  # Output: 3

    # Test Case 2
    mat2 = [[1, 1, 1],
            [0, 1, 0],
            [1, 1, 1]]
    print(longestLine(mat2))  # Output: 3

    # Test Case 3
    mat3 = [[1, 0, 0, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 1],
            [1, 1, 1, 1]]
    print(longestLine(mat3))  # Output: 4

    # Test Case 4
    mat4 = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    print(longestLine(mat4))  # Output: 0

"""
Time Complexity:
- The algorithm iterates through every cell in the matrix once, performing constant-time operations for each cell.
- Therefore, the time complexity is O(m * n), where m is the number of rows and n is the number of columns.

Space Complexity:
- The algorithm uses four auxiliary DP arrays of size m x n to store intermediate results.
- Therefore, the space complexity is O(m * n).

Topic: Dynamic Programming
"""