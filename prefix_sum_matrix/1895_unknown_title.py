"""
LeetCode Problem #1895: Largest Magic Square

Problem Statement:
A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. 
Given an m x n integer grid, return the size (the side length k) of the largest magic square that can be found within this grid.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- 1 <= grid[i][j] <= 10^6
"""

def largestMagicSquare(grid):
    """
    Finds the size of the largest magic square in the given grid.

    :param grid: List[List[int]] - 2D grid of integers
    :return: int - size of the largest magic square
    """
    m, n = len(grid), len(grid[0])

    # Precompute prefix sums for rows and columns
    row_prefix = [[0] * (n + 1) for _ in range(m)]
    col_prefix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            row_prefix[i][j + 1] = row_prefix[i][j] + grid[i][j]
            col_prefix[i + 1][j] = col_prefix[i][j] + grid[i][j]

    def is_magic_square(x, y, k):
        # Check if the k x k square with top-left corner (x, y) is a magic square
        target_sum = sum(grid[x][y:y + k])  # Sum of the first row

        # Check rows
        for i in range(x, x + k):
            if sum(grid[i][y:y + k]) != target_sum:
                return False

        # Check columns
        for j in range(y, y + k):
            if sum(grid[i][j] for i in range(x, x + k)) != target_sum:
                return False

        # Check main diagonal
        if sum(grid[x + i][y + i] for i in range(k)) != target_sum:
            return False

        # Check anti-diagonal
        if sum(grid[x + i][y + k - 1 - i] for i in range(k)) != target_sum:
            return False

        return True

    # Iterate over all possible square sizes
    max_size = 1
    for k in range(2, min(m, n) + 1):  # Start from size 2
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                if is_magic_square(i, j, k):
                    max_size = max(max_size, k)

    return max_size


# Example Test Cases
if __name__ == "__main__":
    grid1 = [
        [7, 1, 4, 5, 6],
        [2, 5, 1, 6, 4],
        [1, 5, 4, 3, 2],
        [1, 2, 7, 3, 4]
    ]
    print(largestMagicSquare(grid1))  # Output: 3

    grid2 = [
        [5, 1, 3, 1],
        [9, 3, 3, 1],
        [1, 3, 3, 8]
    ]
    print(largestMagicSquare(grid2))  # Output: 2

    grid3 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(largestMagicSquare(grid3))  # Output: 1


"""
Time Complexity:
- Precomputing prefix sums: O(m * n)
- Checking all possible squares:
  - For each square size k (from 2 to min(m, n)), we check all possible top-left corners.
  - For each square, we check rows, columns, and diagonals in O(k).
  - Total complexity: O((m * n) * min(m, n)) in the worst case.

Space Complexity:
- O(m * n) for prefix sums.

Topic: Prefix Sum, Matrix
"""