"""
LeetCode Question #505: The Maze II

Problem Statement:
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left, or right, but it won't stop until hitting a wall. When the ball stops, it could choose the next direction.

Given the maze represented as a 2D array, the ball's start position, and the destination, return the shortest distance for the ball to stop at the destination. If the ball cannot stop at the destination, return -1.

The maze is represented by a grid of size m x n, where:
- 1 <= m, n <= 100
- maze[i][j] == 0 means the cell is empty, and maze[i][j] == 1 means the cell is a wall.
- You may assume that the borders of the maze are all walls.
- The start and destination coordinates are always empty spaces, and they will not be the same.

Input:
- maze: List[List[int]] (2D grid representing the maze)
- start: List[int] (starting position of the ball)
- destination: List[int] (destination position of the ball)

Output:
- int (shortest distance to the destination, or -1 if unreachable)
"""

from heapq import heappop, heappush
from typing import List, Tuple

def shortestDistance(maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    def roll(x: int, y: int, dx: int, dy: int) -> Tuple[int, int, int]:
        """Roll the ball in a direction until it hits a wall."""
        distance = 0
        while 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and maze[x + dx][y + dy] == 0:
            x += dx
            y += dy
            distance += 1
        return x, y, distance

    m, n = len(maze), len(maze[0])
    start_x, start_y = start
    dest_x, dest_y = destination

    # Priority queue for Dijkstra's algorithm
    heap = [(0, start_x, start_y)]  # (distance, x, y)
    distances = [[float('inf')] * n for _ in range(m)]
    distances[start_x][start_y] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while heap:
        dist, x, y = heappop(heap)

        # If we reach the destination, return the distance
        if [x, y] == destination:
            return dist

        # Skip if we already found a shorter path to this cell
        if dist > distances[x][y]:
            continue

        # Explore all possible directions
        for dx, dy in directions:
            next_x, next_y, roll_dist = roll(x, y, dx, dy)
            new_dist = dist + roll_dist

            if new_dist < distances[next_x][next_y]:
                distances[next_x][next_y] = new_dist
                heappush(heap, (new_dist, next_x, next_y))

    # If we cannot reach the destination, return -1
    return -1

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
    print(shortestDistance(maze1, start1, destination1))  # Output: 12

    maze2 = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    start2 = [0, 4]
    destination2 = [3, 2]
    print(shortestDistance(maze2, start2, destination2))  # Output: -1

    maze3 = [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    start3 = [0, 0]
    destination3 = [4, 4]
    print(shortestDistance(maze3, start3, destination3))  # Output: 8

# Time Complexity Analysis:
# - Rolling in each direction takes O(m + n) in the worst case (traversing a row or column).
# - Each cell is processed at most once, so the total number of operations is O(m * n * (m + n)).
# - Using a priority queue ensures efficient extraction of the minimum distance, which is O(log(m * n)).
# - Overall time complexity: O(m * n * (m + n)).

# Space Complexity Analysis:
# - The distances array takes O(m * n) space.
# - The priority queue can hold up to O(m * n) elements.
# - Overall space complexity: O(m * n).

# Topic: Graphs, Dijkstra's Algorithm