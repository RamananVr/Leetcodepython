"""
LeetCode Problem #1192: Critical Connections in a Network

Problem Statement:
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network 
where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach other servers 
directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other servers.

You are given the integer n, the number of servers, and the list connections, where connections[i] = [a, b] represents 
a connection between servers a and b. Return all critical connections in the network in any order.

Constraints:
- 1 <= n <= 10^5
- n-1 <= connections.length <= 10^5
- connections[i][0] != connections[i][1]
- There are no repeated connections.

Example:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[1,3]] is the only critical connection in the network. If you remove it, the network will be disconnected.

"""

# Solution
from collections import defaultdict

def criticalConnections(n, connections):
    def dfs(node, parent):
        nonlocal time
        visited[node] = True
        discovery[node] = low[node] = time
        time += 1

        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if not visited[neighbor]:
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > discovery[node]:
                    result.append([node, neighbor])
            else:
                low[node] = min(low[node], discovery[neighbor])

    # Build the graph
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize variables
    discovery = [-1] * n
    low = [-1] * n
    visited = [False] * n
    result = []
    time = 0

    # Start DFS from node 0
    dfs(0, -1)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 4
    connections1 = [[0,1],[1,2],[2,0],[1,3]]
    print(criticalConnections(n1, connections1))  # Output: [[1,3]]

    # Test Case 2
    n2 = 5
    connections2 = [[0,1],[1,2],[2,0],[1,3],[3,4]]
    print(criticalConnections(n2, connections2))  # Output: [[1,3], [3,4]]

    # Test Case 3
    n3 = 6
    connections3 = [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5]]
    print(criticalConnections(n3, connections3))  # Output: [[1,3], [3,4], [4,5]]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph takes O(connections.length).
- The DFS traversal takes O(V + E), where V is the number of nodes (n) and E is the number of edges (connections.length).
- Overall time complexity: O(n + connections.length).

Space Complexity:
- The graph representation uses O(n + connections.length) space.
- The discovery, low, and visited arrays each use O(n) space.
- The recursion stack in the worst case uses O(n) space.
- Overall space complexity: O(n + connections.length).

Topic: Graphs
"""