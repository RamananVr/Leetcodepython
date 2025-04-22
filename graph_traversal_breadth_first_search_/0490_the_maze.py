"""
LeetCode Question #490: The Maze

Problem Statement:
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left, or right, but it won't stop rolling until it hits a wall. When the ball stops, it could choose the next direction.

Given the maze represented by a 2D array, the ball's start position, and the destination, determine whether the ball can stop at the destination.

The maze is represented by a binary 2D array. 1 means the cell is a wall, and 0 means the cell is an empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented as row and column indices.

Example:
Input:
maze = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]

Output: True

Constraints:
- m == maze.length
- n == maze[i].length
- 1 <= m, n <= 100
- maze[i][j] is 0 or 1
- start.length == 2
- destination.length == 2
- 0 <= start[0], destination[0] < m
- 0 <= start[1], destination[1] < n
- Both the start and destination positions are empty spaces.

"""

from collections import deque

def hasPath(maze, start, destination):
    """
    Determines if the ball can stop at the destination in the maze.

    :param maze: List[List[int]] - 2D binary array representing the maze
    :param start: List[int] - Starting position [row, col]
    :param destination: List[int] - Destination position [row, col]
    :return: bool - True if the ball can stop at the destination, False otherwise
    """
    def roll(row, col, direction):
        """Roll the ball in the given direction until it hits a wall."""
        dr, dc = direction
        while 0 <= row + dr < len(maze) and 0 <= col + dc < len(maze[0]) and maze[row + dr][col + dc] == 0:
            row += dr
            col += dc
        return row, col

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    visited = set()
    queue = deque([tuple(start)])

    while queue:
        current = queue.popleft()
        if current == tuple(destination):
            return True
        if current in visited:
            continue
        visited.add(current)

        for direction in directions:
            next_position = roll(current[0], current[1], direction)
            if next_position not in visited:
                queue.append(next_position)

    return False


# Example Test Cases
if __name__ == "__main__":
    maze1 = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    start1 = [0, 4]
    destination1 = [4, 4]
    print(hasPath(maze1, start1, destination1))  # Output: True

    maze2 = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    start2 = [0, 4]
    destination2 = [3, 2]
    print(hasPath(maze2, start2, destination2))  # Output: False

    maze3 = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start3 = [4, 0]
    destination3 = [0, 4]
    print(hasPath(maze3, start3, destination3))  # Output: True


# Time and Space Complexity Analysis
# Time Complexity: O(m * n)
# - Each cell in the maze is visited at most once. Rolling in each direction takes O(m + n) in the worst case.
# - Therefore, the total complexity is O(m * n).

# Space Complexity: O(m * n)
# - The visited set stores at most m * n cells.
# - The queue can also grow up to m * n in the worst case.

# Topic: Graph Traversal (Breadth-First Search)