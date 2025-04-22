"""
LeetCode Problem #861: Score After Flipping Matrix

Problem Statement:
You are given a binary matrix `grid` of size `m x n`. A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0s to 1s and all 1s to 0s).

After making any number of moves, every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.

Example:
Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggling the first row results in [[1,1,0,0],[1,0,1,0],[1,1,0,0]].
The score is then 1*2^3 + 1*2^2 + 0*2^1 + 0*2^0 + 1*2^3 + 0*2^2 + 1*2^1 + 0*2^0 + 1*2^3 + 1*2^2 + 0*2^1 + 0*2^0 = 39.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 20`
- `grid[i][j]` is either `0` or `1`.
"""

def matrixScore(grid):
    """
    Calculate the highest possible score of the binary matrix after flipping rows and columns.

    :param grid: List[List[int]] - Binary matrix
    :return: int - Maximum score
    """
    m, n = len(grid), len(grid[0])

    # Step 1: Ensure the first column is all 1s by flipping rows if necessary
    for row in grid:
        if row[0] == 0:
            for j in range(n):
                row[j] = 1 - row[j]

    # Step 2: Maximize the score by flipping columns
    for col in range(1, n):
        # Count the number of 1s in the current column
        ones_count = sum(row[col] for row in grid)
        # If there are more 0s than 1s, flip the column
        if ones_count < m - ones_count:
            for row in grid:
                row[col] = 1 - row[col]

    # Step 3: Calculate the final score
    score = 0
    for row in grid:
        binary_number = int("".join(map(str, row)), 2)
        score += binary_number

    return score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    print(matrixScore(grid1))  # Output: 39

    # Test Case 2
    grid2 = [[0,1],[1,1]]
    print(matrixScore(grid2))  # Output: 5

    # Test Case 3
    grid3 = [[1,0,0],[0,1,1],[1,1,0]]
    print(matrixScore(grid3))  # Output: 14

"""
Time and Space Complexity Analysis:

Time Complexity:
- Step 1: Flipping rows to ensure the first column is all 1s takes O(m * n), where m is the number of rows and n is the number of columns.
- Step 2: Flipping columns to maximize the score takes O(m * n), as we iterate through each column and potentially flip all rows.
- Step 3: Calculating the score takes O(m * n), as we convert each row to a binary number and sum them up.
- Overall time complexity: O(m * n).

Space Complexity:
- The algorithm uses O(1) additional space, as it modifies the input matrix in place and uses a few variables for calculations.
- Overall space complexity: O(1).

Topic: Arrays
"""