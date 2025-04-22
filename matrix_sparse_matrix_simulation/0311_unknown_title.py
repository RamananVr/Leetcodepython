"""
LeetCode Problem #311: Sparse Matrix Multiplication

Problem Statement:
Given two sparse matrices mat1 and mat2, return the result of their multiplication. 
You may assume that the number of columns in mat1 is equal to the number of rows in mat2.

A matrix is sparse if a majority of its elements are 0.

Example 1:
Input: mat1 = [[1, 0, 0], [-1, 0, 3]], mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
Output: [[7, 0, 0], [-7, 0, 3]]

Example 2:
Input: mat1 = [[0]], mat2 = [[0]]
Output: [[0]]

Constraints:
- m == mat1.length
- k == mat1[i].length
- n == mat2[0].length
- 1 <= m, k, n <= 100
- -100 <= mat1[i][j], mat2[i][j] <= 100
"""

def multiply(mat1, mat2):
    """
    Multiplies two sparse matrices mat1 and mat2.

    :param mat1: List[List[int]] - The first matrix.
    :param mat2: List[List[int]] - The second matrix.
    :return: List[List[int]] - The resulting matrix after multiplication.
    """
    m, k = len(mat1), len(mat1[0])
    k2, n = len(mat2), len(mat2[0])
    assert k == k2, "Number of columns in mat1 must equal number of rows in mat2."

    # Initialize the result matrix with zeros
    result = [[0] * n for _ in range(m)]

    # Optimize by only iterating over non-zero elements in mat1
    for i in range(m):
        for j in range(k):
            if mat1[i][j] != 0:  # Only process non-zero elements in mat1
                for l in range(n):
                    if mat2[j][l] != 0:  # Only process non-zero elements in mat2
                        result[i][l] += mat1[i][j] * mat2[j][l]

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [[1, 0, 0], [-1, 0, 3]]
    mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
    print(multiply(mat1, mat2))  # Expected Output: [[7, 0, 0], [-7, 0, 3]]

    # Test Case 2
    mat1 = [[0]]
    mat2 = [[0]]
    print(multiply(mat1, mat2))  # Expected Output: [[0]]

    # Test Case 3
    mat1 = [[1, 2, 0], [0, 0, 3]]
    mat2 = [[0, 0], [3, 4], [5, 6]]
    print(multiply(mat1, mat2))  # Expected Output: [[6, 8], [15, 18]]

    # Test Case 4
    mat1 = [[1, 0], [0, 2]]
    mat2 = [[3, 4], [5, 6]]
    print(multiply(mat1, mat2))  # Expected Output: [[3, 4], [10, 12]]

"""
Time Complexity:
- Let m = number of rows in mat1, k = number of columns in mat1 (or rows in mat2), and n = number of columns in mat2.
- In the worst case, we iterate over all non-zero elements in mat1 (O(m * k)) and for each, we iterate over all non-zero elements in the corresponding row of mat2 (O(n)).
- Thus, the worst-case time complexity is O(m * k * n).
- However, since the matrices are sparse, the actual runtime is proportional to the number of non-zero elements in mat1 and mat2.

Space Complexity:
- The space complexity is O(m * n) for the result matrix.

Topic: Matrix, Sparse Matrix, Simulation
"""