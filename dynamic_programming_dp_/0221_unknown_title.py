"""
LeetCode Problem #221: Maximal Square

Problem Statement:
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],
                 ["1","0","1","1","1"],
                 ["1","1","1","1","1"],
                 ["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],
                 ["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 300
- matrix[i][j] is '0' or '1'.
"""

# Solution
def maximalSquare(matrix):
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    max_side = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:  # First row or first column
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])

    return max_side * max_side

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matrix1 = [["1","0","1","0","0"],
               ["1","0","1","1","1"],
               ["1","1","1","1","1"],
               ["1","0","0","1","0"]]
    print(maximalSquare(matrix1))  # Output: 4

    # Test Case 2
    matrix2 = [["0","1"],
               ["1","0"]]
    print(maximalSquare(matrix2))  # Output: 1

    # Test Case 3
    matrix3 = [["0"]]
    print(maximalSquare(matrix3))  # Output: 0

    # Test Case 4
    matrix4 = [["1","1","1","1"],
               ["1","1","1","1"],
               ["1","1","1","1"],
               ["1","1","1","1"]]
    print(maximalSquare(matrix4))  # Output: 16

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through each cell in the matrix once.
- For an m x n matrix, the time complexity is O(m * n).

Space Complexity:
- The algorithm uses a 2D dp array of size m x n.
- Therefore, the space complexity is O(m * n).
- Note: The space complexity can be optimized to O(n) by using a single row of dp values.

Topic: Dynamic Programming (DP)
"""