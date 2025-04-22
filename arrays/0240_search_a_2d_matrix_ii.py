"""
LeetCode Question #240: Search a 2D Matrix II

Problem Statement:
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
1. Integers in each row are sorted in ascending order from left to right.
2. Integers in each column are sorted in ascending order from top to bottom.

Example:
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.
Given target = 20, return false.

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= n, m <= 300
- -10^9 <= matrix[i][j] <= 10^9
- All the integers in each row are sorted in ascending order.
- All the integers in each column are sorted in ascending order.
- -10^9 <= target <= 10^9
"""

def searchMatrix(matrix, target):
    """
    Searches for a target value in a 2D matrix with sorted rows and columns.

    :param matrix: List[List[int]], the 2D matrix
    :param target: int, the target value to search for
    :return: bool, True if the target exists in the matrix, False otherwise
    """
    if not matrix or not matrix[0]:
        return False

    # Start from the top-right corner
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return False


# Example Test Cases
if __name__ == "__main__":
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    # Test Case 1: Target exists in the matrix
    target = 5
    print(searchMatrix(matrix, target))  # Output: True

    # Test Case 2: Target does not exist in the matrix
    target = 20
    print(searchMatrix(matrix, target))  # Output: False

    # Test Case 3: Target is the smallest element
    target = 1
    print(searchMatrix(matrix, target))  # Output: True

    # Test Case 4: Target is the largest element
    target = 30
    print(searchMatrix(matrix, target))  # Output: True

    # Test Case 5: Empty matrix
    matrix = []
    target = 10
    print(searchMatrix(matrix, target))  # Output: False

    # Test Case 6: Single row matrix
    matrix = [[1, 2, 3, 4, 5]]
    target = 3
    print(searchMatrix(matrix, target))  # Output: True

    # Test Case 7: Single column matrix
    matrix = [[1], [2], [3], [4], [5]]
    target = 4
    print(searchMatrix(matrix, target))  # Output: True


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm starts at the top-right corner and moves either left or down.
- In the worst case, it traverses one row and one column, resulting in O(m + n), 
  where m is the number of rows and n is the number of columns.

Space Complexity:
- The algorithm uses constant space, O(1), as it only uses a few variables to track the current position.

Topic: Arrays
"""