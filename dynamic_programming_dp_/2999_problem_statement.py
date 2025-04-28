"""
LeetCode Question #2999: Problem Statement

Problem:
You are given a grid of size m x n consisting of non-negative integers. Each cell in the grid represents the cost of stepping on that cell. 
You are initially positioned at the top-left corner of the grid (0, 0) and want to reach the bottom-right corner (m-1, n-1). 
You can only move either down or right at any point in time.

Return the minimum cost to reach the bottom-right corner of the grid.

Constraints:
1. m == grid.length
2. n == grid[i].length
3. 1 <= m, n <= 100
4. 0 <= grid[i][j] <= 1000
"""

# Solution
def minPathSum(grid):
    """
    Function to calculate the minimum path sum in a grid.
    
    :param grid: List[List[int]] - 2D grid of non-negative integers
    :return: int - Minimum cost to reach the bottom-right corner
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])

    # Initialize a DP table to store the minimum cost at each cell
    dp = [[0] * n for _ in range(m)]

    # Base case: Top-left corner
    dp[0][0] = grid[0][0]

    # Fill the first row (can only come from the left)
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # Fill the first column (can only come from above)
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Fill the rest of the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    # The bottom-right corner contains the minimum path sum
    return dp[m - 1][n - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(minPathSum(grid1))  # Output: 7

    # Test Case 2
    grid2 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(minPathSum(grid2))  # Output: 12

    # Test Case 3
    grid3 = [
        [5]
    ]
    print(minPathSum(grid3))  # Output: 5

    # Test Case 4
    grid4 = [
        [1, 2],
        [1, 1]
    ]
    print(minPathSum(grid4))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through every cell in the grid exactly once.
- Therefore, the time complexity is O(m * n), where m is the number of rows and n is the number of columns.

Space Complexity:
- The algorithm uses a DP table of size m x n to store intermediate results.
- Therefore, the space complexity is O(m * n).

Topic: Dynamic Programming (DP)
"""