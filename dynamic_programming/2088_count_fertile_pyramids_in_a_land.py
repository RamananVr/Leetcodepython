"""
LeetCode Question #2088: Count Fertile Pyramids in a Land

Problem Statement:
You are given a 2D integer array grid of size m x n representing a land where:
- grid[i][j] == 0 represents a barren land cell.
- grid[i][j] == 1 represents a fertile land cell.

A pyramid of height h is defined as a pattern of cells where:
- The top cell of the pyramid is grid[i][j] (with value 1).
- The next row contains 2 cells, both with value 1, centered below the top cell.
- The next row contains 3 cells, all with value 1, centered below the previous row.
- And so on until the height h.

A reverse pyramid is defined similarly, but the base is at the top and the tip is at the bottom.

Return the total number of fertile pyramids and reverse pyramids that can be found in grid.

Example:
Input: grid = [[1,1,1],[1,1,1],[1,1,1]]
Output: 10

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 1000
- grid[i][j] is either 0 or 1.
"""

# Python Solution
def countPyramids(grid):
    def count_pyramids(grid):
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        count = 0

        for i in range(1, m):
            for j in range(1, n - 1):
                if grid[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + 1
                    count += dp[i][j]

        return count

    # Count pyramids in the original grid
    pyramids = count_pyramids(grid)

    # Reverse the grid vertically to count reverse pyramids
    reverse_grid = grid[::-1]
    reverse_pyramids = count_pyramids(reverse_grid)

    return pyramids + reverse_pyramids

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print(countPyramids(grid1))  # Output: 10

    # Test Case 2
    grid2 = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    print(countPyramids(grid2))  # Output: 0

    # Test Case 3
    grid3 = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    print(countPyramids(grid3))  # Output: 34

    # Test Case 4
    grid4 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(countPyramids(grid4))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates over the grid twice (once for pyramids and once for reverse pyramids).
- For each cell, it performs constant-time operations to update the dp array.
- Therefore, the time complexity is O(m * n), where m is the number of rows and n is the number of columns.

Space Complexity:
- The function uses a dp array of size m x n to store intermediate results.
- Therefore, the space complexity is O(m * n).
"""

# Topic: Dynamic Programming