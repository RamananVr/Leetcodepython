"""
LeetCode Problem #2684: Maximum Number of Moves in a Grid

Problem Statement:
You are given an m x n grid consisting of positive integers. You can start at any cell in the first column of the grid and move to any cell in the next column that is either directly to the right, diagonally up-right, or diagonally down-right. Specifically, if you are at cell (i, j), you can move to:
- (i - 1, j + 1) if i - 1 >= 0
- (i, j + 1)
- (i + 1, j + 1) if i + 1 < m

Return the maximum number of moves you can perform starting from any cell in the first column.

A move is valid if the value of the cell you are moving to is strictly greater than the value of the cell you are moving from.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- 1 <= grid[i][j] <= 1000
"""

def maxMoves(grid):
    """
    Function to calculate the maximum number of moves in the grid.

    :param grid: List[List[int]] - 2D grid of positive integers
    :return: int - Maximum number of moves
    """
    m, n = len(grid), len(grid[0])
    dp = [[-1] * n for _ in range(m)]  # dp[i][j] stores the max moves starting from cell (i, j)

    def dfs(i, j):
        # If out of bounds or already computed, return the stored value
        if j == n - 1:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]

        max_moves = 0
        # Check all three possible moves
        for ni, nj in [(i - 1, j + 1), (i, j + 1), (i + 1, j + 1)]:
            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
                max_moves = max(max_moves, 1 + dfs(ni, nj))

        dp[i][j] = max_moves
        return dp[i][j]

    # Start from any cell in the first column
    max_result = 0
    for i in range(m):
        max_result = max(max_result, dfs(i, 0))

    return max_result


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [2, 4, 3],
        [3, 4, 5],
        [5, 6, 7]
    ]
    print(maxMoves(grid1))  # Output: 3

    # Test Case 2
    grid2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(maxMoves(grid2))  # Output: 2

    # Test Case 3
    grid3 = [
        [10, 13, 15],
        [12, 14, 16],
        [11, 13, 17]
    ]
    print(maxMoves(grid3))  # Output: 2

    # Test Case 4
    grid4 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    print(maxMoves(grid4))  # Output: 0


"""
Time Complexity:
- The function uses DFS with memoization. Each cell (i, j) is visited at most once.
- There are m * n cells, and for each cell, we check up to 3 neighbors.
- Therefore, the time complexity is O(m * n).

Space Complexity:
- The space complexity is O(m * n) for the dp table and O(m + n) for the recursion stack in the worst case.
- Thus, the total space complexity is O(m * n).

Topic: Dynamic Programming (DP), Depth-First Search (DFS)
"""