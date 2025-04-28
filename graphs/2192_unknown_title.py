"""
LeetCode Problem #2192: All Ancestors of a Node in a Directed Acyclic Graph

Problem Statement:
You are given a directed acyclic graph (DAG) with `n` nodes labeled from `0` to `n - 1`. The graph is represented by a list of edges, where `edges[i] = [from_i, to_i]` indicates that there is a directed edge from node `from_i` to node `to_i`.

Return a list `answer`, where `answer[i]` is a list of all ancestors of the `i-th` node, sorted in ascending order.

A node `u` is an ancestor of a node `v` if there is a directed path from `u` to `v`.

Constraints:
- `1 <= n <= 1000`
- `0 <= edges.length <= min(2000, n * (n - 1) / 2)`
- `edges[i].length == 2`
- `0 <= from_i, to_i < n`
- `from_i != to_i`
- The graph is a DAG.

Example:
Input: n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[4,6]]
Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[2]]

Explanation:
- Node 0 has no ancestors.
- Node 1 has no ancestors.
- Node 2 has no ancestors.
- Node 3 has ancestors [0, 1].
- Node 4 has ancestors [0, 2].
- Node 5 has ancestors [0, 1, 3].
- Node 6 has ancestors [0, 1, 2, 3, 4].
- Node 7 has ancestors [2].
"""

from collections import defaultdict, deque

def getAncestors(n, edges):
    """
    Function to compute all ancestors of each node in a directed acyclic graph.

    :param n: int - Number of nodes in the graph.
    :param edges: List[List[int]] - List of directed edges in the graph.
    :return: List[List[int]] - List of sorted ancestors for each node.
    """
    # Step 1: Build the graph and compute in-degrees
    graph = defaultdict(list)
    in_degree = [0] * n
    for from_node, to_node in edges:
        graph[from_node].append(to_node)
        in_degree[to_node] += 1

    # Step 2: Perform topological sort using Kahn's algorithm
    topo_order = []
    queue = deque([node for node in range(n) if in_degree[node] == 0])
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 3: Compute ancestors for each node
    ancestors = [set() for _ in range(n)]
    for node in topo_order:
        for neighbor in graph[node]:
            ancestors[neighbor].update(ancestors[node])
            ancestors[neighbor].add(node)

    # Step 4: Convert sets to sorted lists
    return [sorted(list(ancestor_set)) for ancestor_set in ancestors]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 8
    edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[4,6]]
    print(getAncestors(n, edges))  # Expected: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[2]]

    # Test Case 2
    n = 5
    edges = [[0,1],[0,2],[1,3],[1,4],[2,4]]
    print(getAncestors(n, edges))  # Expected: [[],[0],[0],[0,1],[0,1,2]]

    # Test Case 3
    n = 3
    edges = [[0,1],[1,2]]
    print(getAncestors(n, edges))  # Expected: [[],[0],[0,1]]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph and computing in-degrees: O(E), where E is the number of edges.
- Topological sort using Kahn's algorithm: O(V + E), where V is the number of nodes.
- Computing ancestors for each node: O(V + E), as we traverse the graph and update ancestor sets.
- Sorting the ancestor sets: O(V * A), where A is the average size of the ancestor set.

Overall: O(V + E + V * A)

Space Complexity:
- Graph representation: O(V + E)
- In-degree array: O(V)
- Ancestors list: O(V * A), where A is the average size of the ancestor set.

Overall: O(V + E + V * A)

Topic: Graphs
"""