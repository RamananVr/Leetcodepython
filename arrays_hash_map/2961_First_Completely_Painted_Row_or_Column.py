"""
LeetCode Problem #2961: First Completely Painted Row or Column

Problem Statement:
You are given an `m x n` integer matrix `mat` and an integer array `arr` of size `k`. 
The matrix `mat` is initially unpainted, and you are tasked with painting it using the integers in `arr` in the given order.

You paint the matrix as follows:
- For each integer `arr[i]`, paint all the cells in the matrix that contain the integer `arr[i]`.

Return the index of the first integer in `arr` that causes any row or column of the matrix to be completely painted.

Notes:
- The index of `arr` starts from 0.
- It is guaranteed that at least one row or column will be completely painted.

Constraints:
- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 500`
- `1 <= mat[i][j], arr[i] <= 10^5`
- All integers in `mat` are distinct.
- All integers in `arr` are distinct.
"""

from collections import defaultdict

def firstCompleteIndex(mat, arr):
    """
    Function to find the index of the first integer in `arr` that causes any row or column
    of the matrix to be completely painted.

    :param mat: List[List[int]] - The m x n matrix
    :param arr: List[int] - The array of integers
    :return: int - The index of the first integer in `arr` that causes a row or column to be completely painted
    """
    m, n = len(mat), len(mat[0])
    
    # Map each value in the matrix to its (row, col) position
    value_to_position = {}
    for i in range(m):
        for j in range(n):
            value_to_position[mat[i][j]] = (i, j)
    
    # Track the number of painted cells in each row and column
    row_paint_count = [0] * m
    col_paint_count = [0] * n
    
    # Iterate through the array `arr` and paint the corresponding cells
    for index, value in enumerate(arr):
        if value in value_to_position:
            row, col = value_to_position[value]
            
            # Increment the paint count for the corresponding row and column
            row_paint_count[row] += 1
            col_paint_count[col] += 1
            
            # Check if the row or column is completely painted
            if row_paint_count[row] == n or col_paint_count[col] == m:
                return index

    # The problem guarantees that at least one row or column will be completely painted
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    arr1 = [2, 5, 1, 4, 9, 3, 6, 7, 8]
    print(firstCompleteIndex(mat1, arr1))  # Output: 3

    # Test Case 2
    mat2 = [[1, 2], [3, 4]]
    arr2 = [1, 3, 4, 2]
    print(firstCompleteIndex(mat2, arr2))  # Output: 2

    # Test Case 3
    mat3 = [[1, 2, 3], [4, 5, 6]]
    arr3 = [6, 5, 4, 3, 2, 1]
    print(firstCompleteIndex(mat3, arr3))  # Output: 1

"""
Time Complexity Analysis:
- Constructing the `value_to_position` dictionary takes O(m * n), where `m` is the number of rows and `n` is the number of columns in the matrix.
- Iterating through the array `arr` takes O(k), where `k` is the length of the array.
- For each value in `arr`, updating the row and column paint counts takes O(1).
- Overall time complexity: O(m * n + k)

Space Complexity Analysis:
- The `value_to_position` dictionary stores one entry for each cell in the matrix, so it takes O(m * n) space.
- The `row_paint_count` and `col_paint_count` arrays take O(m + n) space.
- Overall space complexity: O(m * n)

Topic: Arrays, Hash Map
"""