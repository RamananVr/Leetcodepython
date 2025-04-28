"""
LeetCode Problem #1277: Count Square Submatrices with All Ones

Problem Statement:
Given a `m x n` binary matrix `matrix`, count the number of square submatrices that have all ones.

A square submatrix is a submatrix that is square in shape, meaning it has the same number of rows and columns. 
A square submatrix with all ones is a square submatrix where every element is 1.

Example 1:
Input: matrix = [[0,1,1,1],
                 [1,1,1,1],
                 [0,1,1,1]]
Output: 15
Explanation: 
There are 10 squares of size 1.
There are 4 squares of size 2.
There is 1 square of size 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:
Input: matrix = [[1,0,1],
                 [1,1,0],
                 [1,1,0]]
Output: 7
Explanation: 
There are 6 squares of size 1.
There is 1 square of size 2.
Total number of squares = 6 + 1 = 7.

Constraints:
- `1 <= matrix.length, matrix[0].length <= 300`
- `matrix[i][j]` is either 0 or 1.
"""

def countSquares(matrix):
    """
    Counts the number of square submatrices with all ones.

    :param matrix: List[List[int]] - A binary matrix
    :return: int - Total number of square submatrices with all ones
    """
    # Get dimensions of the matrix
    rows, cols = len(matrix), len(matrix[0])
    
    # Initialize a variable to store the total count of square submatrices
    total_squares = 0
    
    # Iterate through the matrix
    for i in range(rows):
        for j in range(cols):
            # Only process cells with value 1
            if matrix[i][j] == 1:
                # If not in the first row or column, calculate the size of the largest square ending at (i, j)
                if i > 0 and j > 0:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                # Add the size of the square ending at (i, j) to the total count
                total_squares += matrix[i][j]
    
    return total_squares

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matrix1 = [[0, 1, 1, 1],
               [1, 1, 1, 1],
               [0, 1, 1, 1]]
    print(countSquares(matrix1))  # Output: 15

    # Test Case 2
    matrix2 = [[1, 0, 1],
               [1, 1, 0],
               [1, 1, 0]]
    print(countSquares(matrix2))  # Output: 7

    # Test Case 3
    matrix3 = [[1, 1],
               [1, 1]]
    print(countSquares(matrix3))  # Output: 5

    # Test Case 4
    matrix4 = [[0, 0],
               [0, 0]]
    print(countSquares(matrix4))  # Output: 0

"""
Time Complexity Analysis:
- The algorithm iterates through every cell in the matrix once.
- For each cell, it performs a constant amount of work (checking neighbors and updating the value).
- Therefore, the time complexity is O(m * n), where m is the number of rows and n is the number of columns.

Space Complexity Analysis:
- The algorithm modifies the input matrix in place, so no additional space is used apart from a few variables.
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming (DP)
"""