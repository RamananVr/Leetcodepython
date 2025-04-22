"""
LeetCode Problem #924: Minimize Malware Spread

Problem Statement:
You are given a graph represented by an adjacency matrix `graph`, where `graph[i][j] = 1` indicates that node `i` is directly connected to node `j`, and `graph[i][j] = 0` indicates that they are not directly connected.

Initially, some nodes are infected by malware. You are given a list `initial` containing the indices of these infected nodes. You can remove exactly one node from the `initial` list. Removing a node will prevent it from spreading malware to its neighbors.

Return the node that, if removed, minimizes the total number of nodes infected by malware in the graph. If multiple nodes produce the same result, return the smallest index.

Constraints:
- `graph.length == graph[i].length`
- `2 <= graph.length <= 300`
- `graph[i][j]` is `0` or `1`.
- `graph[i][i] == 1`
- `1 <= initial.length <= graph.length`
- `0 <= initial[i] < graph.length`

---

Solution:
"""

from collections import defaultdict

def minimizeMalwareSpread(graph, initial):
    def dfs(node, visited, component):
        visited[node] = True
        component.append(node)
        for neighbor in range(len(graph)):
            if graph[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor, visited, component)

    # Step 1: Find all connected components
    n = len(graph)
    visited = [False] * n
    components = []
    node_to_component = {}

    for i in range(n):
        if not visited[i]:
            component = []
            dfs(i, visited, component)
            components.append(component)
            for node in component:
                node_to_component[node] = len(components) - 1

    # Step 2: Count malware nodes in each component
    component_malware_count = defaultdict(int)
    for node in initial:
        component_malware_count[node_to_component[node]] += 1

    # Step 3: Evaluate the impact of removing each node
    result = (-1, -1)  # (max_saved_nodes, node_to_remove)
    initial.sort()  # Ensure smallest index is chosen in case of ties

    for node in initial:
        component_idx = node_to_component[node]
        if component_malware_count[component_idx] == 1:  # Only one malware node in the component
            saved_nodes = len(components[component_idx])
            if saved_nodes > result[0] or (saved_nodes == result[0] and node < result[1]):
                result = (saved_nodes, node)

    return result[1] if result[1] != -1 else min(initial)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    graph1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    initial1 = [0, 1]
    print(minimizeMalwareSpread(graph1, initial1))  # Output: 0

    # Test Case 2
    graph2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    initial2 = [0, 2]
    print(minimizeMalwareSpread(graph2, initial2))  # Output: 0

    # Test Case 3
    graph3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    initial3 = [1, 2]
    print(minimizeMalwareSpread(graph3, initial3))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The DFS traversal takes O(V + E), where V is the number of nodes and E is the number of edges in the graph.
- Sorting the `initial` list takes O(k log k), where k is the size of the `initial` list.
- Overall complexity is O(V + E + k log k), which is efficient given the constraints.

Space Complexity:
- The `visited` array and `components` list take O(V) space.
- The `node_to_component` dictionary takes O(V) space.
- Overall space complexity is O(V).

Topic: Graphs
"""