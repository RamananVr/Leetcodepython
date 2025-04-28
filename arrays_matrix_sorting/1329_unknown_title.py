"""
LeetCode Problem #1329: Sort the Matrix Diagonally

Problem Statement:
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 100
- 1 <= mat[i][j] <= 100
"""

from collections import defaultdict
from heapq import heappush, heappop

def diagonalSort(mat):
    """
    Sorts each diagonal of the matrix in ascending order.

    :param mat: List[List[int]] - The input matrix
    :return: List[List[int]] - The matrix with sorted diagonals
    """
    # Dictionary to store the diagonals
    diagonals = defaultdict(list)

    # Populate the dictionary with diagonals
    m, n = len(mat), len(mat[0])
    for i in range(m):
        for j in range(n):
            heappush(diagonals[i - j], mat[i][j])

    # Sort the diagonals and place them back into the matrix
    for i in range(m):
        for j in range(n):
            mat[i][j] = heappop(diagonals[i - j])

    return mat

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mat1 = [
        [3, 3, 1, 1],
        [2, 2, 1, 2],
        [1, 1, 1, 2]
    ]
    print("Test Case 1 Output:", diagonalSort(mat1))
    # Expected Output: [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]]

    # Test Case 2
    mat2 = [
        [11, 25, 66, 1, 69, 7],
        [23, 55, 17, 45, 15, 52],
        [75, 31, 36, 44, 58, 8],
        [22, 27, 33, 25, 68, 4],
        [84, 28, 14, 11, 5, 50]
    ]
    print("Test Case 2 Output:", diagonalSort(mat2))
    # Expected Output: [[5, 17, 4, 1, 52, 7], [11, 11, 25, 45, 8, 69], [14, 23, 25, 44, 58, 15], [22, 27, 31, 36, 50, 66], [84, 28, 75, 33, 55, 68]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Collecting elements for each diagonal takes O(m * n), where m is the number of rows and n is the number of columns.
- Sorting each diagonal using a heap takes O(D * log(D)) for each diagonal, where D is the number of elements in the diagonal. Since the sum of all diagonal lengths is O(m * n), the total sorting time is O(m * n * log(min(m, n))).
- Placing the sorted elements back into the matrix takes O(m * n).
- Overall time complexity: O(m * n * log(min(m, n))).

Space Complexity:
- The space used by the dictionary to store diagonals is O(m * n) in the worst case.
- The heap used for sorting each diagonal also contributes to the space complexity, but it is bounded by O(min(m, n)) for the largest diagonal.
- Overall space complexity: O(m * n).
"""

# Topic: Arrays, Matrix, Sorting