"""
LeetCode Problem #766: Toeplitz Matrix

Problem Statement:
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if:
- matrix[i][j] == matrix[i-1][j-1] for all i > 0 and j > 0.

Example 1:
Input: matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: true
Explanation:
In the above matrix, every diagonal from top-left to bottom-right has the same elements.

Example 2:
Input: matrix = [
  [1,2],
  [2,2]
]
Output: false
Explanation:
The diagonal starting at matrix[1][0] is not consistent.

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 20
- 0 <= matrix[i][j] <= 99

Follow-up:
What if the matrix is stored on disk, and the memory is limited such that you can only load a few rows at a time?
"""

def isToeplitzMatrix(matrix):
    """
    Function to check if a given matrix is Toeplitz.

    :param matrix: List[List[int]] - 2D matrix
    :return: bool - True if the matrix is Toeplitz, False otherwise
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] != matrix[i-1][j-1]:
                return False
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matrix1 = [
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [9, 5, 1, 2]
    ]
    print(isToeplitzMatrix(matrix1))  # Output: True

    # Test Case 2
    matrix2 = [
        [1, 2],
        [2, 2]
    ]
    print(isToeplitzMatrix(matrix2))  # Output: False

    # Test Case 3
    matrix3 = [
        [1]
    ]
    print(isToeplitzMatrix(matrix3))  # Output: True

    # Test Case 4
    matrix4 = [
        [1, 2, 3],
        [4, 1, 2],
        [5, 4, 1]
    ]
    print(isToeplitzMatrix(matrix4))  # Output: True

    # Test Case 5
    matrix5 = [
        [1, 2, 3],
        [4, 1, 2],
        [5, 4, 0]
    ]
    print(isToeplitzMatrix(matrix5))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through all elements of the matrix except the first row and first column.
- If the matrix has m rows and n columns, the number of iterations is (m-1) * (n-1).
- Therefore, the time complexity is O(m * n).

Space Complexity:
- The function uses a constant amount of extra space (no additional data structures are used).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""