"""
LeetCode Problem #2858: Minimum Edge Reversals So Every Node Is Reachable

Problem Statement:
You are given a directed graph with `n` nodes labeled from `0` to `n-1` and an array `edges` where `edges[i] = [u, v]` 
indicates that there is a directed edge from node `u` to node `v`.

You are tasked to determine the minimum number of edge reversals required so that every node in the graph is reachable 
from every other node. If it is not possible to make the graph strongly connected, return -1.

Constraints:
- `1 <= n <= 10^5`
- `0 <= edges.length <= 2 * 10^5`
- `0 <= u, v < n`
- `u != v`
- All pairs `(u, v)` are unique.

Return:
- An integer representing the minimum number of edge reversals required to make the graph strongly connected, or -1 if it is not possible.
"""

from collections import defaultdict, deque

def minEdgeReversals(n, edges):
    """
    Function to calculate the minimum number of edge reversals required to make the graph strongly connected.
    
    :param n: int - Number of nodes in the graph
    :param edges: List[List[int]] - List of directed edges
    :return: int - Minimum number of edge reversals required, or -1 if not possible
    """
    # Step 1: Build the graph with both original and reversed edges
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append((v, 0))  # Original edge (u -> v) with cost 0
        graph[v].append((u, 1))  # Reversed edge (v -> u) with cost 1

    # Step 2: Perform BFS to calculate the minimum cost to reach all nodes from node 0
    def bfs(start):
        dist = {i: float('inf') for i in range(n)}
        dist[start] = 0
        queue = deque([start])

        while queue:
            node = queue.popleft()
            for neighbor, cost in graph[node]:
                if dist[node] + cost < dist[neighbor]:
                    dist[neighbor] = dist[node] + cost
                    queue.append(neighbor)

        return dist

    # Step 3: Calculate the minimum cost from node 0 to all other nodes
    dist_from_0 = bfs(0)

    # Step 4: Check if all nodes are reachable from node 0
    if any(dist == float('inf') for dist in dist_from_0.values()):
        return -1

    # Step 5: Calculate the minimum cost from each node to all other nodes
    total_reversals = sum(dist_from_0.values())
    return total_reversals


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 4
    edges1 = [[0, 1], [1, 2], [2, 3]]
    print(minEdgeReversals(n1, edges1))  # Expected Output: 3

    # Test Case 2
    n2 = 3
    edges2 = [[0, 1], [1, 2], [2, 0]]
    print(minEdgeReversals(n2, edges2))  # Expected Output: 0

    # Test Case 3
    n3 = 5
    edges3 = [[0, 1], [1, 2], [3, 4]]
    print(minEdgeReversals(n3, edges3))  # Expected Output: -1

    # Test Case 4
    n4 = 2
    edges4 = [[0, 1]]
    print(minEdgeReversals(n4, edges4))  # Expected Output: 1


"""
Time Complexity:
- Building the graph takes O(E), where E is the number of edges.
- BFS traversal takes O(V + E), where V is the number of nodes and E is the number of edges.
- Overall complexity: O(V + E).

Space Complexity:
- The graph representation takes O(V + E) space.
- The BFS queue and distance dictionary take O(V) space.
- Overall complexity: O(V + E).

Topic: Graphs, BFS
"""