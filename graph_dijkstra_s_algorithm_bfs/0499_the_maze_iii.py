"""
LeetCode Question #499: The Maze III

Problem Statement:
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left, or right, but it won't stop until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination, and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot reach the destination, return "impossible".

The maze is represented as a 2D array. Each cell is either a wall (1) or an empty space (0). You may assume that the borders of the maze are all walls. The start and destination coordinates are represented as row and column indices.

You need to return the shortest path in lexicographical order if there are multiple shortest paths.

Example:
Input:
maze = [[0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]

Output: "ldrd"

Constraints:
1. The maze is a 2D array with dimensions m x n where 1 <= m, n <= 100.
2. The maze[i][j] is either 0 (empty space) or 1 (wall).
3. The start and destination coordinates are within the maze and are empty spaces.
4. The ball can only travel in the four cardinal directions (up, down, left, right).
5. The ball stops rolling when it hits a wall or the boundary of the maze.
"""

from heapq import heappop, heappush
from collections import defaultdict

def findShortestWay(maze, start, destination):
    def roll(x, y, dx, dy):
        distance = 0
        while 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and maze[x + dx][y + dy] == 0:
            x += dx
            y += dy
            distance += 1
        return x, y, distance

    directions = [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]
    heap = [(0, "", start[0], start[1])]
    visited = defaultdict(lambda: float('inf'))

    while heap:
        dist, path, x, y = heappop(heap)
        if [x, y] == destination:
            return path
        if dist > visited[(x, y)]:
            continue
        visited[(x, y)] = dist
        for dx, dy, d in directions:
            nx, ny, d_dist = roll(x, y, dx, dy)
            if dist + d_dist < visited[(nx, ny)]:
                heappush(heap, (dist + d_dist, path + d, nx, ny))

    return "impossible"

# Example Test Cases
if __name__ == "__main__":
    maze1 = [[0, 0, 0, 0, 0],
             [1, 1, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0]]
    start1 = [0, 4]
    destination1 = [4, 4]
    print(findShortestWay(maze1, start1, destination1))  # Output: "ldrd"

    maze2 = [[0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0],
             [1, 1, 0, 1, 1],
             [0, 0, 0, 0, 0]]
    start2 = [0, 4]
    destination2 = [4, 4]
    print(findShortestWay(maze2, start2, destination2))  # Output: "dldr"

    maze3 = [[0, 0, 0, 0, 0],
             [1, 1, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0]]
    start3 = [0, 4]
    destination3 = [3, 2]
    print(findShortestWay(maze3, start3, destination3))  # Output: "impossible"

# Time Complexity:
# The algorithm explores all reachable cells in the maze. For each cell, it considers four directions.
# Rolling in a direction takes O(m + n) in the worst case (where m and n are the dimensions of the maze).
# Thus, the time complexity is O(m * n * (m + n)).

# Space Complexity:
# The space complexity is O(m * n) for the visited dictionary and the priority queue.

# Topic: Graph, Dijkstra's Algorithm, BFS