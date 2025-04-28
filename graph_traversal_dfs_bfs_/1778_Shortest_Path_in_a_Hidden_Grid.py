"""
LeetCode Problem #1778: Shortest Path in a Hidden Grid

Problem Statement:
You are given a grid with some cells being empty (0) and some cells being blocked (1). 
The grid is hidden, and you can only interact with it through a `GridMaster` API. 
The `GridMaster` API provides the following methods:

1. `canMove(direction: str) -> bool`: Returns `True` if you can move in the given direction 
   ('U', 'D', 'L', 'R') from the current cell, otherwise returns `False`.

2. `move(direction: str) -> None`: Moves the current position in the given direction 
   ('U', 'D', 'L', 'R') if `canMove(direction)` is `True`. Otherwise, it does nothing.

3. `isTarget() -> bool`: Returns `True` if the current cell is the target cell, otherwise `False`.

Your task is to find the shortest path from the starting cell to the target cell. 
If there is no valid path, return -1.

Constraints:
- The grid is finite and has at most 100 cells.
- The starting cell is always empty (0).
- The target cell is always empty (0) and reachable if there is a valid path.
- The grid is surrounded by blocked cells (1).

Write a function `findShortestPath(master: 'GridMaster') -> int` that returns the shortest path 
to the target cell or -1 if no path exists.
"""

from collections import deque

def findShortestPath(master: 'GridMaster') -> int:
    # Directions and their opposites for backtracking
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    opposites = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
    
    # A dictionary to store the grid we discover
    grid = {}
    target = None

    # Step 1: DFS to explore the grid
    def dfs(x, y):
        nonlocal target
        if master.isTarget():
            target = (x, y)
        
        for direction, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if (nx, ny) not in grid and master.canMove(direction):
                master.move(direction)
                grid[(nx, ny)] = 0  # Mark as empty
                dfs(nx, ny)
                master.move(opposites[direction])  # Backtrack
        
        grid[(x, y)] = 0  # Mark as visited

    # Start DFS from the initial position (0, 0)
    grid[(0, 0)] = 0
    dfs(0, 0)

    # If the target was not found during DFS, return -1
    if target is None:
        return -1

    # Step 2: BFS to find the shortest path to the target
    queue = deque([(0, 0, 0)])  # (x, y, distance)
    visited = set()
    visited.add((0, 0))

    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == target:
            return dist
        for dx, dy in directions.values():
            nx, ny = x + dx, y + dy
            if (nx, ny) in grid and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))

    return -1  # If no path is found

# Example Test Cases
class MockGridMaster:
    def __init__(self, grid, start, target):
        self.grid = grid
        self.current = start
        self.target = target

    def canMove(self, direction):
        x, y = self.current
        directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy
        return 0 <= nx < len(self.grid) and 0 <= ny < len(self.grid[0]) and self.grid[nx][ny] == 0

    def move(self, direction):
        if self.canMove(direction):
            x, y = self.current
            directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
            dx, dy = directions[direction]
            self.current = (x + dx, y + dy)

    def isTarget(self):
        return self.current == self.target

# Test Case 1
grid = [
    [0, 1, 0],
    [0, 0, 0],
    [1, 0, 0]
]
master = MockGridMaster(grid, (0, 0), (2, 1))
print(findShortestPath(master))  # Output: 3

# Test Case 2
grid = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
master = MockGridMaster(grid, (0, 0), (2, 2))
print(findShortestPath(master))  # Output: -1

# Time Complexity Analysis:
# - The DFS explores all reachable cells in the grid, which is O(N), where N is the number of cells.
# - The BFS also explores all reachable cells, which is O(N).
# - Overall time complexity: O(N).

# Space Complexity Analysis:
# - The space used by the grid dictionary is O(N).
# - The space used by the DFS recursion stack is O(N) in the worst case.
# - The space used by the BFS queue is O(N).
# - Overall space complexity: O(N).

# Topic: Graph Traversal (DFS, BFS)