"""
LeetCode Question #62: Unique Paths

Problem Statement:
A robot is located at the top-left corner of a `m x n` grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
- 1 <= m, n <= 100
- The answer is guaranteed to be less than or equal to 2 * 10^9.
"""

# Clean, Correct Python Solution
def uniquePaths(m: int, n: int) -> int:
    """
    Calculate the number of unique paths in an m x n grid using dynamic programming.

    :param m: Number of rows in the grid.
    :param n: Number of columns in the grid.
    :return: Number of unique paths from top-left to bottom-right.
    """
    # Create a 2D DP table initialized with 1s
    dp = [[1] * n for _ in range(m)]
    
    # Fill the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    # The bottom-right cell contains the result
    return dp[m - 1][n - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    m1, n1 = 3, 7
    print(f"Unique paths for grid {m1}x{n1}: {uniquePaths(m1, n1)}")  # Expected Output: 28

    # Test Case 2
    m2, n2 = 3, 2
    print(f"Unique paths for grid {m2}x{n2}: {uniquePaths(m2, n2)}")  # Expected Output: 3

    # Test Case 3
    m3, n3 = 1, 1
    print(f"Unique paths for grid {m3}x{n3}: {uniquePaths(m3, n3)}")  # Expected Output: 1

    # Test Case 4
    m4, n4 = 10, 10
    print(f"Unique paths for grid {m4}x{n4}: {uniquePaths(m4, n4)}")  # Expected Output: 48620

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through all cells in the m x n grid.
- Therefore, the time complexity is O(m * n).

Space Complexity:
- The algorithm uses a 2D DP table of size m x n.
- Therefore, the space complexity is O(m * n).
"""

# Topic: Dynamic Programming