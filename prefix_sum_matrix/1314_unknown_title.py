"""
LeetCode Problem #1314: Matrix Block Sum

Problem Statement:
Given a `m x n` matrix `mat` and an integer `k`, return a matrix `answer` where each `answer[i][j]` is the sum of all elements 
`mat[r][c]` for:
- `i - k <= r <= i + k`
- `j - k <= c <= j + k`
- `(r, c)` is a valid position in the matrix.

Example:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]

Constraints:
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 100`
- `1 <= mat[i][j] <= 100`
- `0 <= k <= min(m, n)`
"""

# Solution
def matrixBlockSum(mat, k):
    """
    Calculate the matrix block sum for the given matrix and k.

    :param mat: List[List[int]] - Input matrix
    :param k: int - Block size
    :return: List[List[int]] - Matrix block sum
    """
    m, n = len(mat), len(mat[0])
    
    # Step 1: Compute prefix sum matrix
    prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            prefix_sum[i + 1][j + 1] = mat[i][j] + prefix_sum[i + 1][j] + prefix_sum[i][j + 1] - prefix_sum[i][j]
    
    # Step 2: Compute the block sum using the prefix sum matrix
    answer = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            r1, c1 = max(0, i - k), max(0, j - k)
            r2, c2 = min(m - 1, i + k), min(n - 1, j + k)
            
            # Convert to prefix_sum indices
            r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1
            
            answer[i][j] = prefix_sum[r2][c2] - prefix_sum[r1 - 1][c2] - prefix_sum[r2][c1 - 1] + prefix_sum[r1 - 1][c1 - 1]
    
    return answer

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k1 = 1
    print(matrixBlockSum(mat1, k1))  # Expected Output: [[12, 21, 16], [27, 45, 33], [24, 39, 28]]

    # Test Case 2
    mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k2 = 2
    print(matrixBlockSum(mat2, k2))  # Expected Output: [[45, 45, 45], [45, 45, 45], [45, 45, 45]]

    # Test Case 3
    mat3 = [[1]]
    k3 = 0
    print(matrixBlockSum(mat3, k3))  # Expected Output: [[1]]

    # Test Case 4
    mat4 = [[1, 2], [3, 4]]
    k4 = 1
    print(matrixBlockSum(mat4, k4))  # Expected Output: [[10, 10], [10, 10]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Computing the prefix sum matrix takes O(m * n), where m is the number of rows and n is the number of columns.
- Calculating the block sum for each element also takes O(m * n), as we perform constant-time operations for each cell.
- Overall time complexity: O(m * n).

Space Complexity:
- The prefix sum matrix requires O((m + 1) * (n + 1)) space.
- The answer matrix requires O(m * n) space.
- Overall space complexity: O(m * n).

Topic: Prefix Sum, Matrix
"""