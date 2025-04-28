"""
LeetCode Problem #1572: Matrix Diagonal Sum

Problem Statement:
Given a square matrix `mat`, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

Example 1:
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25. Notice that element mat[1][1] = 5 is counted only once.

Example 2:
Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

Example 3:
Input: mat = [[5]]
Output: 5

Constraints:
- `n == mat.length == mat[i].length`
- `1 <= n <= 100`
- `1 <= mat[i][j] <= 100`
"""

# Python Solution
def diagonalSum(mat):
    """
    Calculate the sum of the primary and secondary diagonals of a square matrix.
    
    :param mat: List[List[int]] - A square matrix
    :return: int - The sum of the diagonals
    """
    n = len(mat)
    total_sum = 0
    
    for i in range(n):
        # Add primary diagonal element
        total_sum += mat[i][i]
        # Add secondary diagonal element (if not overlapping with primary diagonal)
        if i != n - i - 1:
            total_sum += mat[i][n - i - 1]
    
    return total_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    print(diagonalSum(mat1))  # Output: 25

    # Test Case 2
    mat2 = [[1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]]
    print(diagonalSum(mat2))  # Output: 8

    # Test Case 3
    mat3 = [[5]]
    print(diagonalSum(mat3))  # Output: 5

    # Test Case 4
    mat4 = [[10, 20, 30],
            [40, 50, 60],
            [70, 80, 90]]
    print(diagonalSum(mat4))  # Output: 250

# Time and Space Complexity Analysis
"""
Time Complexity:
The function iterates through each row of the matrix once (O(n)), where `n` is the size of the matrix.
Accessing elements in the matrix is O(1), so the overall time complexity is O(n).

Space Complexity:
The function uses a constant amount of extra space (O(1)) to store the sum and loop variables.
Thus, the space complexity is O(1).
"""

# Topic: Arrays