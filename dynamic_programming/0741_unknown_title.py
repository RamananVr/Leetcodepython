"""
LeetCode Problem #741: Cherry Pickup

Problem Statement:
You are given an n x n grid representing a field of cherries, each cell is one of three possible integers:
- 0 means the cell is empty, so you can pass through,
- 1 means the cell contains a cherry that you can pick up, and
- -1 means the cell contains a thorn that blocks your way.

You have to start at the top-left corner (0, 0) and reach the bottom-right corner (n-1, n-1) to collect cherries. 
Once you reach the bottom-right corner, you have to return to the top-left corner, picking up cherries on the way back.

You can only move either down or right on the way to the bottom-right corner, and only move up or left on the way back. 
Thorns (-1) block your path, and if you encounter a thorn, you cannot continue the path.

Write a function `cherryPickup(grid)` that returns the maximum number of cherries you can collect by following the rules above. 
If it is impossible to reach the bottom-right corner and return to the top-left corner, return 0.

Constraints:
- n == grid.length == grid[i].length
- 1 <= n <= 50
- grid[i][j] is -1, 0, or 1
"""

def cherryPickup(grid):
    """
    Dynamic Programming solution for the Cherry Pickup problem.
    """
    n = len(grid)
    # Memoization table: dp[x1][y1][x2] represents the maximum cherries collected
    # when person 1 is at (x1, y1) and person 2 is at (x2, y2), where y2 = x1 + y1 - x2.
    dp = [[[-1] * n for _ in range(n)] for _ in range(n)]
    
    def dfs(x1, y1, x2):
        y2 = x1 + y1 - x2  # Derive y2 based on the constraint x1 + y1 == x2 + y2
        if x1 >= n or y1 >= n or x2 >= n or y2 >= n or grid[x1][y1] == -1 or grid[x2][y2] == -1:
            return float('-inf')  # Invalid state
        if x1 == n - 1 and y1 == n - 1:  # Reached the bottom-right corner
            return grid[x1][y1]
        if dp[x1][y1][x2] != -1:  # Return cached result
            return dp[x1][y1][x2]
        
        # Collect cherries at (x1, y1) and (x2, y2)
        result = grid[x1][y1]
        if x1 != x2:  # Avoid double-counting if both are at the same cell
            result += grid[x2][y2]
        
        # Explore all possible moves
        result += max(
            dfs(x1 + 1, y1, x2 + 1),  # Both move down
            dfs(x1 + 1, y1, x2),      # Person 1 moves down, Person 2 moves right
            dfs(x1, y1 + 1, x2 + 1),  # Person 1 moves right, Person 2 moves down
            dfs(x1, y1 + 1, x2)       # Both move right
        )
        
        dp[x1][y1][x2] = result  # Cache the result
        return result
    
    # Start the DFS from the top-left corner
    result = dfs(0, 0, 0)
    return max(0, result)  # If result is negative, return 0 (impossible case)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    grid1 = [
        [0, 1, -1],
        [1, 0, -1],
        [1, 1,  1]
    ]
    print(cherryPickup(grid1))  # Output: 5

    # Test Case 2
    grid2 = [
        [1, 1, -1],
        [1, -1, 1],
        [-1, 1, 1]
    ]
    print(cherryPickup(grid2))  # Output: 0

    # Test Case 3
    grid3 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    print(cherryPickup(grid3))  # Output: 12

"""
Time Complexity:
- The state space of the DP is O(n^3), where n is the size of the grid.
- Each state takes O(1) time to compute, so the overall time complexity is O(n^3).

Space Complexity:
- The space complexity is O(n^3) for the DP table.

Topic: Dynamic Programming
"""