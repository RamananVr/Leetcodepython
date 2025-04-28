"""
LeetCode Problem #1730: Shortest Path to Get Food

Problem Statement:
You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell in a grid. 
You are given an m x n character matrix, grid, of these different types of cells:

- '*' is your location. There is exactly one '*' cell.
- '#' is a food cell. There may be multiple food cells.
- 'O' is a free space, and you can move through these cells.
- 'X' is an obstacle, and you cannot move through these cells.

You can move left, right, up, or down to any adjacent cell. Return the length of the shortest path for you to reach any food cell. 
If there is no path for you to reach food, return -1.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- grid[row][col] is '*', 'X', 'O', or '#'.
- The grid contains exactly one '*' cell.

"""

from collections import deque

def getFood(grid):
    """
    Finds the shortest path to any food cell in the grid.

    :param grid: List[List[str]] - The grid representing the map.
    :return: int - The shortest path length to a food cell, or -1 if unreachable.
    """
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    # Find the starting position ('*')
    start = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '*':
                start = (r, c)
                break
        if start:
            break

    # BFS to find the shortest path to any food cell
    queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
    visited = set()
    visited.add(start)

    while queue:
        r, c, dist = queue.popleft()

        # Check if we reached a food cell
        if grid[r][c] == '#':
            return dist

        # Explore neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] != 'X':
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    # If no path to food is found
    return -1

# Example Test Cases
if __name__ == "__main__":
    grid1 = [
        ["X", "X", "X", "X", "X", "X"],
        ["X", "*", "O", "O", "O", "X"],
        ["X", "O", "O", "#", "O", "X"],
        ["X", "X", "X", "X", "X", "X"]
    ]
    print(getFood(grid1))  # Output: 3

    grid2 = [
        ["X", "X", "X", "X", "X"],
        ["X", "*", "X", "O", "X"],
        ["X", "O", "X", "#", "X"],
        ["X", "X", "X", "X", "X"]
    ]
    print(getFood(grid2))  # Output: -1

    grid3 = [
        ["X", "*", "O", "O", "O"],
        ["X", "O", "O", "#", "O"],
        ["X", "O", "O", "O", "O"],
        ["X", "X", "X", "X", "X"]
    ]
    print(getFood(grid3))  # Output: 3

# Time Complexity Analysis:
# - The BFS explores each cell at most once, so the time complexity is O(m * n), where m is the number of rows and n is the number of columns.

# Space Complexity Analysis:
# - The space complexity is O(m * n) due to the visited set and the queue, which can store up to m * n elements in the worst case.

# Topic: Breadth-First Search (BFS), Graph Traversal