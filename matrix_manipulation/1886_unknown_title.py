"""
LeetCode Problem #1886: Determine Whether Matrix Can Be Obtained By Rotation

Problem Statement:
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

You can rotate a matrix 90 degrees clockwise by swapping and reversing rows and columns. For example:
    Original Matrix:
    [[1, 2],
     [3, 4]]

    After 90-degree rotation:
    [[3, 1],
     [4, 2]]

Constraints:
- n == mat.length == mat[i].length
- n == target.length == target[i].length
- 1 <= n <= 10
- mat[i][j] and target[i][j] are either 0 or 1.
"""

def can_be_obtained_by_rotation(mat, target):
    """
    Determine whether the matrix `mat` can be rotated to match the matrix `target`.

    :param mat: List[List[int]] - The original matrix.
    :param target: List[List[int]] - The target matrix.
    :return: bool - True if `mat` can be rotated to match `target`, False otherwise.
    """
    def rotate_90(matrix):
        """
        Rotate the matrix 90 degrees clockwise.

        :param matrix: List[List[int]] - The matrix to rotate.
        :return: List[List[int]] - The rotated matrix.
        """
        n = len(matrix)
        return [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]

    for _ in range(4):  # Rotate up to 4 times (0, 90, 180, 270 degrees)
        if mat == target:
            return True
        mat = rotate_90(mat)
    
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Matrices match after one rotation
    mat1 = [[0, 1], [1, 0]]
    target1 = [[1, 0], [0, 1]]
    print(can_be_obtained_by_rotation(mat1, target1))  # Expected: True

    # Test Case 2: Matrices match after two rotations
    mat2 = [[0, 0, 0], [1, 0, 0], [1, 1, 1]]
    target2 = [[1, 1, 1], [0, 0, 1], [0, 0, 0]]
    print(can_be_obtained_by_rotation(mat2, target2))  # Expected: True

    # Test Case 3: Matrices do not match after any rotation
    mat3 = [[1, 1], [0, 1]]
    target3 = [[1, 0], [0, 1]]
    print(can_be_obtained_by_rotation(mat3, target3))  # Expected: False

    # Test Case 4: Matrices are already equal
    mat4 = [[1, 0], [0, 1]]
    target4 = [[1, 0], [0, 1]]
    print(can_be_obtained_by_rotation(mat4, target4))  # Expected: True

    # Test Case 5: Larger matrix with no match
    mat5 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    target5 = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
    print(can_be_obtained_by_rotation(mat5, target5))  # Expected: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- Rotating the matrix takes O(n^2) time, where n is the size of the matrix.
- We perform up to 4 rotations, so the total time complexity is O(4 * n^2) = O(n^2).

Space Complexity:
- The rotation function creates a new matrix, which requires O(n^2) space.
- No additional space is used beyond the rotated matrix, so the space complexity is O(n^2).

Topic: Matrix Manipulation
"""