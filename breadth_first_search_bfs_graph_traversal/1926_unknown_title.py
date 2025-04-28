"""
LeetCode Problem #1926: Nearest Exit from Entrance in Maze

Problem Statement:
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). 
You are also given the entrance of the maze, where entrance = [entrance_row, entrance_col] denotes the row and column 
of the cell you are initially standing at.

In one step, you can move up, down, left, or right through an empty cell, but you cannot step into a wall or move 
outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that 
is at the border of the maze. The entrance cell is not an exit.

Return the number of steps in the shortest path to the nearest exit, or -1 if no such path exists.

Constraints:
- maze.length == m
- maze[i].length == n
- 1 <= m, n <= 100
- maze[i][j] is either '.' or '+'
- entrance.length == 2
- 0 <= entrance_row < m
- 0 <= entrance_col < n
- The entrance will always be an empty cell.

"""

from collections import deque

def nearestExit(maze, entrance):
    """
    Finds the shortest path to the nearest exit from the entrance in the maze.

    :param maze: List[List[str]] - The maze represented as a 2D grid.
    :param entrance: List[int] - The entrance coordinates [row, col].
    :return: int - The number of steps to the nearest exit, or -1 if no exit exists.
    """
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)
    visited = set()
    visited.add((entrance[0], entrance[1]))

    while queue:
        row, col, steps = queue.popleft()

        # Check if the current cell is an exit (on the border and not the entrance)
        if (row == 0 or row == rows - 1 or col == 0 or col == cols - 1) and (row, col) != (entrance[0], entrance[1]):
            return steps

        # Explore neighbors
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == '.' and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, steps + 1))

    return -1  # No exit found


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    maze1 = [["+", "+", ".", "+"],
             [".", ".", ".", "+"],
             ["+", "+", "+", "."]]
    entrance1 = [1, 2]
    print(nearestExit(maze1, entrance1))  # Expected Output: 1

    # Test Case 2
    maze2 = [["+", "+", "+"],
             [".", ".", "."],
             ["+", "+", "+"]]
    entrance2 = [1, 0]
    print(nearestExit(maze2, entrance2))  # Expected Output: 2

    # Test Case 3
    maze3 = [[".", "+"]]
    entrance3 = [0, 0]
    print(nearestExit(maze3, entrance3))  # Expected Output: -1

    # Test Case 4
    maze4 = [["+", ".", "+", "+", "+", "+", "+"],
             ["+", ".", "+", ".", ".", ".", "+"],
             ["+", ".", "+", ".", "+", ".", "+"],
             ["+", ".", ".", ".", "+", ".", "+"],
             ["+", "+", "+", "+", "+", ".", "+"]]
    entrance4 = [1, 1]
    print(nearestExit(maze4, entrance4))  # Expected Output: 12


# Time and Space Complexity Analysis
"""
Time Complexity:
- Each cell in the maze is visited at most once, and there are m * n cells in the maze.
- Therefore, the time complexity is O(m * n).

Space Complexity:
- The space complexity is determined by the queue and the visited set.
- In the worst case, the queue and visited set can contain all m * n cells.
- Therefore, the space complexity is O(m * n).
"""

# Topic: Breadth-First Search (BFS), Graph Traversal