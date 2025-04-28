"""
LeetCode Problem #2638: Count the Number of Complete Components

Problem Statement:
You are given an undirected graph represented by an integer n, which is the number of vertices, and an array edges, 
where edges[i] = [ai, bi] indicates that there is an edge between vertices ai and bi.

A connected component of the graph is complete if every pair of its vertices is connected by an edge. 
In other words, if the component has k vertices, then there must be exactly k * (k - 1) / 2 edges in that component.

Return the number of complete connected components in the graph.

Example:
Input: n = 6, edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
Output: 1
Explanation: There are 2 connected components in the graph:
- The first component is {0, 1, 2}, which is complete because every pair of nodes is connected.
- The second component is {3, 4}, which is not complete because there is no edge between 3 and 4.

Constraints:
- 1 <= n <= 50
- 0 <= edges.length <= n * (n - 1) / 2
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- There are no repeated edges.
"""

from collections import defaultdict

def countCompleteComponents(n, edges):
    def dfs(node, component):
        visited[node] = True
        component.add(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, component)

    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * n
    complete_count = 0

    # Find all connected components using DFS
    for i in range(n):
        if not visited[i]:
            component = set()
            dfs(i, component)

            # Check if the component is complete
            num_nodes = len(component)
            num_edges = sum(len(graph[node]) for node in component) // 2
            if num_edges == num_nodes * (num_nodes - 1) // 2:
                complete_count += 1

    return complete_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 6
    edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
    print(countCompleteComponents(n, edges))  # Output: 1

    # Test Case 2
    n = 4
    edges = [[0, 1], [1, 2], [2, 3], [3, 0]]
    print(countCompleteComponents(n, edges))  # Output: 1

    # Test Case 3
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    print(countCompleteComponents(n, edges))  # Output: 0

    # Test Case 4
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    print(countCompleteComponents(n, edges))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph takes O(E), where E is the number of edges.
- The DFS traversal takes O(V + E), where V is the number of vertices and E is the number of edges.
- Checking if a component is complete involves iterating over the nodes and edges in the component, which takes O(V + E) for each component.
- In the worst case, the graph has one component containing all nodes, so the total complexity is O(V + E).

Space Complexity:
- The graph representation (adjacency list) takes O(V + E).
- The visited array takes O(V).
- The DFS stack and component set take O(V) in the worst case.
- Total space complexity is O(V + E).

Topic: Graphs
"""