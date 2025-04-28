"""
LeetCode Problem #73: Set Matrix Zeroes

Problem Statement:
Given an m x n integer matrix `matrix`, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Constraints:
1. m == matrix.length
2. n == matrix[0].length
3. 1 <= m, n <= 200
4. -2^31 <= matrix[i][j] <= 2^31 - 1

Follow-up:
- A straightforward solution using O(m * n) space is probably a good start.
- Could you devise a constant space solution?
"""

def setZeroes(matrix):
    """
    Modify the input matrix in-place such that if an element is 0, its entire row and column are set to 0.
    
    Args:
    matrix (List[List[int]]): The input 2D matrix.
    
    Returns:
    None: The matrix is modified in-place.
    """
    rows, cols = len(matrix), len(matrix[0])
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))
    
    # Use the first row and column to mark zero rows and columns
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    # Set matrix cells to zero based on markers in the first row and column
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # Handle the first row
    if first_row_has_zero:
        for j in range(cols):
            matrix[0][j] = 0
    
    # Handle the first column
    if first_col_has_zero:
        for i in range(rows):
            matrix[i][0] = 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matrix1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    setZeroes(matrix1)
    print("Test Case 1 Output:", matrix1)  # Expected: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    # Test Case 2
    matrix2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    setZeroes(matrix2)
    print("Test Case 2 Output:", matrix2)  # Expected: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

    # Test Case 3
    matrix3 = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9]
    ]
    setZeroes(matrix3)
    print("Test Case 3 Output:", matrix3)  # Expected: [[1, 0, 3], [0, 0, 0], [7, 0, 9]]

"""
Time Complexity Analysis:
- Let m = number of rows, n = number of columns.
- The algorithm iterates over the matrix multiple times:
  1. First pass to check the first row and column for zeros: O(m + n).
  2. Second pass to mark rows and columns: O(m * n).
  3. Third pass to set zeros based on markers: O(m * n).
  4. Final pass to handle the first row and column: O(m + n).
- Total time complexity: O(m * n).

Space Complexity Analysis:
- The algorithm uses constant extra space (O(1)) by leveraging the first row and column as markers.

Topic: Arrays
"""