"""
LeetCode Problem #1211: Minimum Moves to Reach Target with Rotations

Problem Statement:
In an n x n grid, there is a snake that spans two cells and initially lies horizontally at the top-left corner of the grid. The head of the snake is at (0, 1), and the tail is at (0, 0).

The grid has empty cells represented by 0 and blocked cells represented by 1. The snake can move in the following ways:
1. Move Forward: Move the head and the tail one cell forward in the current direction.
2. Rotate Clockwise: Rotate the snake clockwise if it's in a horizontal position, turning it into a vertical position.
3. Rotate Counterclockwise: Rotate the snake counterclockwise if it's in a vertical position, turning it into a horizontal position.

Return the minimum number of moves to reach the target position (n-1, n-1) with the snake in a horizontal position. If there is no way to reach the target, return -1.

Constraints:
- 2 <= n <= 100
- 0 <= grid[i][j] <= 1
- The snake's initial position and the target position are always empty.

Example:
Input: grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]
Output: 11
"""

from collections import deque

def minimumMoves(grid):
    n = len(grid)
    visited = set()
    queue = deque([(0, 0, 0, 1, 0)])  # (tail_x, tail_y, head_x, head_y, moves)

    while queue:
        tail_x, tail_y, head_x, head_y, moves = queue.popleft()

        # If the snake reaches the target in horizontal position
        if (tail_x, tail_y, head_x, head_y) == (n-1, n-2, n-1, n-1):
            return moves

        # Skip if already visited
        if (tail_x, tail_y, head_x, head_y) in visited:
            continue
        visited.add((tail_x, tail_y, head_x, head_y))

        # Move forward
        if head_x == tail_x:  # Horizontal
            if head_y + 1 < n and grid[head_x][head_y + 1] == 0:
                queue.append((tail_x, tail_y + 1, head_x, head_y + 1, moves + 1))
        else:  # Vertical
            if head_x + 1 < n and grid[head_x + 1][head_y] == 0:
                queue.append((tail_x + 1, tail_y, head_x + 1, head_y, moves + 1))

        # Rotate clockwise (horizontal -> vertical)
        if head_x == tail_x and head_x + 1 < n and grid[head_x + 1][head_y] == 0 and grid[tail_x + 1][tail_y] == 0:
            queue.append((tail_x, tail_y, tail_x + 1, tail_y, moves + 1))

        # Rotate counterclockwise (vertical -> horizontal)
        if head_y == tail_y and head_y + 1 < n and grid[head_x][head_y + 1] == 0 and grid[tail_x][tail_y + 1] == 0:
            queue.append((tail_x, tail_y, tail_x, tail_y + 1, moves + 1))

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
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    print(minimumMoves(grid2))  # Output: -1

# Time Complexity Analysis:
# The maximum number of states is O(n^2 * 2), where n is the grid size (n^2 for all possible positions of the snake,
# and 2 for the two possible orientations: horizontal and vertical). Each state is processed once, and each state
# has a constant number of transitions (at most 4). Thus, the time complexity is O(n^2).

# Space Complexity Analysis:
# The space complexity is O(n^2) for the visited set and the queue.

# Topic: Breadth-First Search (BFS), Grid Traversal