"""
LeetCode Question #2077: Paths in Maze That Lead to Same Room

Problem Statement:
You are given a maze represented as a directed graph. The maze consists of `n` rooms numbered from `0` to `n-1`, and you are given a list of directed edges `edges` where `edges[i] = [u, v]` indicates that there is a directed edge from room `u` to room `v`.

A path in the maze is a sequence of rooms such that:
- The first room is the starting room.
- Each subsequent room is reachable from the previous room via a directed edge.

Two paths are said to lead to the same room if they both end at the same room.

Your task is to determine the number of pairs of paths that lead to the same room.

Write a function `countPathsToSameRoom(n: int, edges: List[List[int]]) -> int` that takes:
- `n`: the number of rooms in the maze.
- `edges`: the list of directed edges.

Return the number of pairs of paths that lead to the same room.

Constraints:
- `1 <= n <= 1000`
- `1 <= edges.length <= 2000`
- `0 <= u, v < n`
"""

from collections import defaultdict
from itertools import combinations

def countPathsToSameRoom(n: int, edges: list[list[int]]) -> int:
    """
    Count the number of pairs of paths that lead to the same room.

    :param n: Number of rooms in the maze.
    :param edges: List of directed edges in the maze.
    :return: Number of pairs of paths that lead to the same room.
    """
    # Step 1: Build adjacency list for the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    # Step 2: Perform DFS to find all paths leading to each room
    room_paths = defaultdict(list)  # room_paths[room] = list of paths leading to this room
    
    def dfs(current_room, path):
        path.append(current_room)
        room_paths[current_room].append(tuple(path))  # Store the path as a tuple
        for neighbor in graph[current_room]:
            dfs(neighbor, path[:])  # Pass a copy of the path to avoid mutation
    
    for room in range(n):
        dfs(room, [])
    
    # Step 3: Count pairs of paths leading to the same room
    count = 0
    for paths in room_paths.values():
        if len(paths) > 1:
            count += len(list(combinations(paths, 2)))  # Count pairs of paths
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 4
    edges1 = [[0, 1], [0, 2], [1, 3], [2, 3]]
    print(countPathsToSameRoom(n1, edges1))  # Expected Output: 1 (Paths [0->1->3] and [0->2->3] lead to room 3)

    # Test Case 2
    n2 = 3
    edges2 = [[0, 1], [1, 2], [0, 2]]
    print(countPathsToSameRoom(n2, edges2))  # Expected Output: 1 (Paths [0->1->2] and [0->2] lead to room 2)

    # Test Case 3
    n3 = 5
    edges3 = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4]]
    print(countPathsToSameRoom(n3, edges3))  # Expected Output: 0 (No pairs of paths lead to the same room)

# Time and Space Complexity Analysis
"""
Time Complexity:
- Building the adjacency list: O(edges.length)
- DFS traversal: O(n * edges.length) in the worst case (if every room is connected to every other room).
- Counting pairs of paths: O(P^2) for each room, where P is the number of paths leading to a room.
Overall complexity: O(n * edges.length + P^2), where P is the maximum number of paths leading to a room.

Space Complexity:
- Adjacency list: O(edges.length)
- Room paths storage: O(P), where P is the total number of paths stored.
- DFS stack: O(n) in the worst case.
Overall complexity: O(edges.length + P + n).
"""

# Topic: Graphs