"""
LeetCode Question #74: Search a 2D Matrix

Problem Statement:
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
1. Integers in each row are sorted from left to right.
2. The first integer of each row is greater than the last integer of the previous row.

Given a matrix `matrix` and a target `target`, return `true` if `target` is in the matrix or `false` otherwise.

Example 1:
Input: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 3
Output: true

Example 2:
Input: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 13
Output: false

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10^4 <= matrix[i][j], target <= 10^4
"""

# Python Solution
def searchMatrix(matrix, target):
    """
    Searches for a target value in a 2D matrix.

    :param matrix: List[List[int]], the 2D matrix
    :param target: int, the target value to search for
    :return: bool, True if the target exists in the matrix, False otherwise
    """
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        row, col = divmod(mid, n)
        mid_value = matrix[row][col]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Target exists in the matrix
    matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target1 = 3
    print(searchMatrix(matrix1, target1))  # Output: True

    # Test Case 2: Target does not exist in the matrix
    matrix2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target2 = 13
    print(searchMatrix(matrix2, target2))  # Output: False

    # Test Case 3: Single row matrix
    matrix3 = [[1, 2, 3, 4, 5]]
    target3 = 4
    print(searchMatrix(matrix3, target3))  # Output: True

    # Test Case 4: Single column matrix
    matrix4 = [[1], [3], [5], [7], [9]]
    target4 = 6
    print(searchMatrix(matrix4, target4))  # Output: False

    # Test Case 5: Empty matrix
    matrix5 = []
    target5 = 1
    print(searchMatrix(matrix5, target5))  # Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm performs a binary search on the flattened matrix, which has m * n elements.
- The time complexity is O(log(m * n)).

Space Complexity:
- The algorithm uses constant space, as no additional data structures are used.
- The space complexity is O(1).
"""

# Topic: Arrays, Binary Search