"""
LeetCode Question #867: Transpose Matrix

Problem Statement:
Given a 2D integer array `matrix`, return the transpose of `matrix`.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

Constraints:
- `m == matrix.length`
- `n == matrix[i].length`
- 1 <= m, n <= 1000
- 1 <= matrix[i][j] <= 10^9
"""

def transpose(matrix):
    """
    Transpose the given 2D matrix.

    Args:
    matrix (List[List[int]]): A 2D list representing the input matrix.

    Returns:
    List[List[int]]: The transposed matrix.
    """
    # Use list comprehension to construct the transposed matrix
    return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Input:", matrix1)
    print("Output:", transpose(matrix1))  # Expected: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    # Test Case 2
    matrix2 = [[1, 2, 3], [4, 5, 6]]
    print("Input:", matrix2)
    print("Output:", transpose(matrix2))  # Expected: [[1, 4], [2, 5], [3, 6]]

    # Test Case 3
    matrix3 = [[1]]
    print("Input:", matrix3)
    print("Output:", transpose(matrix3))  # Expected: [[1]]

    # Test Case 4
    matrix4 = [[1, 2], [3, 4], [5, 6]]
    print("Input:", matrix4)
    print("Output:", transpose(matrix4))  # Expected: [[1, 3, 5], [2, 4, 6]]

"""
Time Complexity Analysis:
- Let `m` be the number of rows and `n` be the number of columns in the input matrix.
- The algorithm iterates over all `m * n` elements of the matrix exactly once to construct the transposed matrix.
- Therefore, the time complexity is O(m * n).

Space Complexity Analysis:
- The algorithm creates a new matrix to store the transposed result, which requires O(m * n) additional space.
- Hence, the space complexity is O(m * n).

Topic: Arrays
"""