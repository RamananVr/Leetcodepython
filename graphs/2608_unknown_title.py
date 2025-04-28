"""
LeetCode Problem #2608: Shortest Cycle in a Graph

Problem Statement:
You are given an undirected graph represented by an integer n, the number of nodes, and a list edges, 
where edges[i] = [u_i, v_i] indicates that there is an undirected edge between nodes u_i and v_i.

Return the length of the shortest cycle in the graph. If there are no cycles, return -1.

A cycle is a path that starts and ends at the same node, and each edge is visited exactly once.

Constraints:
- 2 <= n <= 1000
- 1 <= edges.length <= 1000
- edges[i].length == 2
- 0 <= u_i, v_i < n
- u_i != v_i
- There are no duplicate edges.
"""

from collections import deque

def shortest_cycle(n, edges):
    """
    Finds the length of the shortest cycle in an undirected graph.

    :param n: int - Number of nodes in the graph.
    :param edges: List[List[int]] - List of edges in the graph.
    :return: int - Length of the shortest cycle, or -1 if no cycle exists.
    """
    # Build adjacency list
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start):
        # Perform BFS to find the shortest cycle starting from `start`
        visited = [-1] * n  # -1 indicates unvisited
        queue = deque([(start, -1)])  # (current_node, parent_node)
        visited[start] = 0  # Distance from start node

        while queue:
            node, parent = queue.popleft()

            for neighbor in graph[node]:
                if visited[neighbor] == -1:  # If neighbor is unvisited
                    visited[neighbor] = visited[node] + 1
                    queue.append((neighbor, node))
                elif neighbor != parent:  # If neighbor is visited and not the parent
                    # Cycle detected: calculate cycle length
                    return visited[node] + visited[neighbor] + 1

        return float('inf')  # No cycle found

    # Find the shortest cycle in the graph
    shortest = float('inf')
    for i in range(n):
        shortest = min(shortest, bfs(i))

    return shortest if shortest != float('inf') else -1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Graph with a cycle
    n1 = 5
    edges1 = [[0, 1], [1, 2], [2, 3], [3, 0], [3, 4]]
    print(shortest_cycle(n1, edges1))  # Expected Output: 4

    # Test Case 2: Graph with no cycle
    n2 = 4
    edges2 = [[0, 1], [1, 2], [2, 3]]
    print(shortest_cycle(n2, edges2))  # Expected Output: -1

    # Test Case 3: Graph with multiple cycles
    n3 = 6
    edges3 = [[0, 1], [1, 2], [2, 0], [2, 3], [3, 4], [4, 5], [5, 3]]
    print(shortest_cycle(n3, edges3))  # Expected Output: 3

    # Test Case 4: Single cycle
    n4 = 3
    edges4 = [[0, 1], [1, 2], [2, 0]]
    print(shortest_cycle(n4, edges4))  # Expected Output: 3


"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the adjacency list takes O(edges.length).
- BFS is performed for each node. In the worst case, BFS visits all nodes and edges, taking O(n + edges.length).
- Therefore, the overall time complexity is O(n * (n + edges.length)).

Space Complexity:
- The adjacency list takes O(n + edges.length) space.
- The visited array and BFS queue take O(n) space.
- Therefore, the overall space complexity is O(n + edges.length).

Topic: Graphs
"""