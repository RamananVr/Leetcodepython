"""
LeetCode Question #566: Reshape the Matrix

Problem Statement:
In MATLAB, there is a handy function called `reshape` which can reshape an `m x n` matrix into a new one with a different size `r x c` keeping its original data. You are given an `m x n` matrix `mat` and two integers `r` and `c` representing the number of rows and columns of the reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were. If the `reshape` operation with given parameters is not possible and legal, output the original matrix.

You must implement the function `matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]`.

Constraints:
- `m == len(mat)`
- `n == len(mat[0])`
- `1 <= m, n <= 100`
- `-1000 <= mat[i][j] <= 1000`
- `1 <= r, c <= 300`

Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

Explanation:
If the reshape operation is not possible, the original matrix is returned.

"""

from typing import List

def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    # Flatten the original matrix into a single list
    flat_list = [num for row in mat for num in row]
    
    # Check if reshape is possible
    if len(flat_list) != r * c:
        return mat
    
    # Reshape the matrix
    reshaped_matrix = []
    for i in range(r):
        reshaped_matrix.append(flat_list[i * c:(i + 1) * c])
    
    return reshaped_matrix

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [[1, 2], [3, 4]]
    r1, c1 = 1, 4
    print(matrixReshape(mat1, r1, c1))  # Output: [[1, 2, 3, 4]]

    # Test Case 2
    mat2 = [[1, 2], [3, 4]]
    r2, c2 = 2, 4
    print(matrixReshape(mat2, r2, c2))  # Output: [[1, 2], [3, 4]]

    # Test Case 3
    mat3 = [[1, 2], [3, 4], [5, 6]]
    r3, c3 = 2, 3
    print(matrixReshape(mat3, r3, c3))  # Output: [[1, 2], [3, 4], [5, 6]]

    # Test Case 4
    mat4 = [[1]]
    r4, c4 = 1, 1
    print(matrixReshape(mat4, r4, c4))  # Output: [[1]]

    # Test Case 5
    mat5 = [[1, 2, 3, 4]]
    r5, c5 = 2, 2
    print(matrixReshape(mat5, r5, c5))  # Output: [[1, 2], [3, 4]]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Flattening the matrix takes O(m * n), where m is the number of rows and n is the number of columns in the original matrix.
- Reshaping the matrix takes O(r * c), where r is the number of rows and c is the number of columns in the reshaped matrix.
- Overall, the time complexity is O(m * n), as r * c == m * n when the reshape is valid.

Space Complexity:
- The flattened list requires O(m * n) space.
- The reshaped matrix requires O(r * c) space, which is equivalent to O(m * n) when the reshape is valid.
- Overall, the space complexity is O(m * n).

Topic: Arrays
"""