"""
LeetCode Problem #2314: "Matrix Diagonal Sum"

Problem Statement:
You are given a 2D integer matrix `mat` of size `n x n` where `n` is odd. The matrix is square, meaning it has the same number of rows and columns. Your task is to return the sum of the matrix's primary diagonal and secondary diagonal.

The primary diagonal of a matrix is the diagonal that runs from the top-left corner to the bottom-right corner. The secondary diagonal of a matrix is the diagonal that runs from the top-right corner to the bottom-left corner.

Note:
- The element at the intersection of the primary and secondary diagonal is only counted once.

Constraints:
- `n == mat.length == mat[i].length`
- `1 <= n <= 1000`
- `1 <= mat[i][j] <= 10^5`
"""

def diagonalSum(mat):
    """
    Calculate the sum of the primary and secondary diagonals of a square matrix.

    Args:
    mat (List[List[int]]): A 2D list representing the square matrix.

    Returns:
    int: The sum of the primary and secondary diagonals.
    """
    n = len(mat)
    total_sum = 0

    for i in range(n):
        # Add the primary diagonal element
        total_sum += mat[i][i]
        # Add the secondary diagonal element
        total_sum += mat[i][n - i - 1]

    # If n is odd, subtract the middle element (it was added twice)
    if n % 2 == 1:
        total_sum -= mat[n // 2][n // 2]

    return total_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(diagonalSum(mat1))  # Output: 25

    # Test Case 2
    mat2 = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    print(diagonalSum(mat2))  # Output: 8

    # Test Case 3
    mat3 = [
        [5]
    ]
    print(diagonalSum(mat3))  # Output: 5

    # Test Case 4
    mat4 = [
        [1, 2],
        [3, 4]
    ]
    print(diagonalSum(mat4))  # Output: 10

"""
Time Complexity:
- The function iterates through the rows of the matrix once, performing O(1) operations for each row.
- Therefore, the time complexity is O(n), where n is the number of rows (or columns) in the matrix.

Space Complexity:
- The function uses a constant amount of extra space, regardless of the size of the input matrix.
- Therefore, the space complexity is O(1).

Topic: Arrays, Matrix
"""