"""
LeetCode Question #304: Range Sum Query 2D - Immutable

Problem Statement:
Given a 2D matrix `matrix`, handle multiple queries of the following type:
- Calculate the sum of the elements of `matrix` inside the rectangle defined by its upper left corner `(row1, col1)` and lower right corner `(row2, col2)`.

Implement the `NumMatrix` class:
- `NumMatrix(matrix)` Initializes the object with the integer matrix `matrix`.
- `sumRegion(row1, col1, row2, col2)` Returns the sum of the elements of `matrix` inside the rectangle defined by its upper left corner `(row1, col1)` and lower right corner `(row2, col2)`.

You must design an efficient solution with a focus on minimizing the time complexity of the `sumRegion` method.

Constraints:
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 200`
- `-10^5 <= matrix[i][j] <= 10^5`
- `0 <= row1 <= row2 < m`
- `0 <= col1 <= col2 < n`
- At most 10^4 calls will be made to `sumRegion`.

Example:
Input:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
obj = NumMatrix(matrix)
obj.sumRegion(2, 1, 4, 3) -> 8
obj.sumRegion(1, 1, 2, 2) -> 11
obj.sumRegion(1, 2, 2, 4) -> 12
"""

class NumMatrix:
    def __init__(self, matrix):
        """
        Initialize the NumMatrix object with the given matrix.
        Precompute a prefix sum matrix to allow efficient sumRegion queries.
        """
        if not matrix or not matrix[0]:
            self.prefix_sum = []
            return
        
        m, n = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Build the prefix sum matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefix_sum[i][j] = (
                    matrix[i - 1][j - 1]
                    + self.prefix_sum[i - 1][j]
                    + self.prefix_sum[i][j - 1]
                    - self.prefix_sum[i - 1][j - 1]
                )

    def sumRegion(self, row1, col1, row2, col2):
        """
        Return the sum of the elements in the rectangle defined by (row1, col1) and (row2, col2).
        """
        return (
            self.prefix_sum[row2 + 1][col2 + 1]
            - self.prefix_sum[row1][col2 + 1]
            - self.prefix_sum[row2 + 1][col1]
            + self.prefix_sum[row1][col1]
        )


# Example Test Cases
if __name__ == "__main__":
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    obj = NumMatrix(matrix)
    
    # Test Case 1
    print(obj.sumRegion(2, 1, 4, 3))  # Output: 8
    
    # Test Case 2
    print(obj.sumRegion(1, 1, 2, 2))  # Output: 11
    
    # Test Case 3
    print(obj.sumRegion(1, 2, 2, 4))  # Output: 12


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Initialization (`__init__`): O(m * n), where `m` is the number of rows and `n` is the number of columns in the matrix. This is due to the construction of the prefix sum matrix.
   - Query (`sumRegion`): O(1), as the sum is computed using constant-time arithmetic operations on the prefix sum matrix.

2. Space Complexity:
   - The prefix sum matrix requires O(m * n) space, where `m` is the number of rows and `n` is the number of columns in the matrix.

Overall:
- Initialization: O(m * n)
- Query: O(1)
- Space: O(m * n)

Topic: Dynamic Programming (Prefix Sum)
"""