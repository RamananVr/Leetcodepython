"""
LeetCode Question #2658: Maximum Number of Fish in a Grid

Problem Statement:
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
- A land cell if grid[r][c] > 0, and it contains grid[r][c] fish.
- A water cell if grid[r][c] == 0.

A fisher can start at any water cell (r, c) and can do the following operations any number of times:
- Catch all the fish at cell (r, c).
- Move to an adjacent water cell.

Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

Two cells are adjacent if they share a side.

Examples:
Example 1:
Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,1) and collect 3 fish, then move to (1,2) and collect 4 fish.

Example 2:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[1,0,0,1]]
Output: 0
Explanation: There are no water cells, so the fisher cannot catch any fish.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- 0 <= grid[r][c] <= 10
"""

from typing import List

def findMaxFish(grid: List[List[int]]) -> int:
    """
    Find maximum fish using DFS from each water cell.
    
    Strategy: Try starting from each water cell and use DFS to explore
    all reachable water cells, collecting fish along the way.
    """
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    max_fish = 0
    
    def dfs(r, c, visited):
        """DFS to collect fish from connected water cells."""
        if (r < 0 or r >= m or c < 0 or c >= n or 
            grid[r][c] == 0 or (r, c) in visited):
            return 0
        
        visited.add((r, c))
        fish_count = grid[r][c]
        
        # Explore all adjacent cells
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            fish_count += dfs(nr, nc, visited)
        
        return fish_count
    
    # Try starting from each water cell
    for i in range(m):
        for j in range(n):
            if grid[i][j] > 0:  # Water cell with fish
                visited = set()
                fish_collected = dfs(i, j, visited)
                max_fish = max(max_fish, fish_collected)
    
    return max_fish

def findMaxFishOptimized(grid: List[List[int]]) -> int:
    """
    Optimized approach using connected components.
    
    Since we want to find the maximum fish in any connected component,
    we can use DFS/BFS to find all connected components and return the maximum.
    """
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    max_fish = 0
    
    def dfs(r, c):
        """DFS to collect all fish in current connected component."""
        if (r < 0 or r >= m or c < 0 or c >= n or 
            grid[r][c] == 0 or (r, c) in visited):
            return 0
        
        visited.add((r, c))
        fish_count = grid[r][c]
        
        # Explore all adjacent water cells
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            fish_count += dfs(nr, nc)
        
        return fish_count
    
    # Find all connected components
    for i in range(m):
        for j in range(n):
            if grid[i][j] > 0 and (i, j) not in visited:
                component_fish = dfs(i, j)
                max_fish = max(max_fish, component_fish)
    
    return max_fish

def findMaxFishBFS(grid: List[List[int]]) -> int:
    """
    BFS approach for finding connected components.
    """
    if not grid or not grid[0]:
        return 0
    
    from collections import deque
    
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    max_fish = 0
    
    def bfs(start_r, start_c):
        """BFS to collect all fish in current connected component."""
        queue = deque([(start_r, start_c)])
        visited.add((start_r, start_c))
        total_fish = 0
        
        while queue:
            r, c = queue.popleft()
            total_fish += grid[r][c]
            
            # Explore adjacent cells
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and 
                    grid[nr][nc] > 0 and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        
        return total_fish
    
    # Find all connected components
    for i in range(m):
        for j in range(n):
            if grid[i][j] > 0 and (i, j) not in visited:
                component_fish = bfs(i, j)
                max_fish = max(max_fish, component_fish)
    
    return max_fish

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]], 7),
        ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1]], 0),
        ([[10]], 10),
        ([[1, 2, 3], [0, 0, 0], [4, 5, 6]], 21),  # Two separate components: 6 and 15
        ([[1, 2], [3, 4]], 10),  # One connected component
        ([[0, 0], [0, 0]], 0)  # No fish
    ]
    
    print("Testing DFS approach:")
    for grid, expected in test_cases:
        result = findMaxFish([row[:] for row in grid])  # Deep copy
        print(f"findMaxFish({grid}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting optimized DFS approach:")
    for grid, expected in test_cases:
        result = findMaxFishOptimized([row[:] for row in grid])  # Deep copy
        print(f"findMaxFishOptimized({grid}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting BFS approach:")
    for grid, expected in test_cases:
        result = findMaxFishBFS([row[:] for row in grid])  # Deep copy
        print(f"findMaxFishBFS({grid}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")

"""
Time and Space Complexity Analysis:

DFS Approach:
Time Complexity: O(m * n * m * n) = O((mn)^2) in worst case
- For each cell, we might do DFS that visits all cells
- In practice, much better due to visited tracking
Space Complexity: O(m * n) - recursion stack and visited set

Optimized DFS Approach:
Time Complexity: O(m * n) - each cell visited at most once
Space Complexity: O(m * n) - recursion stack and visited set

BFS Approach:
Time Complexity: O(m * n) - each cell visited at most once
Space Complexity: O(m * n) - queue and visited set

Key Insights:
1. This is a connected components problem
2. We need to find the component with maximum sum
3. Water cells (grid[r][c] = 0) act as barriers
4. Fish can only move between adjacent water cells (grid[r][c] > 0)

Topic: Matrix, DFS, BFS, Connected Components, Graph Traversal
"""
