"""
LeetCode Problem #1428: Leftmost Column with at Least a One

Problem Statement:
A binary matrix means that all elements in the matrix are either 0 or 1. 
For each individual row of the matrix, the 1s are sorted in non-decreasing order. 
This means that if a row contains a 1, then all the elements to the right of it are also 1.

Given a `binary matrix` with `n` rows and `m` columns, return the index (0-based) of the leftmost column with at least a 1 in it. 
If such a column does not exist, return -1.

You cannot access the binary matrix directly. You are only allowed to access the matrix using a `BinaryMatrix` interface:
- `BinaryMatrix.get(row: int, col: int) -> int`: returns the element of the matrix at index (row, col) (0-indexed).
- `BinaryMatrix.dimensions() -> List[int]`: returns a list of 2 elements [n, m], which are the number of rows and columns in the matrix, respectively.

Submissions making more than 1000 calls to `BinaryMatrix.get` will be judged as incorrect.

Constraints:
- 1 <= n, m <= 100
- BinaryMatrix.get(row, col) in {0, 1}
- BinaryMatrix.dimensions() returns dimensions of the matrix as a list [n, m].
- The matrix is guaranteed to be binary and sorted row-wise.

Follow-up:
Could you solve the problem in less than O(n * m) time complexity?
"""

# Python Solution
from typing import List

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # Get the dimensions of the matrix
        n, m = binaryMatrix.dimensions()
        
        # Start from the top-right corner of the matrix
        row, col = 0, m - 1
        leftmost_col = -1
        
        # Traverse the matrix
        while row < n and col >= 0:
            if binaryMatrix.get(row, col) == 1:
                # Update the leftmost column and move left
                leftmost_col = col
                col -= 1
            else:
                # Move down to the next row
                row += 1
        
        return leftmost_col

# Example Test Cases
class BinaryMatrix:
    """
    Mock implementation of the BinaryMatrix interface for testing purposes.
    """
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def get(self, row: int, col: int) -> int:
        return self.matrix[row][col]

    def dimensions(self) -> List[int]:
        return [len(self.matrix), len(self.matrix[0])]

# Test cases
if __name__ == "__main__":
    # Test case 1
    matrix1 = BinaryMatrix([
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 1, 1]
    ])
    solution = Solution()
    print(solution.leftMostColumnWithOne(matrix1))  # Output: 1

    # Test case 2
    matrix2 = BinaryMatrix([
        [0, 0],
        [0, 0]
    ])
    print(solution.leftMostColumnWithOne(matrix2))  # Output: -1

    # Test case 3
    matrix3 = BinaryMatrix([
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 1]
    ])
    print(solution.leftMostColumnWithOne(matrix3))  # Output: 1

    # Test case 4
    matrix4 = BinaryMatrix([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ])
    print(solution.leftMostColumnWithOne(matrix4))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm starts at the top-right corner and moves either left or down.
- In the worst case, it makes at most `n + m` moves (n rows and m columns).
- Therefore, the time complexity is O(n + m).

Space Complexity:
- The algorithm uses a constant amount of extra space.
- Therefore, the space complexity is O(1).
"""

# Topic: Matrix, Binary Search