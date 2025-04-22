"""
LeetCode Problem #308: Range Sum Query 2D - Mutable

Problem Statement:
Given a 2D matrix `matrix`, handle multiple queries of the following types:
1. Update the value of a cell in the matrix.
2. Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) 
   and lower right corner (row2, col2).

Implement the NumMatrix class:
- NumMatrix(int[][] matrix) Initializes the object with the integer matrix `matrix`.
- void update(int row, int col, int val) Updates the value of matrix[row][col] to be `val`.
- int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle 
  defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

You must design an algorithm where `update` and `sumRegion` work in O(log(m) * log(n)) time.

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 200
- -10^5 <= matrix[i][j] <= 10^5
- -10^5 <= val <= 10^5
- 0 <= row1 <= row2 < m
- 0 <= col1 <= col2 < n
- At most 10^4 calls will be made to `update` and `sumRegion`.

"""

class NumMatrix:
    def __init__(self, matrix):
        """
        Initialize the NumMatrix object with a 2D matrix.
        Use a Binary Indexed Tree (BIT) for efficient updates and range queries.
        """
        if not matrix or not matrix[0]:
            return
        
        self.rows, self.cols = len(matrix), len(matrix[0])
        self.matrix = [[0] * self.cols for _ in range(self.rows)]
        self.BIT = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        
        for r in range(self.rows):
            for c in range(self.cols):
                self.update(r, c, matrix[r][c])

    def update(self, row, col, val):
        """
        Update the value at matrix[row][col] to val.
        """
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        r = row + 1
        while r <= self.rows:
            c = col + 1
            while c <= self.cols:
                self.BIT[r][c] += delta
                c += c & -c
            r += r & -r

    def sumRegion(self, row1, col1, row2, col2):
        """
        Return the sum of the elements in the rectangle defined by (row1, col1) and (row2, col2).
        """
        return (self._sum(row2 + 1, col2 + 1) 
                - self._sum(row1, col2 + 1) 
                - self._sum(row2 + 1, col1) 
                + self._sum(row1, col1))

    def _sum(self, row, col):
        """
        Helper function to calculate the prefix sum up to (row, col) using the BIT.
        """
        total = 0
        r = row
        while r > 0:
            c = col
            while c > 0:
                total += self.BIT[r][c]
                c -= c & -c
            r -= r & -r
        return total


# Example Test Cases
if __name__ == "__main__":
    # Initialize the matrix
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    numMatrix = NumMatrix(matrix)

    # Test sumRegion
    print(numMatrix.sumRegion(2, 1, 4, 3))  # Output: 8
    print(numMatrix.sumRegion(1, 1, 2, 2))  # Output: 11
    print(numMatrix.sumRegion(1, 2, 2, 4))  # Output: 12

    # Test update
    numMatrix.update(3, 2, 2)
    print(numMatrix.sumRegion(2, 1, 4, 3))  # Output: 10


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - `update`: O(log(m) * log(n)), where m is the number of rows and n is the number of columns. 
     This is because we update the Binary Indexed Tree (BIT) in a logarithmic manner for both rows and columns.
   - `sumRegion`: O(log(m) * log(n)), as we query the BIT for prefix sums in a logarithmic manner for both rows and columns.

2. Space Complexity:
   - O(m * n), where m is the number of rows and n is the number of columns. 
     This is the space required to store the BIT and the matrix.

Topic: Binary Indexed Tree (BIT), 2D Range Queries
"""