"""
LeetCode Problem #785: Is Graph Bipartite?

Problem Statement:
There is an undirected graph with `n` nodes, where each node is numbered between `0` and `n - 1`. 
You are given a 2D array `graph`, where `graph[u]` is an array of nodes that node `u` is adjacent to. 
More formally, for each `v` in `graph[u]`, there is an undirected edge between node `u` and node `v`. 
The graph has the following properties:
- There are no self-edges (i.e., `graph[u]` does not contain `u`).
- There are no parallel edges (i.e., there is at most one edge between any two nodes).
- The graph may not be connected, meaning there may be two nodes `u` and `v` such that there is no path between them.

A graph is bipartite if the nodes can be partitioned into two independent sets `A` and `B` such that every edge in the graph connects a node in set `A` and a node in set `B`.

Return `true` if and only if it is bipartite.
"""

from collections import deque

def isBipartite(graph):
    """
    Determines if the given graph is bipartite.

    :param graph: List[List[int]] - adjacency list representation of the graph
    :return: bool - True if the graph is bipartite, False otherwise
    """
    n = len(graph)
    color = [-1] * n  # -1 means uncolored, 0 and 1 are the two colors

    def bfs(start):
        queue = deque([start])
        color[start] = 0  # Start coloring with 0
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if color[neighbor] == -1:  # If the neighbor is uncolored
                    color[neighbor] = 1 - color[node]  # Assign the opposite color
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:  # If the neighbor has the same color
                    return False
        return True

    for i in range(n):
        if color[i] == -1:  # If the node is unvisited
            if not bfs(i):
                return False

    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: A simple bipartite graph
    graph1 = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(isBipartite(graph1))  # Expected output: True

    # Test Case 2: A graph that is not bipartite
    graph2 = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    print(isBipartite(graph2))  # Expected output: False

    # Test Case 3: A disconnected graph that is bipartite
    graph3 = [[1], [0], [3], [2]]
    print(isBipartite(graph3))  # Expected output: True

    # Test Case 4: A single node graph
    graph4 = [[]]
    print(isBipartite(graph4))  # Expected output: True

    # Test Case 5: A graph with no edges
    graph5 = [[], [], []]
    print(isBipartite(graph5))  # Expected output: True

"""
Time Complexity:
- Let `n` be the number of nodes and `e` be the number of edges in the graph.
- Each node is visited once, and each edge is traversed once during the BFS.
- Therefore, the time complexity is O(n + e).

Space Complexity:
- The space complexity is O(n) due to the `color` array and the BFS queue.

Topic: Graphs
"""