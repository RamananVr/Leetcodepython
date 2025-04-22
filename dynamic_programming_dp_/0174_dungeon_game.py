"""
LeetCode Question #174: Dungeon Game

Problem Statement:
The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. 
The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned 
in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health 
drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), and others contain magic 
orbs that increase the knight's health (represented by positive integers). Other rooms are empty (represented by 0).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward 
in each step.

Write a function to determine the knight's minimum initial health so that he can rescue the princess.

The knight's health must be at least 1 at all times, regardless of the values in the dungeon.

Constraints:
- m == dungeon.length
- n == dungeon[i].length
- 1 <= m, n <= 200
- -1000 <= dungeon[i][j] <= 1000
"""

# Solution
def calculateMinimumHP(dungeon):
    """
    Calculate the minimum initial health required for the knight to rescue the princess.

    :param dungeon: List[List[int]] - 2D grid representing the dungeon
    :return: int - Minimum initial health required
    """
    m, n = len(dungeon), len(dungeon[0])
    # dp[i][j] represents the minimum health required to reach the princess from cell (i, j)
    dp = [[float('inf')] * n for _ in range(m)]
    
    # Base case: Bottom-right cell (where the princess is located)
    dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
    
    # Fill the dp table from bottom-right to top-left
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i < m-1:
                dp[i][j] = min(dp[i][j], max(1, dp[i+1][j] - dungeon[i][j]))
            if j < n-1:
                dp[i][j] = min(dp[i][j], max(1, dp[i][j+1] - dungeon[i][j]))
    
    return dp[0][0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    dungeon1 = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    print(calculateMinimumHP(dungeon1))  # Expected Output: 7

    # Test Case 2
    dungeon2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(calculateMinimumHP(dungeon2))  # Expected Output: 1

    # Test Case 3
    dungeon3 = [[1, -3, 3], [0, -2, 0], [-3, -3, -3]]
    print(calculateMinimumHP(dungeon3))  # Expected Output: 3

    # Test Case 4
    dungeon4 = [[-1]]
    print(calculateMinimumHP(dungeon4))  # Expected Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
The solution involves filling up an m x n DP table, where m is the number of rows and n is the number of columns.
Each cell is computed in constant time, so the overall time complexity is O(m * n).

Space Complexity:
The space complexity is O(m * n) due to the DP table. However, this can be optimized to O(n) if we use a single 
row/column for computation instead of the entire table.
"""

# Topic: Dynamic Programming (DP)