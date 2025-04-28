"""
LeetCode Problem #576: Out of Boundary Paths

Problem Statement:
There is an `m x n` grid with a ball. The ball is initially at the position `[startRow, startColumn]`. 
You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid boundary). 
You can apply at most `maxMove` moves to the ball.

Given the five integers `m`, `n`, `maxMove`, `startRow`, `startColumn`, return the number of paths to move the ball out of the grid boundary. 
Since the answer can be very large, return it modulo `10^9 + 7`.

Constraints:
- `1 <= m, n <= 50`
- `0 <= maxMove <= 50`
- `0 <= startRow < m`
- `0 <= startColumn < n`
"""

# Solution
def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    MOD = 10**9 + 7

    # Edge case: If no moves are allowed, the ball cannot go out of bounds
    if maxMove == 0:
        return 0

    # Initialize a 3D DP table: dp[move][row][col]
    dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
    dp[0][startRow][startColumn] = 1

    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Count of paths leading out of bounds
    result = 0

    # Iterate over the number of moves
    for move in range(1, maxMove + 1):
        for row in range(m):
            for col in range(n):
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc
                    if 0 <= newRow < m and 0 <= newCol < n:
                        dp[move][row][col] = (dp[move][row][col] + dp[move - 1][newRow][newCol]) % MOD
                    else:
                        result = (result + dp[move - 1][row][col]) % MOD

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    m, n, maxMove, startRow, startColumn = 2, 2, 2, 0, 0
    print(findPaths(m, n, maxMove, startRow, startColumn))  # Expected Output: 6

    # Test Case 2
    m, n, maxMove, startRow, startColumn = 1, 3, 3, 0, 1
    print(findPaths(m, n, maxMove, startRow, startColumn))  # Expected Output: 12

    # Test Case 3
    m, n, maxMove, startRow, startColumn = 3, 3, 0, 1, 1
    print(findPaths(m, n, maxMove, startRow, startColumn))  # Expected Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The DP table has dimensions (maxMove + 1) x m x n.
- For each cell in the DP table, we iterate over 4 possible directions.
- Thus, the time complexity is O(maxMove * m * n * 4) = O(maxMove * m * n).

Space Complexity:
- The DP table requires O(maxMove * m * n) space.
- Therefore, the space complexity is O(maxMove * m * n).
"""

# Topic: Dynamic Programming (DP)