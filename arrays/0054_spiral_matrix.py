"""
LeetCode Question #54: Spiral Matrix

Problem Statement:
Given an m x n matrix, return all elements of the matrix in spiral order.

You must traverse the matrix in the following order:
- Start from the top-left corner and move right across the first row.
- Then move down the last column.
- Then move left across the last row.
- Then move up the first column.
- Repeat the process for the inner sub-matrix until all elements are traversed.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100
"""

# Clean, Correct Python Solution
def spiralOrder(matrix):
    """
    Returns the elements of the matrix in spiral order.

    :param matrix: List[List[int]] - The input matrix
    :return: List[int] - The elements in spiral order
    """
    result = []
    while matrix:
        # Add the first row
        result += matrix.pop(0)
        # Add the last column
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        # Add the last row in reverse order
        if matrix:
            result += matrix.pop()[::-1]
        # Add the first column in reverse order
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(spiralOrder(matrix1))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

    # Test Case 2
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(spiralOrder(matrix2))  # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    # Test Case 3
    matrix3 = [[1]]
    print(spiralOrder(matrix3))  # Output: [1]

    # Test Case 4
    matrix4 = [[1, 2], [3, 4]]
    print(spiralOrder(matrix4))  # Output: [1, 2, 4, 3]

    # Test Case 5
    matrix5 = [[1, 2, 3]]
    print(spiralOrder(matrix5))  # Output: [1, 2, 3]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm processes each element of the matrix exactly once.
- If the matrix has m rows and n columns, the total number of elements is m * n.
- Therefore, the time complexity is O(m * n).

Space Complexity:
- The algorithm uses a list `result` to store the output, which contains all elements of the matrix.
- The space complexity for the result list is O(m * n).
- Additionally, the input matrix is modified in-place (rows are popped), but no extra space is used beyond the result list.
- Therefore, the overall space complexity is O(m * n).

Primary Topic: Arrays
"""