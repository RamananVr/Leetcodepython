"""
LeetCode Problem #928: Minimize Malware Spread II

Problem Statement:
You are given a network of `n` nodes represented as an `n x n` adjacency matrix `graph`, 
where the `i-th` node is directly connected to the `j-th` node if `graph[i][j] == 1`.

Some nodes are initially infected by malware. This is given as an integer array `initial`, 
where each `initial[i]` is the index of a node initially infected.

Whenever two nodes are directly connected and at least one of those two nodes is infected 
by malware, both nodes will be infected by malware. This spread of malware will continue 
until no more nodes can be infected in this manner.

Suppose `M(initial)` is the final number of nodes infected with malware in the entire network, 
after the spread of the malware stops.

We will remove exactly one node from `initial`. Return the node that, if removed, would minimize 
`M(initial)`. If multiple nodes could be removed to minimize `M(initial)`, return such a node 
with the smallest index.

Constraints:
- `n == graph.length`
- `n == graph[i].length`
- `2 <= n <= 300`
- `graph[i][j]` is `0` or `1`.
- `graph[i][i] == 1`
- `1 <= initial.length <= n`
- `0 <= initial[i] <= n - 1`
- All the integers in `initial` are distinct.

Example:
Input: graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
Output: 0

Input: graph = [[1,0,0],[0,1,0],[0,0,1]], initial = [0,2]
Output: 0

Input: graph = [[1,1,1],[1,1,1],[1,1,1]], initial = [1,2]
Output: 1
"""

from collections import defaultdict, deque

def minMalwareSpread(graph, initial):
    def bfs(node):
        """Perform BFS to find all nodes in the connected component of `node`."""
        queue = deque([node])
        visited = set([node])
        while queue:
            current = queue.popleft()
            for neighbor, is_connected in enumerate(graph[current]):
                if is_connected and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return visited

    n = len(graph)
    initial_set = set(initial)
    connected_components = {}
    infected_count = defaultdict(int)

    # Find all connected components and count infections in each
    visited = set()
    for i in range(n):
        if i not in visited:
            component = bfs(i)
            for node in component:
                connected_components[node] = component
            visited.update(component)

    for node in initial:
        for neighbor in connected_components[node]:
            infected_count[neighbor] += 1

    # Evaluate the impact of removing each node in `initial`
    best_node = min(initial)
    best_reduction = -1

    for node in initial:
        reduction = 0
        for neighbor in connected_components[node]:
            if infected_count[neighbor] == 1:  # Only this node is responsible for infection
                reduction += 1
        if reduction > best_reduction or (reduction == best_reduction and node < best_node):
            best_reduction = reduction
            best_node = node

    return best_node

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    graph1 = [[1,1,0],[1,1,0],[0,0,1]]
    initial1 = [0,1]
    print(minMalwareSpread(graph1, initial1))  # Output: 0

    # Test Case 2
    graph2 = [[1,0,0],[0,1,0],[0,0,1]]
    initial2 = [0,2]
    print(minMalwareSpread(graph2, initial2))  # Output: 0

    # Test Case 3
    graph3 = [[1,1,1],[1,1,1],[1,1,1]]
    initial3 = [1,2]
    print(minMalwareSpread(graph3, initial3))  # Output: 1

"""
Time Complexity:
- BFS for each node takes O(V + E), where V is the number of nodes and E is the number of edges.
- In the worst case, we perform BFS for all nodes, so the complexity is O(n^2) due to the adjacency matrix representation.
- Evaluating the impact of removing each node in `initial` takes O(n).
- Overall time complexity: O(n^2).

Space Complexity:
- The space required for the BFS queue and visited set is O(n).
- The connected_components dictionary and infected_count dictionary also take O(n) space.
- Overall space complexity: O(n).

Topic: Graphs
"""