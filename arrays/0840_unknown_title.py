"""
LeetCode Problem #840: Magic Squares In Grid

Problem Statement:
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an `m x n` grid of integers, return the number of 3 x 3 magic square subgrids that appear in the grid.

A subgrid is a 3 x 3 section of the grid.

Example:
Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: The only 3x3 magic square subgrid is:
4 3 8
9 5 1
2 7 6

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `0 <= grid[i][j] <= 15`
"""

# Python Solution
def numMagicSquaresInside(grid):
    def isMagicSquare(subgrid):
        # Flatten the subgrid and check if it contains all numbers from 1 to 9
        nums = [num for row in subgrid for num in row]
        if sorted(nums) != list(range(1, 10)):
            return False
        
        # Check rows, columns, and diagonals for the magic sum
        magic_sum = 15
        rows = [sum(row) for row in subgrid]
        cols = [sum(subgrid[i][j] for i in range(3)) for j in range(3)]
        diag1 = sum(subgrid[i][i] for i in range(3))
        diag2 = sum(subgrid[i][2 - i] for i in range(3))
        
        return all(x == magic_sum for x in rows + cols + [diag1, diag2])
    
    m, n = len(grid), len(grid[0])
    count = 0
    
    # Iterate over all possible 3x3 subgrids
    for i in range(m - 2):
        for j in range(n - 2):
            subgrid = [grid[i + k][j:j + 3] for k in range(3)]
            if isMagicSquare(subgrid):
                count += 1
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[4, 3, 8, 4],
             [9, 5, 1, 9],
             [2, 7, 6, 2]]
    print(numMagicSquaresInside(grid1))  # Output: 1

    # Test Case 2
    grid2 = [[8, 1, 6],
             [3, 5, 7],
             [4, 9, 2]]
    print(numMagicSquaresInside(grid2))  # Output: 1

    # Test Case 3
    grid3 = [[10, 3, 5],
             [1, 6, 11],
             [7, 9, 2]]
    print(numMagicSquaresInside(grid3))  # Output: 0

    # Test Case 4
    grid4 = [[4, 3, 8, 4],
             [9, 5, 1, 9],
             [2, 7, 6, 2],
             [1, 2, 3, 4]]
    print(numMagicSquaresInside(grid4))  # Output: 1

# Time and Space Complexity Analysis
# Time Complexity:
# - The outer loop iterates over all possible top-left corners of 3x3 subgrids, which is O((m-2) * (n-2)).
# - For each subgrid, we check if it is a magic square, which involves constant work (O(1)).
# - Overall time complexity: O(m * n).

# Space Complexity:
# - The space used is constant (O(1)) since we only store the subgrid and intermediate sums.
# - Overall space complexity: O(1).

# Topic: Arrays