"""
LeetCode Question #2889: Find the Maximum Sum of a Path in a Matrix

Problem Statement:
You are given an m x n matrix `grid` consisting of non-negative integers. You can start at any cell in the first row and move to any cell in the last row by following these rules:
1. You can move directly downward to the cell below.
2. You can move diagonally downward to the left or right.

Return the maximum sum of a path from the first row to the last row.

Example:
Input: grid = [[5, 3, 2], [1, 4, 6], [7, 8, 9]]
Output: 18
Explanation: The path with the maximum sum is 5 -> 4 -> 9.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- 0 <= grid[i][j] <= 10^4
"""

# Solution
def maxPathSum(grid):
    """
    Finds the maximum sum of a path from the first row to the last row in the given matrix.

    :param grid: List[List[int]] - The input matrix of non-negative integers.
    :return: int - The maximum sum of a path.
    """
    m, n = len(grid), len(grid[0])
    
    # Create a DP table to store the maximum sum at each cell
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the first row of the DP table
    for j in range(n):
        dp[0][j] = grid[0][j]
    
    # Fill the DP table row by row
    for i in range(1, m):
        for j in range(n):
            # Calculate the maximum sum for the current cell
            dp[i][j] = grid[i][j] + max(
                dp[i-1][j],  # Directly above
                dp[i-1][j-1] if j > 0 else 0,  # Diagonally left
                dp[i-1][j+1] if j < n-1 else 0  # Diagonally right
            )
    
    # The result is the maximum value in the last row of the DP table
    return max(dp[-1])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[5, 3, 2], [1, 4, 6], [7, 8, 9]]
    print(maxPathSum(grid1))  # Output: 18

    # Test Case 2
    grid2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(maxPathSum(grid2))  # Output: 21

    # Test Case 3
    grid3 = [[10, 10, 2], [1, 1, 20], [5, 5, 5]]
    print(maxPathSum(grid3))  # Output: 35

    # Test Case 4
    grid4 = [[1]]
    print(maxPathSum(grid4))  # Output: 1

    # Test Case 5
    grid5 = [[1, 2], [3, 4], [5, 6]]
    print(maxPathSum(grid5))  # Output: 12

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through each cell in the matrix once.
- There are m rows and n columns, so the time complexity is O(m * n).

Space Complexity:
- The algorithm uses a DP table of size m x n to store intermediate results.
- Therefore, the space complexity is O(m * n).
"""

# Topic: Dynamic Programming