"""
LeetCode Problem #2174: Remove All Ones With Row and Column Flips II

Problem Statement:
You are given a binary matrix `grid` where each cell is either 0 (empty) or 1 (occupied). 
You can perform any number of operations on the matrix. In one operation, you can select any row or column and flip all the values in that row or column (i.e., change all 0s to 1s and all 1s to 0s).

Return the minimum number of operations needed to remove all 1s from the matrix.

Constraints:
- `1 <= grid.length, grid[0].length <= 10`
- `grid[i][j]` is either 0 or 1.

"""

from itertools import product

def minFlips(grid):
    """
    Function to calculate the minimum number of operations needed to remove all 1s from the matrix.
    
    :param grid: List[List[int]] - A binary matrix
    :return: int - Minimum number of operations
    """
    m, n = len(grid), len(grid[0])
    target = [[0] * n for _ in range(m)]  # Target matrix with all 0s
    min_operations = float('inf')

    # Helper function to flip a row
    def flip_row(matrix, row):
        for col in range(n):
            matrix[row][col] ^= 1

    # Helper function to flip a column
    def flip_col(matrix, col):
        for row in range(m):
            matrix[row][col] ^= 1

    # Try all combinations of row flips
    for row_mask in product([0, 1], repeat=m):
        # Create a copy of the grid
        temp_grid = [row[:] for row in grid]
        operations = 0

        # Apply row flips based on the row_mask
        for i in range(m):
            if row_mask[i] == 1:
                flip_row(temp_grid, i)
                operations += 1

        # Check if we can make the grid equal to the target by flipping columns
        valid = True
        for col in range(n):
            col_sum = sum(temp_grid[row][col] for row in range(m))
            if col_sum not in {0, m}:  # Column must be all 0s or all 1s
                valid = False
                break
            if col_sum == m:  # If all 1s, flip the column
                flip_col(temp_grid, col)
                operations += 1

        # Check if the grid matches the target
        if valid and temp_grid == target:
            min_operations = min(min_operations, operations)

    return min_operations if min_operations != float('inf') else -1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[0, 1], [1, 0]]
    print(minFlips(grid1))  # Output: 2

    # Test Case 2
    grid2 = [[1, 1, 1], [1, 0, 1], [0, 0, 0]]
    print(minFlips(grid2))  # Output: 3

    # Test Case 3
    grid3 = [[0, 0], [0, 0]]
    print(minFlips(grid3))  # Output: 0

    # Test Case 4
    grid4 = [[1, 1], [1, 1]]
    print(minFlips(grid4))  # Output: 1


"""
Time Complexity Analysis:
- The number of row flip combinations is 2^m (since each row can either be flipped or not).
- For each combination, we iterate through all columns (O(n)) and rows (O(m)).
- Thus, the overall time complexity is O(2^m * m * n).

Space Complexity Analysis:
- The space complexity is O(m * n) for the temporary grid copy.

Topic: Matrix, Bit Manipulation, Backtracking
"""