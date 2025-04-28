"""
LeetCode Problem #2850: Minimum Moves to Spread Stones Over Grid

Problem Statement:
You are given a 2D grid of size `m x n` where each cell contains either a positive integer representing the number of stones in that cell, or `0` indicating that the cell is empty. In one move, you can transfer one stone from a cell containing at least one stone to an adjacent cell (up, down, left, or right).

Return the minimum number of moves required to spread all stones such that every cell in the grid has exactly one stone.

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 5`
- `0 <= grid[i][j] <= 5`
- The sum of all stones in the grid is equal to `m * n`.

"""

# Solution
from itertools import permutations

def minimumMoves(grid):
    def dfs(index, moves):
        if index == len(excess):
            return moves
        
        x, y = excess[index]
        min_moves = float('inf')
        
        for i, (tx, ty) in enumerate(deficit):
            if visited[i]:
                continue
            
            visited[i] = True
            min_moves = min(min_moves, dfs(index + 1, moves + abs(x - tx) + abs(y - ty)))
            visited[i] = False
        
        return min_moves
    
    excess = []
    deficit = []
    
    # Identify excess and deficit cells
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 1:
                excess.extend([(i,j)
    
    
    
    
    