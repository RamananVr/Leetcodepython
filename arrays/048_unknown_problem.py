"""
LeetCode Problem #48: Rotate Image

Problem Statement:
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000
"""

def rotate(matrix):
    """
    Rotates the given n x n matrix 90 degrees clockwise in-place.

    :param matrix: List[List[int]] - The n x n 2D matrix to rotate
    :return: None - The matrix is modified in-place
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix1)
    print("Rotated Matrix 1:", matrix1)  # Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    # Test Case 2
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(matrix2)
    print("Rotated Matrix 2:", matrix2)  # Expected: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    # Test Case 3
    matrix3 = [[1]]
    rotate(matrix3)
    print("Rotated Matrix 3:", matrix3)  # Expected: [[1]]

    # Test Case 4
    matrix4 = [[1, 2], [3, 4]]
    rotate(matrix4)
    print("Rotated Matrix 4:", matrix4)  # Expected: [[3, 1], [4, 2]]

# Topic: Arrays