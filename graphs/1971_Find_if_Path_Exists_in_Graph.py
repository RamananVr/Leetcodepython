"""
LeetCode Problem #1971: Find if Path Exists in Graph

Problem Statement:
There is a bi-directional graph with `n` vertices, where each vertex is labeled from `0` to `n - 1` 
(inclusive). The edges in the graph are represented as a 2D integer array `edges`, where each 
`edges[i] = [ui, vi]` denotes a bi-directional edge between vertex `ui` and vertex `vi`. 
Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You are given the integer `n` and the array `edges`. You are also given two integers, `source` 
and `destination`, that represent the start and end vertices, respectively.

Return `true` if there is a valid path from `source` to `destination` in the graph, or `false` otherwise.

Constraints:
- `1 <= n <= 2 * 10^5`
- `0 <= edges.length <= 2 * 10^5`
- `edges[i].length == 2`
- `0 <= ui, vi <= n - 1`
- `ui != vi`
- `0 <= source, destination <= n - 1`

Example:
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: true
Explanation: There is a path from 0 to 5 via the vertices 0 -> 2 -> 3 -> 5.

"""

from collections import defaultdict, deque

def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    # Step 1: Build the adjacency list for the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Step 2: Perform BFS to check if a path exists
    visited = set()
    queue = deque([source])
    
    while queue:
        current = queue.popleft()
        
        # If we reach the destination, return True
        if current == destination:
            return True
        
        # Mark the current node as visited
        visited.add(current)
        
        # Add all unvisited neighbors to the queue
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
    
    # If we exhaust the queue without finding the destination, return False
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 6
    edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    source = 0
    destination = 5
    print(validPath(n, edges, source, destination))  # Output: True

    # Test Case 2
    n = 3
    edges = [[0,1],[1,2],[2,0]]
    source = 0
    destination = 2
    print(validPath(n, edges, source, destination))  # Output: True

    # Test Case 3
    n = 3
    edges = [[0,1]]
    source = 0
    destination = 2
    print(validPath(n, edges, source, destination))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the adjacency list takes O(E), where E is the number of edges.
- In the worst case, BFS visits all vertices and edges, which takes O(V + E), where V is the number of vertices.
- Overall time complexity: O(V + E).

Space Complexity:
- The adjacency list requires O(V + E) space.
- The visited set and the queue each require O(V) space in the worst case.
- Overall space complexity: O(V + E).

Topic: Graphs
"""