"""
LeetCode Problem #1292: Maximum Side Length of a Square with Sum Less than or Equal to Threshold

Problem Statement:
Given a `m x n` matrix `mat` and an integer `threshold`, return the maximum side length of a square 
with a sum less than or equal to `threshold` or return 0 if there is no such square.

Example:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], threshold = 8
Output: 2
Explanation: The largest square with a sum less than or equal to 8 is of side length 2.

Constraints:
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 300`
- `0 <= mat[i][j] <= 10^4`
- `0 <= threshold <= 10^5`
"""

# Solution
def maxSideLength(mat, threshold):
    def get_prefix_sum(matrix):
        """Compute the prefix sum matrix."""
        m, n = len(matrix), len(matrix[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = matrix[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]
        return prefix

    def get_square_sum(prefix, x1, y1, x2, y2):
        """Get the sum of the square using the prefix sum matrix."""
        return prefix[x2 + 1][y2 + 1] - prefix[x1][y2 + 1] - prefix[x2 + 1][y1] + prefix[x1][y1]

    m, n = len(mat), len(mat[0])
    prefix = get_prefix_sum(mat)
    max_side = 0

    for side in range(1, min(m, n) + 1):
        found = False
        for i in range(m - side + 1):
            for j in range(n - side + 1):
                if get_square_sum(prefix, i, j, i + side - 1, j + side - 1) <= threshold:
                    max_side = side
                    found = True
                    break
            if found:
                break

    return max_side

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    threshold1 = 8
    print(maxSideLength(mat1, threshold1))  # Output: 2

    # Test Case 2
    mat2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    threshold2 = 4
    print(maxSideLength(mat2, threshold2))  # Output: 2

    # Test Case 3
    mat3 = [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
    threshold3 = 5
    print(maxSideLength(mat3, threshold3))  # Output: 0

    # Test Case 4
    mat4 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    threshold4 = 15
    print(maxSideLength(mat4, threshold4))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Computing the prefix sum matrix takes O(m * n).
- For each possible side length (up to min(m, n)), we iterate over the matrix to check all possible squares.
  This takes O(m * n * min(m, n)) in the worst case.
- Overall time complexity: O(m * n * min(m, n)).

Space Complexity:
- The prefix sum matrix requires O(m * n) space.
- Overall space complexity: O(m * n).
"""

# Topic: Prefix Sum, Matrix