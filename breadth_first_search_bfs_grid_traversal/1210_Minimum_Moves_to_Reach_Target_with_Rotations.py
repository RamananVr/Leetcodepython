"""
LeetCode Problem #1210: Minimum Moves to Reach Target with Rotations

Problem Statement:
In an n x n grid, there is a snake that spans two cells and starts moving from the top-left corner at (0, 0) and (0, 1). 
The grid has empty cells represented by 0 and blocked cells represented by 1. The snake can move in four possible ways:

1. Move one cell to the right if there are no blocked cells in the way.
2. Move one cell down if there are no blocked cells in the way.
3. Rotate clockwise if the snake is horizontal and the two cells under it are empty.
4. Rotate counterclockwise if the snake is vertical and the two cells to its right are empty.

Your task is to return the minimum number of moves to reach the target position (n-1, n-2) with the snake in a horizontal position. 
If there is no way to reach the target, return -1.

Constraints:
- 2 <= n <= 100
- 0 <= grid[i][j] <= 1
- The snake starts at (0, 0) and (0, 1) with a horizontal orientation.
- The grid is guaranteed to be square.

"""

from collections import deque

def minimumMoves(grid):
    n = len(grid)
    # Directions: (dx, dy, new_orientation)
    # 0 = horizontal, 1 = vertical
    directions = [
        (0, 1, 0),  # Move right
        (1, 0, 1),  # Move down
        (0, 0, 1),  # Rotate clockwise (horizontal to vertical)
        (0, 0, 0)   # Rotate counterclockwise (vertical to horizontal)
    ]
    
    # BFS queue: (x, y, orientation, moves)
    queue = deque([(0, 0, 0, 0)])
    visited = set([(0, 0, 0)])
    
    while queue:
        x, y, orientation, moves = queue.popleft()
        
        # Check if we've reached the target
        if (x, y, orientation) == (n-1, n-2, 0):
            return moves
        
        for dx, dy, new_orientation in directions:
            nx, ny = x + dx, y + dy
            
            if new_orientation == 0:  # Horizontal
                if nx < n and ny + 1 < n and grid[nx][ny] == 0 and grid[nx][ny + 1] == 0:
                    if (nx, ny, 0) not in visited:
                        visited.add((nx, ny, 0))
                        queue.append((nx, ny, 0, moves + 1))
            elif new_orientation == 1:  # Vertical
                if nx + 1 < n and ny < n and grid[nx][ny] == 0 and grid[nx + 1][ny] == 0:
                    if (nx, ny, 1) not in visited:
                        visited.add((nx, ny, 1))
                        queue.append((nx, ny, 1, moves + 1))
            elif orientation == 0 and new_orientation == 1:  # Rotate clockwise
                if x + 1 < n and grid[x + 1][y] == 0 and grid[x + 1][y + 1] == 0:
                    if (x, y, 1) not in visited:
                        visited.add((x, y, 1))
                        queue.append((x, y, 1, moves + 1))
            elif orientation == 1 and new_orientation == 0:  # Rotate counterclockwise
                if y + 1 < n and grid[x][y + 1] == 0 and grid[x + 1][y + 1] == 0:
                    if (x, y, 0) not in visited:
                        visited.add((x, y, 0))
                        queue.append((x, y, 0, moves + 1))
    
    return -1

# Example Test Cases
if __name__ == "__main__":
    grid1 = [
        [0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0]
    ]
    print(minimumMoves(grid1))  # Output: 11

    grid2 = [
        [0, 0, 1, 1],
        [0, 0, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 0, 0]
    ]
    print(minimumMoves(grid2))  # Output: -1

# Time Complexity Analysis:
# The BFS explores each state (x, y, orientation) at most once. There are O(n^2) possible positions for the snake,
# and 2 possible orientations (horizontal or vertical). Thus, the time complexity is O(n^2).
# Each state has a constant number of transitions (4 directions), so the overall complexity is O(n^2).

# Space Complexity Analysis:
# The space complexity is O(n^2) for the visited set and the BFS queue.

# Topic: Breadth-First Search (BFS), Grid Traversal