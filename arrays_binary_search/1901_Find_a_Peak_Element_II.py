"""
LeetCode Problem #1901: Find a Peak Element II

Problem Statement:
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors. 
You are given a 0-indexed m x n matrix `mat` where no two adjacent cells are equal. 
Find any peak element `mat[i][j]` and return the position `[i, j]`.

You may assume that the entire matrix is surrounded by an outer perimeter with the value -∞.

You must write an algorithm that runs in O(m log n) or O(n log m) time.

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 500
- 1 <= mat[i][j] <= 10^5
- All elements in `mat` are distinct.

Example:
Input: mat = [[1, 4], [3, 2]]
Output: [0, 1]
Explanation: Both 4 and 3 are peak elements, so either [0,1] or [1,0] is acceptable.

Follow-up:
Can you solve the problem in O(m log n) or O(n log m) time?
"""

# Python Solution
def findPeakGrid(mat):
    """
    Finds a peak element in a 2D grid and returns its position.

    :param mat: List[List[int]] - 2D grid of integers
    :return: List[int] - Position [i, j] of a peak element
    """
    rows, cols = len(mat), len(mat[0])
    left, right = 0, cols - 1

    while left <= right:
        mid_col = (left + right) // 2
        max_row = 0

        # Find the row with the maximum element in the middle column
        for row in range(rows):
            if mat[row][mid_col] > mat[max_row][mid_col]:
                max_row = row

        # Check if the middle column's max element is a peak
        left_is_smaller = mid_col == 0 or mat[max_row][mid_col] > mat[max_row][mid_col - 1]
        right_is_smaller = mid_col == cols - 1 or mat[max_row][mid_col] > mat[max_row][mid_col + 1]

        if left_is_smaller and right_is_smaller:
            return [max_row, mid_col]
        elif not left_is_smaller:
            right = mid_col - 1
        else:
            left = mid_col + 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [[1, 4], [3, 2]]
    print(findPeakGrid(mat1))  # Output: [0, 1] or [1, 0]

    # Test Case 2
    mat2 = [[10, 20, 15], [21, 30, 14], [7, 16, 32]]
    print(findPeakGrid(mat2))  # Output: [1, 1] or [2, 2]

    # Test Case 3
    mat3 = [[1, 2, 3], [6, 5, 4], [7, 8, 9]]
    print(findPeakGrid(mat3))  # Output: [2, 2]

    # Test Case 4
    mat4 = [[10]]
    print(findPeakGrid(mat4))  # Output: [0, 0]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm performs a binary search on the columns, which takes O(log n) time.
- For each column, it scans all rows to find the maximum element, which takes O(m) time.
- Therefore, the overall time complexity is O(m log n).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Arrays, Binary Search