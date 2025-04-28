"""
LeetCode Problem #2510: Check if There is a Path With Equal Number of 0's And 1's

Problem Statement:
You are given a 2D grid of size `m x n` consisting of only 0's and 1's. You need to determine if there exists a path from the top-left corner (0, 0) to the bottom-right corner (m-1, n-1) such that the number of 0's and 1's along the path are equal.

The path can only move in two directions: right or down.

Return `True` if such a path exists, otherwise return `False`.

Constraints:
- `1 <= m, n <= 100`
- The grid consists of only 0's and 1's.

Example:
Input: grid = [[0,1,0],[1,0,1],[0,1,0]]
Output: True
Explanation: One possible path is (0,0) -> (0,1) -> (1,1) -> (2,1) -> (2,2). This path has 2 zeros and 2 ones.

Input: grid = [[0,1],[1,1]]
Output: False
Explanation: There is no path with an equal number of 0's and 1's.
"""

from collections import defaultdict
from functools import lru_cache

def isThereAPath(grid):
    """
    Determines if there exists a path from the top-left to the bottom-right corner
    of the grid such that the number of 0's and 1's along the path are equal.

    :param grid: List[List[int]] - 2D grid of 0's and 1's
    :return: bool - True if such a path exists, False otherwise
    """
    m, n = len(grid), len(grid[0])

    @lru_cache(None)
    def dfs(x, y, balance):
        # Base case: If we reach the bottom-right corner
        if x == m - 1 and y == n - 1:
            return balance + (1 if grid[x][y] == 1 else -1) == 0

        # Update the balance based on the current cell
        balance += 1 if grid[x][y] == 1 else -1

        # If the balance is invalid (too many 1's or 0's), return False
        if abs(balance) > (m + n - 1) // 2:
            return False

        # Explore the two possible directions: right and down
        if x + 1 < m and dfs(x + 1, y, balance):
            return True
        if y + 1 < n and dfs(x, y + 1, balance):
            return True

        return False

    return dfs(0, 0, 0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    print(isThereAPath(grid1))  # Output: True

    # Test Case 2
    grid2 = [[0, 1], [1, 1]]
    print(isThereAPath(grid2))  # Output: False

    # Test Case 3
    grid3 = [[0, 0, 1], [1, 1, 0], [0, 1, 1]]
    print(isThereAPath(grid3))  # Output: True

    # Test Case 4
    grid4 = [[1, 1], [1, 1]]
    print(isThereAPath(grid4))  # Output: False

"""
Time Complexity Analysis:
- The function uses memoization to avoid redundant calculations. The state of the recursion is defined by three variables: `x`, `y`, and `balance`.
- There are at most `m * n` unique grid cells, and the range of `balance` is bounded by `-m*n` to `m*n`. However, in practice, the balance is limited to a much smaller range due to the constraints of the problem.
- Thus, the time complexity is approximately O(m * n * k), where `k` is the range of valid balances.

Space Complexity Analysis:
- The space complexity is O(m * n * k) due to the memoization table.
- Additionally, the recursion stack can go as deep as O(m + n) in the worst case.

Topic: Dynamic Programming (DP), Depth-First Search (DFS)
"""