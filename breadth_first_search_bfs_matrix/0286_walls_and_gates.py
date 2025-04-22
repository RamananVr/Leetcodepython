"""
LeetCode Question #286: Walls and Gates

Problem Statement:
You are given a m x n grid rooms initialized with these three possible values:
- -1 represents a wall or an obstacle.
- 0 represents a gate.
- INF represents an empty room. INF is a constant value (2^31 - 1).

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, leave the room as INF.

You may assume that there are no gates adjacent to a wall, and that the grid has at least one gate.

Example:
Input:
rooms = [
    [INF, -1,  0, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, -1],
    [  0, -1, INF, INF]
]

Output:
rooms = [
    [  3, -1,   0,   1],
    [  2,   2,   1,  -1],
    [  1,  -1,   2,  -1],
    [  0,  -1,   3,   4]
]
"""

from collections import deque

def walls_and_gates(rooms):
    """
    Modify the input grid `rooms` in-place to fill each empty room with the distance to its nearest gate.
    
    :param rooms: List[List[int]] - 2D grid of integers representing rooms, walls, and gates.
    :return: None
    """
    if not rooms or not rooms[0]:
        return
    
    INF = 2**31 - 1
    rows, cols = len(rooms), len(rooms[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque()
    
    # Add all gates to the queue
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))
    
    # Perform BFS from all gates
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and rooms[nx][ny] == INF:
                rooms[nx][ny] = rooms[x][y] + 1
                queue.append((nx, ny))

# Example Test Cases
if __name__ == "__main__":
    INF = 2**31 - 1
    rooms = [
        [INF, -1,  0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [  0, -1, INF, INF]
    ]
    walls_and_gates(rooms)
    print("Output:")
    for row in rooms:
        print(row)

"""
Time and Space Complexity Analysis:

Time Complexity:
- The BFS traversal visits each cell in the grid at most once.
- Therefore, the time complexity is O(m * n), where m is the number of rows and n is the number of columns.

Space Complexity:
- The space complexity is determined by the queue used in BFS. In the worst case, the queue can contain all the gates and their neighbors.
- Therefore, the space complexity is O(m * n).

Topic: Breadth-First Search (BFS), Matrix
"""