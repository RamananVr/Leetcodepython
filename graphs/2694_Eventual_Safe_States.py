"""
LeetCode Problem #2694: Eventual Safe States

Problem Statement:
A directed graph of `n` nodes is represented as a list of `n` adjacency lists, where `graph[i]` is a list of nodes that node `i` can directly reach. A node is considered "safe" if it can only reach terminal nodes (nodes with no outgoing edges) or other safe nodes.

Return an array containing all the safe nodes of the graph in ascending order.

Constraints:
- `n == graph.length`
- `1 <= n <= 10^4`
- `0 <= graph[i].length <= n`
- `0 <= graph[i][j] <= n - 1`
- The graph may contain self-loops or duplicate edges.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation:
- Node 5 and 6 are terminal nodes.
- Node 2 can reach only terminal nodes (5 and 6).
- Node 4 can reach only terminal nodes (5 and 6).
- Node 3 can reach node 0, which eventually reaches terminal nodes.
- Node 0 and 1 are not safe because they form a cycle.

"""

# Python Solution
from collections import deque

def eventualSafeNodes(graph):
    n = len(graph)
    reverse_graph = [[] for _ in range(n)]
    out_degree = [0] * n
    
    # Build reverse graph and calculate out-degree
    for node in range(n):
        for neighbor in graph[node]:
            reverse_graph[neighbor].append(node)
        out_degree[node] = len(graph[node])
    
    # Start with terminal nodes (nodes with out-degree 0)
    queue = deque([node for node in range(n) if out_degree[node] == 0])
    safe_nodes = set(queue)
    
    while queue:
        current = queue.popleft()
        for neighbor in reverse_graph[current]:
            out_degree[neighbor] -= 1
            if out_degree[neighbor] == 0:
                safe_nodes.add(neighbor)
                queue.append(neighbor)
    
    return sorted(safe_nodes)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    graph1 = [[1,2],[2,3],[5],[0],[5],[],[]]
    print(eventualSafeNodes(graph1))  # Output: [2,4,5,6]

    # Test Case 2
    graph2 = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
    print(eventualSafeNodes(graph2))  # Output: [4]

    # Test Case 3
    graph3 = [[],[0,2,3,4],[3],[4],[]]
    print(eventualSafeNodes(graph3))  # Output: [0,1,2,3,4]

    # Test Case 4
    graph4 = [[1],[2],[3],[4],[]]
    print(eventualSafeNodes(graph4))  # Output: [0,1,2,3,4]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the reverse graph takes O(E), where E is the number of edges in the graph.
- Traversing the graph using BFS takes O(V + E), where V is the number of nodes and E is the number of edges.
- Sorting the safe nodes takes O(V log V).
- Overall time complexity: O(V + E + V log V).

Space Complexity:
- The reverse graph takes O(V + E) space.
- The out-degree array takes O(V) space.
- The queue and safe_nodes set take O(V) space.
- Overall space complexity: O(V + E).

Topic: Graphs
"""