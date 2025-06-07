"""
LeetCode Question #2684: Maximum Number of Moves in a Grid

Problem Statement:
You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:
- From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1), or (row + 1, col + 1).
- You can only move to a cell if the value in that cell is strictly greater than the value in your current cell.

Return the maximum number of moves you can make.

Examples:
Example 1:
Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
Output: 3
Explanation: We can start at the cell (0, 0) and make the following moves:
- (0, 0) -> (0, 1) (4 > 2)
- (0, 1) -> (1, 2) (9 > 4)  
- (1, 2) -> (2, 3) (11 > 9)
It is impossible to make any more moves.

Example 2:
Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
Output: 0
Explanation: Starting from any cell in the first column, we cannot perform any moves.

Constraints:
- m == grid.length
- n == grid[i].length
- 2 <= m, n <= 1000
- 4 <= grid[i][j] <= 10^6
"""

from typing import List
from functools import lru_cache

def maxMoves(grid: List[List[int]]) -> int:
    """
    Find maximum number of moves using DFS with memoization.
    
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    m, n = len(grid), len(grid[0])
    
    @lru_cache(maxsize=None)
    def dfs(row: int, col: int) -> int:
        if col == n - 1:
            return 0
        
        max_moves = 0
        current_val = grid[row][col]
        
        # Try all three possible moves
        for next_row in [row - 1, row, row + 1]:
            if 0 <= next_row < m and grid[next_row][col + 1] > current_val:
                max_moves = max(max_moves, 1 + dfs(next_row, col + 1))
        
        return max_moves
    
    # Try starting from each cell in the first column
    result = 0
    for i in range(m):
        result = max(result, dfs(i, 0))
    
    return result

def maxMovesDP(grid: List[List[int]]) -> int:
    """
    Dynamic programming approach - bottom-up.
    
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    m, n = len(grid), len(grid[0])
    
    # dp[i][j] = maximum moves starting from cell (i, j)
    dp = [[0] * n for _ in range(m)]
    
    # Fill dp table from right to left
    for col in range(n - 2, -1, -1):
        for row in range(m):
            current_val = grid[row][col]
            
            # Check all three possible moves
            for next_row in [row - 1, row, row + 1]:
                if (0 <= next_row < m and 
                    grid[next_row][col + 1] > current_val):
                    dp[row][col] = max(dp[row][col], 1 + dp[next_row][col + 1])
    
    # Return maximum moves starting from first column
    return max(dp[i][0] for i in range(m))

def maxMovesOptimizedDP(grid: List[List[int]]) -> int:
    """
    Space-optimized DP using only two columns.
    
    Time Complexity: O(m * n)
    Space Complexity: O(m)
    """
    m, n = len(grid), len(grid[0])
    
    # Only need current and next column
    prev_col = [0] * m
    curr_col = [0] * m
    
    # Process from right to left
    for col in range(n - 2, -1, -1):
        for row in range(m):
            curr_col[row] = 0
            current_val = grid[row][col]
            
            # Check all three possible moves
            for next_row in [row - 1, row, row + 1]:
                if (0 <= next_row < m and 
                    grid[next_row][col + 1] > current_val):
                    curr_col[row] = max(curr_col[row], 1 + prev_col[next_row])
        
        # Swap columns
        prev_col, curr_col = curr_col, prev_col
    
    return max(prev_col)

def maxMovesBFS(grid: List[List[int]]) -> int:
    """
    BFS approach to find maximum moves.
    
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    from collections import deque
    
    m, n = len(grid), len(grid[0])
    
    # Start BFS from all cells in first column
    queue = deque()
    visited = set()
    
    for i in range(m):
        queue.append((i, 0, 0))  # (row, col, moves)
        visited.add((i, 0))
    
    max_moves = 0
    
    while queue:
        row, col, moves = queue.popleft()
        max_moves = max(max_moves, moves)
        
        if col == n - 1:
            continue
        
        current_val = grid[row][col]
        
        # Try all three possible moves
        for next_row in [row - 1, row, row + 1]:
            if (0 <= next_row < m and 
                (next_row, col + 1) not in visited and
                grid[next_row][col + 1] > current_val):
                
                queue.append((next_row, col + 1, moves + 1))
                visited.add((next_row, col + 1))
    
    return max_moves

def maxMovesRecursive(grid: List[List[int]]) -> int:
    """
    Pure recursive approach (may cause stack overflow for large grids).
    
    Time Complexity: O(3^(m*n)) without memoization
    Space Complexity: O(m*n) for recursion stack
    """
    m, n = len(grid), len(grid[0])
    
    def dfs(row: int, col: int) -> int:
        if col == n - 1:
            return 0
        
        max_moves = 0
        current_val = grid[row][col]
        
        # Try all three possible moves
        for next_row in [row - 1, row, row + 1]:
            if 0 <= next_row < m and grid[next_row][col + 1] > current_val:
                max_moves = max(max_moves, 1 + dfs(next_row, col + 1))
        
        return max_moves
    
    # Try starting from each cell in the first column
    result = 0
    for i in range(m):
        result = max(result, dfs(i, 0))
    
    return result

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]], 3),
        ([[3,2,4],[2,1,9],[1,1,7]], 0),
        ([[1000000,92910,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068]], 49),
        ([[1,2,3,4],[2,3,4,5],[3,4,5,6]], 3),
        ([[1]], 0),
        ([[1,2],[3,4]], 1)
    ]
    
    print("Testing main DFS approach:")
    for grid, expected in test_cases:
        result = maxMoves(grid)
        print(f"maxMoves(grid) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting DP approach:")
    for grid, expected in test_cases:
        result = maxMovesDP(grid)
        print(f"maxMovesDP(grid) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting optimized DP approach:")
    for grid, expected in test_cases:
        result = maxMovesOptimizedDP(grid)
        print(f"maxMovesOptimizedDP(grid) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting BFS approach:")
    for grid, expected in test_cases:
        result = maxMovesBFS(grid)
        print(f"maxMovesBFS(grid) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    # Test visualization for small grid
    print("\nVisualization for test case 1:")
    grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
    print("Grid:")
    for row in grid:
        print(row)
    
    print("\nPath analysis:")
    print("Starting from (0,0): 2 -> 4 -> 9 -> 11 (3 moves)")
    print("Values: 2 < 4 < 9 < 11 ✓")

"""
Time and Space Complexity Analysis:

DFS with Memoization:
Time Complexity: O(m * n) - Each cell visited once due to memoization
Space Complexity: O(m * n) - Memoization cache + recursion stack

Dynamic Programming:
Time Complexity: O(m * n) - Fill entire DP table
Space Complexity: O(m * n) - DP table storage

Optimized DP:
Time Complexity: O(m * n) - Same computation but space optimized
Space Complexity: O(m) - Only store two columns

BFS Approach:
Time Complexity: O(m * n) - Visit each valid cell once
Space Complexity: O(m * n) - Queue and visited set

Recursive (without memoization):
Time Complexity: O(3^(m*n)) - Exponential without pruning
Space Complexity: O(m*n) - Recursion stack depth

Key Insights:
1. Can start from any cell in the first column
2. Three possible directions: up-right, right, down-right
3. Must move to strictly greater values
4. Memoization/DP eliminates redundant calculations
5. Space optimization possible by processing column by column

Optimization Strategies:
- Use memoization to avoid recalculating subproblems
- Process from right to left in DP to build solutions
- Space optimization by keeping only necessary columns
- Early termination when no valid moves possible

Topic: Dynamic Programming, Graph Traversal, DFS, BFS, Memoization
"""
