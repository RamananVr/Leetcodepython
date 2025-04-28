"""
LeetCode Problem #2245: Maximum Trailing Zeros in a Cornered Path

Problem Statement:
You are given a 2D integer array `grid` of size `m x n`, where each cell contains a positive integer. 
A cornered path is defined as a path that starts at any cell in the grid and ends at any cell in the grid, 
and consists of a sequence of moves that are either "right" or "down". The path must form a corner, 
meaning it must consist of two segments: one segment of moves in the "right" direction and one segment 
of moves in the "down" direction (or vice versa).

The trailing zeros of a number are the number of consecutive zeros in its decimal representation, 
starting from the least significant digit. For example, the number 100 has two trailing zeros, 
and the number 123 has zero trailing zeros.

Your task is to find the maximum number of trailing zeros that can be obtained in the product of 
the values along any cornered path in the grid.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10^3`
- `1 <= grid[i][j] <= 10^9`

Example:
Input: grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]
Output: 3
Explanation: The cornered path with the maximum trailing zeros is highlighted in the grid.

"""

# Python Solution
def maxTrailingZeros(grid):
    def count_factors(num, factor):
        """Helper function to count the number of times `factor` divides `num`."""
        count = 0
        while num % factor == 0:
            num //= factor
            count += 1
        return count

    m, n = len(grid), len(grid[0])

    # Precompute the number of 2s and 5s in each cell
    twos = [[0] * n for _ in range(m)]
    fives = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            twos[i][j] = count_factors(grid[i][j], 2)
            fives[i][j] = count_factors(grid[i][j], 5)

    # Precompute prefix sums for rows and columns
    row_twos = [[0] * (n + 1) for _ in range(m)]
    row_fives = [[0] * (n + 1) for _ in range(m)]
    col_twos = [[0] * n for _ in range(m + 1)]
    col_fives = [[0] * n for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            row_twos[i][j + 1] = row_twos[i][j] + twos[i][j]
            row_fives[i][j + 1] = row_fives[i][j] + fives[i][j]

    for j in range(n):
        for i in range(m):
            col_twos[i + 1][j] = col_twos[i][j] + twos[i][j]
            col_fives[i + 1][j] = col_fives[i][j] + fives[i][j]

    # Calculate the maximum trailing zeros for all possible cornered paths
    max_zeros = 0
    for i in range(m):
        for j in range(n):
            # Four possible cornered paths
            left_twos = row_twos[i][j]
            left_fives = row_fives[i][j]
            right_twos = row_twos[i][n] - row_twos[i][j + 1]
            right_fives = row_fives[i][n] - row_fives[i][j + 1]
            up_twos = col_twos[i][j]
            up_fives = col_fives[i][j]
            down_twos = col_twos[m][j] - col_twos[i + 1][j]
            down_fives = col_fives[m][j] - col_fives[i + 1][j]

            # Combine the segments to form cornered paths
            max_zeros = max(max_zeros,
                            min(left_twos + up_twos, left_fives + up_fives),
                            min(left_twos + down_twos, left_fives + down_fives),
                            min(right_twos + up_twos, right_fives + up_fives),
                            min(right_twos + down_twos, right_fives + down_fives))

    return max_zeros

# Example Test Cases
if __name__ == "__main__":
    grid1 = [[23, 17, 15, 3, 20],
             [8, 1, 20, 27, 11],
             [9, 4, 6, 2, 21],
             [40, 9, 1, 10, 6],
             [22, 7, 4, 5, 3]]
    print(maxTrailingZeros(grid1))  # Output: 3

    grid2 = [[10, 5], [2, 1]]
    print(maxTrailingZeros(grid2))  # Output: 1

    grid3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print(maxTrailingZeros(grid3))  # Output: 0

# Time and Space Complexity Analysis
# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the grid.
# - Precomputing the factors of 2 and 5 for each cell takes O(m * n).
# - Calculating prefix sums for rows and columns takes O(m * n).
# - Iterating through each cell to calculate the maximum trailing zeros takes O(m * n).

# Space Complexity: O(m * n), for storing the `twos`, `fives`, `row_twos`, `row_fives`, `col_twos`, and `col_fives` arrays.

# Topic: Dynamic Programming, Prefix Sum, Grid