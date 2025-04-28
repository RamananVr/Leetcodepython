"""
LeetCode Problem #1263: Minimum Moves to Move a Box to Their Target Location

Problem Statement:
A storekeeper is a person who is responsible for moving boxes in a warehouse to their target locations. The warehouse is represented as a grid of size m x n, where each cell is either empty (represented as '.') or an obstacle (represented as '#'). The storekeeper and the box are also located in the grid.

You are given a grid of size m x n, where:
- 'S' is the starting position of the storekeeper.
- 'B' is the starting position of the box.
- 'T' is the target position of the box.

The storekeeper can move up, down, left, or right to adjacent empty cells. The box can be moved to an adjacent empty cell only if the storekeeper is adjacent to the box and pushes it in the direction of movement. The storekeeper cannot walk through obstacles or push the box into obstacles.

Return the minimum number of pushes required to move the box to the target position. If it is impossible to move the box to the target position, return -1.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 20
- grid[i][j] is either '.', '#', 'S', 'B', or 'T'.
- There is exactly one 'S', 'B', and 'T' in the grid.

"""

from collections import deque

def minPushBox(grid):
    def is_valid(x, y):
        """Check if a position is within bounds and not an obstacle."""
        return 0 <= x < m and 0 <= y < n and grid[x][y] != '#'

    def can_reach(sx, sy, tx, ty, box_x, box_y):
        """Check if the storekeeper can reach (tx, ty) without crossing the box."""
        visited = set()
        queue = deque([(sx, sy)])
        while queue:
            x, y = queue.popleft()
            if (x, y) == (tx, ty):
                return True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny) and (nx, ny) not in visited and (nx, ny) != (box_x, box_y):
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        return False

    m, n = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    storekeeper, box, target = None, None, None

    # Locate the positions of the storekeeper, box, and target
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                storekeeper = (i, j)
            elif grid[i][j] == 'B':
                box = (i, j)
            elif grid[i][j] == 'T':
                target = (i, j)

    # BFS to find the minimum pushes
    queue = deque([(box[0], box[1], storekeeper[0], storekeeper[1], 0)])  # (box_x, box_y, storekeeper_x, storekeeper_y, pushes)
    visited = set([(box[0], box[1], storekeeper[0], storekeeper[1])])

    while queue:
        box_x, box_y, sk_x, sk_y, pushes = queue.popleft()
        if (box_x, box_y) == target:
            return pushes
        for dx, dy in directions:
            new_box_x, new_box_y = box_x + dx, box_y + dy
            new_sk_x, new_sk_y = box_x - dx, box_y - dy
            if is_valid(new_box_x, new_box_y) and is_valid(new_sk_x, new_sk_y) and (new_box_x, new_box_y, box_x, box_y) not in visited:
                if can_reach(sk_x, sk_y, new_sk_x, new_sk_y, box_x, box_y):
                    visited.add((new_box_x, new_box_y, box_x, box_y))
                    queue.append((new_box_x, new_box_y, box_x, box_y, pushes + 1))
    return -1

# Example Test Cases
if __name__ == "__main__":
    grid1 = [
        ["#", "#", "#", "#", "#", "#"],
        ["#", "T", "#", "#", "#", "#"],
        ["#", ".", ".", "B", ".", "#"],
        ["#", ".", "#", "#", ".", "#"],
        ["#", ".", ".", ".", "S", "#"],
        ["#", "#", "#", "#", "#", "#"]
    ]
    print(minPushBox(grid1))  # Output: 3

    grid2 = [
        ["#", "#", "#", "#", "#", "#"],
        ["#", "T", "#", "#", "#", "#"],
        ["#", ".", ".", "B", ".", "#"],
        ["#", "#", "#", "#", ".", "#"],
        ["#", ".", ".", ".", "S", "#"],
        ["#", "#", "#", "#", "#", "#"]
    ]
    print(minPushBox(grid2))  # Output: -1

    grid3 = [
        ["#", "#", "#", "#", "#", "#"],
        ["#", "T", ".", ".", "#", "#"],
        ["#", ".", "#", "B", ".", "#"],
        ["#", ".", ".", ".", ".", "#"],
        ["#", ".", ".", ".", "S", "#"],
        ["#", "#", "#", "#", "#", "#"]
    ]
    print(minPushBox(grid3))  # Output: 5

# Time and Space Complexity Analysis
# Time Complexity: O(m * n * m * n), where m and n are the dimensions of the grid. This accounts for the BFS traversal and the reachability check for the storekeeper.
# Space Complexity: O(m * n * m * n), for the visited set and the BFS queue.

# Topic: Graph, Breadth-First Search (BFS)