"""
LeetCode Problem #63: Unique Paths II

Problem Statement:
A robot is located at the top-left corner of a `m x n` grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as `1` and `0` respectively in the grid.

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid. There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

Constraints:
- `m == obstacleGrid.length`
- `n == obstacleGrid[i].length`
- `1 <= m, n <= 100`
- `obstacleGrid[i][j]` is 0 or 1.
"""

# Python Solution
def uniquePathsWithObstacles(obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    # Get dimensions of the grid
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    
    # If the starting or ending cell is blocked, return 0
    if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
        return 0
    
    # Initialize a DP table with the same dimensions as the grid
    dp = [[0] * n for _ in range(m)]
    
    # Starting point
    dp[0][0] = 1
    
    # Fill the DP table
    for i in range(m):
        for j in range(n):
            # Skip obstacle cells
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                # Add paths from the top cell (if valid)
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                # Add paths from the left cell (if valid)
                if j > 0:
                    dp[i][j] += dp[i][j-1]
    
    # Return the number of unique paths to the bottom-right corner
    return dp[m-1][n-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    obstacleGrid1 = [[0,0,0],[0,1,0],[0,0,0]]
    print(uniquePathsWithObstacles(obstacleGrid1))  # Output: 2

    # Test Case 2
    obstacleGrid2 = [[0,1],[0,0]]
    print(uniquePathsWithObstacles(obstacleGrid2))  # Output: 1

    # Test Case 3
    obstacleGrid3 = [[1,0]]
    print(uniquePathsWithObstacles(obstacleGrid3))  # Output: 0

    # Test Case 4
    obstacleGrid4 = [[0,0],[1,0]]
    print(uniquePathsWithObstacles(obstacleGrid4))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through every cell in the `m x n` grid exactly once.
- Therefore, the time complexity is O(m * n), where `m` is the number of rows and `n` is the number of columns.

Space Complexity:
- The algorithm uses a DP table of size `m x n` to store intermediate results.
- Therefore, the space complexity is O(m * n).

Topic: Dynamic Programming (DP)
"""