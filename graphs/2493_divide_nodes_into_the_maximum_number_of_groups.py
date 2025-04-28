"""
LeetCode Question #2493: Divide Nodes Into the Maximum Number of Groups

Problem Statement:
You are given a positive integer `n` representing the number of nodes in an undirected graph, and a 2D integer array `edges`, where `edges[i] = [ui, vi]` indicates that there is an edge between nodes `ui` and `vi`.

Divide the nodes into the maximum number of groups such that:
1. Each node belongs to exactly one group.
2. For every edge `[ui, vi]`, if `ui` belongs to group `x` and `vi` belongs to group `y`, then `|x - y| = 1`.

Return the maximum number of groups you can achieve. If it is impossible to divide the nodes into groups satisfying the conditions, return `-1`.

Constraints:
- `1 <= n <= 500`
- `1 <= edges.length <= 10^4`
- `edges[i].length == 2`
- `1 <= ui, vi <= n`
- `ui != vi`
- There are no duplicate edges.

"""

from collections import deque, defaultdict

def magnificent_groups(n, edges):
    """
    Function to divide nodes into the maximum number of groups satisfying the conditions.
    
    Args:
    n (int): Number of nodes in the graph.
    edges (List[List[int]]): List of edges in the graph.
    
    Returns:
    int: Maximum number of groups, or -1 if impossible.
    """
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS to check bipartite and calculate depth
    def bfs(node):
        queue = deque([(node, 0)])  # (current node, depth)
        visited[node] = 0  # Start with depth 0
        max_depth = 0
        
        while queue:
            current, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited[neighbor] = depth + 1
                    queue.append((neighbor, depth + 1))
                elif abs(visited[neighbor] - visited[current]) != 1:
                    return -1  # Not bipartite
        
        return max_depth
    
    visited = {}
    total_groups = 0
    
    for node in range(1, n + 1):
        if node not in visited:
            result = bfs(node)
            if result == -1:
                return -1  # Impossible to divide into groups
            total_groups += result + 1  # Add the depth of the connected component
    
    return total_groups


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 6
    edges1 = [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6]]
    print(magnificent_groups(n1, edges1))  # Expected Output: 4

    # Test Case 2
    n2 = 3
    edges2 = [[1, 2], [1, 3], [2, 3]]
    print(magnificent_groups(n2, edges2))  # Expected Output: -1

    # Test Case 3
    n3 = 4
    edges3 = [[1, 2], [2, 3], [3, 4]]
    print(magnificent_groups(n3, edges3))  # Expected Output: 3

    # Test Case 4
    n4 = 5
    edges4 = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
    print(magnificent_groups(n4, edges4))  # Expected Output: -1


"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the adjacency list takes O(edges.length).
- BFS traversal for each connected component takes O(V + E), where V is the number of nodes and E is the number of edges in the component.
- In the worst case, we traverse all nodes and edges, so the total time complexity is O(n + edges.length).

Space Complexity:
- The adjacency list takes O(n + edges.length) space.
- The visited dictionary takes O(n) space.
- The BFS queue takes O(n) space in the worst case.
- Total space complexity is O(n + edges.length).

Topic: Graphs
"""