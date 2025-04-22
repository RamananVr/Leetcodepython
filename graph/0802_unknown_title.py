"""
LeetCode Problem #802: Find Eventual Safe States

Problem Statement:
There is a directed graph of n nodes with each node labeled from 0 to n - 1. 
The graph is represented by a 0-indexed 2D integer array graph where graph[i] 
is an integer array of nodes that node i is connected to, meaning there is a 
directed edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node 
if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

Example 1:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation:
- Node 5 is terminal, and node 6 is terminal.
- Node 2 can only reach nodes 5 and 6, which are terminal, so node 2 is safe.
- Node 4 can only reach node 5, which is terminal, so node 4 is safe.
- Node 3 can reach node 0, which in turn can reach nodes 1, 2, 3, 4, 5, and 6, so node 3 is not safe.
- Node 0 can reach nodes 1, 2, 3, 4, 5, and 6, so node 0 is not safe.
- Node 1 can reach nodes 2, 3, 4, 5, and 6, so node 1 is not safe.

Example 2:
Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]

Constraints:
- n == graph.length
- 1 <= n <= 10^4
- 0 <= graph[i].length <= n
- 0 <= graph[i][j] <= n - 1
- graph[i] is sorted in a strictly increasing order.
- The graph may contain self-loops.
- The graph may contain cycles.
"""

from collections import deque

def eventualSafeNodes(graph):
    """
    Finds all the eventual safe nodes in a directed graph.

    :param graph: List[List[int]] - adjacency list representation of the graph
    :return: List[int] - sorted list of safe nodes
    """
    n = len(graph)
    reverse_graph = [[] for _ in range(n)]
    out_degree = [0] * n

    # Build the reverse graph and calculate out-degrees
    for node in range(n):
        for neighbor in graph[node]:
            reverse_graph[neighbor].append(node)
        out_degree[node] = len(graph[node])

    # Start with all terminal nodes (nodes with out-degree 0)
    queue = deque([node for node in range(n) if out_degree[node] == 0])
    safe_nodes = set(queue)

    # Process the queue
    while queue:
        current = queue.popleft()
        for neighbor in reverse_graph[current]:
            out_degree[neighbor] -= 1
            if out_degree[neighbor] == 0:
                safe_nodes.add(neighbor)
                queue.append(neighbor)

    # Return the sorted list of safe nodes
    return sorted(safe_nodes)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    graph1 = [[1,2],[2,3],[5],[0],[5],[],[]]
    print(eventualSafeNodes(graph1))  # Output: [2, 4, 5, 6]

    # Test Case 2
    graph2 = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
    print(eventualSafeNodes(graph2))  # Output: [4]

    # Test Case 3
    graph3 = [[],[0,2,3,4],[3],[4],[]]
    print(eventualSafeNodes(graph3))  # Output: [0, 1, 2, 3, 4]

"""
Time Complexity:
- Building the reverse graph and calculating out-degrees takes O(V + E), where V is the number of nodes and E is the number of edges.
- Processing the queue takes O(V + E) since each node and edge is processed at most once.
- Sorting the safe nodes takes O(V log V).
- Overall: O(V + E + V log V).

Space Complexity:
- The reverse graph takes O(V + E) space.
- The out-degree array takes O(V) space.
- The queue and safe_nodes set take O(V) space.
- Overall: O(V + E).

Topic: Graph
"""