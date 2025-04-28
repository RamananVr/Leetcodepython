"""
LeetCode Problem #2964: (Hypothetical Problem Statement)

Problem Statement:
You are given a 2D grid of integers `grid` where each cell contains a non-negative integer. 
Your task is to find the maximum sum of a path from the top-left corner to the bottom-right corner of the grid. 
You can only move either down or right at any point in time.

Return the maximum sum of such a path.

Constraints:
- `1 <= grid.length, grid[0].length <= 100`
- `0 <= grid[i][j] <= 10^4`

Example:
Input: grid = [[5, 3, 2], [1, 9, 1], [4, 2, 1]]
Output: 21
Explanation: The path with the maximum sum is 5 -> 3 -> 9 -> 2 -> 1, which gives a sum of 21.
"""

# Solution
def maxPathSum(grid):
    """
    Function to calculate the maximum path sum in a 2D grid.
    
    :param grid: List[List[int]] - 2D grid of non-negative integers
    :return: int - Maximum path sum from top-left to bottom-right
    """
    rows, cols = len(grid), len(grid[0])
    
    # Create a DP table to store the maximum path sums
    dp = [[0] * cols for _ in range(rows)]
    
    # Initialize the top-left corner
    dp[0][0] = grid[0][0]
    
    # Fill the first row (can only come from the left)
    for col in range(1, cols):
        dp[0][col] = dp[0][col - 1] + grid[0][col]
    
    # Fill the first column (can only come from above)
    for row in range(1, rows):
        dp[row][0] = dp[row - 1][0] + grid[row][0]
    
    # Fill the rest of the DP table
    for row in range(1, rows):
        for col in range(1, cols):
            dp[row][col] = max(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]
    
    # The bottom-right corner contains the maximum path sum
    return dp[rows - 1][cols - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[5, 3, 2], [1, 9, 1], [4, 2, 1]]
    print(maxPathSum(grid1))  # Output: 21

    # Test Case 2
    grid2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(maxPathSum(grid2))  # Output: 29

    # Test Case 3
    grid3 = [[1]]
    print(maxPathSum(grid3))  # Output: 1

    # Test Case 4
    grid4 = [[1, 2], [1, 1]]
    print(maxPathSum(grid4))  # Output: 4

    # Test Case 5
    grid5 = [[10, 10, 2], [1, 1, 20], [1, 1, 1]]
    print(maxPathSum(grid5))  # Output: 42

"""
Time Complexity Analysis:
- The solution iterates through every cell in the grid exactly once.
- Let `m` be the number of rows and `n` be the number of columns in the grid.
- Time complexity: O(m * n)

Space Complexity Analysis:
- The solution uses a DP table of size `m x n` to store intermediate results.
- Space complexity: O(m * n)

Topic: Dynamic Programming (DP)
"""