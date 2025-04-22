"""
LeetCode Question #931: Minimum Falling Path Sum

Problem Statement:
Given an `n x n` array of integers `matrix`, return the minimum sum of any falling path through `matrix`.

A falling path starts at any element in the first row and chooses one element from the next row that is either directly below or diagonally left/right. Specifically, the next element from position `(row, col)` will be `(row + 1, col - 1)`, `(row + 1, col)`, or `(row + 1, col + 1)`.

The path continues until reaching the last row. The sum of a falling path is the sum of the values of the cells visited.

Constraints:
- `n == matrix.length == matrix[i].length`
- `1 <= n <= 100`
- `-100 <= matrix[i][j] <= 100`
"""

def minFallingPathSum(matrix):
    """
    Finds the minimum falling path sum in the given matrix.

    :param matrix: List[List[int]] - The input n x n matrix.
    :return: int - The minimum sum of any falling path through the matrix.
    """
    n = len(matrix)
    
    # Start from the second-to-last row and move upwards
    for row in range(n - 2, -1, -1):
        for col in range(n):
            # Calculate the minimum sum for the current cell
            best_below = matrix[row + 1][col]
            if col > 0:
                best_below = min(best_below, matrix[row + 1][col - 1])
            if col < n - 1:
                best_below = min(best_below, matrix[row + 1][col + 1])
            matrix[row][col] += best_below
    
    # The minimum falling path sum will be the minimum value in the first row
    return min(matrix[0])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    matrix1 = [
        [2, 1, 3],
        [6, 5, 4],
        [7, 8, 9]
    ]
    print(minFallingPathSum(matrix1))  # Output: 13

    # Test Case 2
    matrix2 = [
        [-19, 57],
        [-40, -5]
    ]
    print(minFallingPathSum(matrix2))  # Output: -59

    # Test Case 3
    matrix3 = [
        [1]
    ]
    print(minFallingPathSum(matrix3))  # Output: 1

    # Test Case 4
    matrix4 = [
        [100, -42, -46, -41],
        [31, 97, 10, -10],
        [-58, -51, 82, 89],
        [51, 81, 69, -51]
    ]
    print(minFallingPathSum(matrix4))  # Output: -36

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through each cell of the matrix once.
- There are `n` rows and `n` columns, so the total number of cells is `n * n`.
- For each cell, we perform a constant amount of work (checking up to 3 neighboring cells).
- Therefore, the time complexity is O(n^2).

Space Complexity:
- The algorithm modifies the input matrix in place, so no additional space is used.
- The space complexity is O(1).

Topic: Dynamic Programming
"""