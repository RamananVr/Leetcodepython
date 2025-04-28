"""
LeetCode Problem #2643: Row With Maximum Ones

Problem Statement:
You are given a 0-indexed m x n binary matrix `mat`, where `mat[i][j]` is either 0 or 1.

A row `i` is called the "maximum ones row" if it contains the maximum number of 1's among all the rows. 
If there are multiple rows with the same maximum number of 1's, the row with the smallest index is chosen.

Return an array `[rowIndex, maxOnes]`, where:
- `rowIndex` is the index of the row with the maximum number of 1's.
- `maxOnes` is the number of 1's in that row.

Example 1:
Input: mat = [[0,1],[1,0]]
Output: [0,1]
Explanation: Both rows have the same number of 1's. Row 0 is chosen because it has the smallest index.

Example 2:
Input: mat = [[0,0,0],[0,1,1]]
Output: [1,2]
Explanation: Row 1 has the most 1's (2 of them).

Example 3:
Input: mat = [[0,0],[1,1],[0,0]]
Output: [1,2]
Explanation: Row 1 has the most 1's (2 of them).

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 100
- mat[i][j] is either 0 or 1.
"""

# Python Solution
from typing import List

def rowAndMaximumOnes(mat: List[List[int]]) -> List[int]:
    max_ones = 0
    row_index = -1
    
    for i, row in enumerate(mat):
        ones_count = sum(row)
        if ones_count > max_ones:
            max_ones = ones_count
            row_index = i
        elif ones_count == max_ones and i < row_index:
            row_index = i
    
    return [row_index, max_ones]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [[0, 1], [1, 0]]
    print(rowAndMaximumOnes(mat1))  # Output: [0, 1]

    # Test Case 2
    mat2 = [[0, 0, 0], [0, 1, 1]]
    print(rowAndMaximumOnes(mat2))  # Output: [1, 2]

    # Test Case 3
    mat3 = [[0, 0], [1, 1], [0, 0]]
    print(rowAndMaximumOnes(mat3))  # Output: [1, 2]

    # Test Case 4
    mat4 = [[1, 1, 1], [1, 1, 1], [0, 0, 0]]
    print(rowAndMaximumOnes(mat4))  # Output: [0, 3]

    # Test Case 5
    mat5 = [[0, 0], [0, 0], [0, 0]]
    print(rowAndMaximumOnes(mat5))  # Output: [0, 0]

"""
Time Complexity Analysis:
- Let m = number of rows and n = number of columns in the matrix.
- For each row, we calculate the sum of its elements, which takes O(n) time.
- Since there are m rows, the total time complexity is O(m * n).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""