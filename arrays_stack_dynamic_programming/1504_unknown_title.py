"""
LeetCode Problem #1504: Count Submatrices With All Ones

Problem Statement:
Given an m x n binary matrix mat, return the number of submatrices that have all ones.

A submatrix is a rectangular part of the matrix. It consists of all the elements in the selected rows and columns.

Example 1:
Input: mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
Output: 13
Explanation:
There are 6 rectangles of size 1x1.
There are 2 rectangles of size 1x2.
There are 3 rectangles of size 2x1.
There is 1 rectangle of size 2x2.
There is 1 rectangle of size 3x1.
Total = 6 + 2 + 3 + 1 + 1 = 13.

Example 2:
Input: mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
Output: 24
Explanation:
There are 8 rectangles of size 1x1.
There are 5 rectangles of size 1x2.
There are 2 rectangles of size 1x3.
There are 4 rectangles of size 2x1.
There are 2 rectangles of size 2x2.
There are 2 rectangles of size 3x1.
There is 1 rectangle of size 3x2.
Total = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.

Constraints:
- 1 <= m, n <= 150
- mat[i][j] is either 0 or 1.
"""

def numSubmat(mat):
    """
    Function to count the number of submatrices with all ones.

    :param mat: List[List[int]] - A binary matrix
    :return: int - The number of submatrices with all ones
    """
    m, n = len(mat), len(mat[0])
    # Precompute the number of consecutive ones in each row
    for i in range(m):
        for j in range(1, n):
            if mat[i][j] == 1:
                mat[i][j] += mat[i][j - 1]

    result = 0
    # Iterate over each column and calculate the number of submatrices
    for j in range(n):
        stack = []
        sum_ = 0
        for i in range(m):
            count = 1
            while stack and stack[-1][0] >= mat[i][j]:
                val, cnt = stack.pop()
                sum_ -= val * cnt
                count += cnt
            stack.append((mat[i][j], count))
            sum_ += mat[i][j] * count
            result += sum_
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [[1, 0, 1],
            [1, 1, 0],
            [1, 1, 0]]
    print(numSubmat(mat1))  # Output: 13

    # Test Case 2
    mat2 = [[0, 1, 1, 0],
            [0, 1, 1, 1],
            [1, 1, 1, 0]]
    print(numSubmat(mat2))  # Output: 24

    # Test Case 3
    mat3 = [[1, 1],
            [1, 1]]
    print(numSubmat(mat3))  # Output: 9

    # Test Case 4
    mat4 = [[1, 0],
            [0, 1]]
    print(numSubmat(mat4))  # Output: 2

"""
Time Complexity:
- Precomputing the number of consecutive ones in each row takes O(m * n).
- The main loop iterates over each column, and for each column, it processes each row using a stack. 
  In the worst case, each element is pushed and popped from the stack once, resulting in O(m) operations per column.
- Overall, the time complexity is O(m * n).

Space Complexity:
- The space complexity is O(m) due to the stack used for each column.

Topic: Arrays, Stack, Dynamic Programming
"""