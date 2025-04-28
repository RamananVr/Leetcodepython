"""
LeetCode Problem #2685: Count the Number of Complete Components

Problem Statement:
You are given an undirected graph represented by an integer `n`, the number of nodes, and a 2D integer array `edges`, 
where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi`.

A connected component of the graph is called "complete" if every pair of nodes in the component is directly connected 
by an edge.

Return the number of complete connected components in the graph.

Constraints:
- 1 <= n <= 50
- 0 <= edges.length <= n * (n - 1) / 2
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- There are no repeated edges.

Example:
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 1
Explanation: There is one complete component, which is the component containing nodes [0,1,2].

Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[4,5],[3,5]]
Output: 2
Explanation: There are two complete components: [0,1,2] and [3,4,5].
"""

from collections import defaultdict, deque

def countCompleteComponents(n, edges):
    # Step 1: Build the adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Step 2: Helper function to perform BFS and collect nodes in a connected component
    def bfs(node, visited):
        queue = deque([node])
        visited.add(node)
        component_nodes = set()
        component_edges = 0
        
        while queue:
            current = queue.popleft()
            component_nodes.add(current)
            for neighbor in graph[current]:
                component_edges += 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return component_nodes, component_edges // 2  # Each edge is counted twice
    
    # Step 3: Iterate through all nodes and find connected components
    visited = set()
    complete_components = 0
    
    for i in range(n):
        if i not in visited:
            component_nodes, component_edges = bfs(i, visited)
            # A component is complete if the number of edges equals the number of pairs of nodes
            num_nodes = len(component_nodes)
            if component_edges == (num_nodes * (num_nodes - 1)) // 2:
                complete_components += 1
    
    return complete_components

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 6
    edges1 = [[0,1],[0,2],[1,2],[3,4]]
    print(countCompleteComponents(n1, edges1))  # Output: 1

    # Test Case 2
    n2 = 6
    edges2 = [[0,1],[0,2],[1,2],[3,4],[4,5],[3,5]]
    print(countCompleteComponents(n2, edges2))  # Output: 2

    # Test Case 3
    n3 = 4
    edges3 = [[0,1],[1,2]]
    print(countCompleteComponents(n3, edges3))  # Output: 0

    # Test Case 4
    n4 = 5
    edges4 = [[0,1],[1,2],[2,0],[3,4]]
    print(countCompleteComponents(n4, edges4))  # Output: 2

"""
Time Complexity Analysis:
- Building the adjacency list takes O(E), where E is the number of edges.
- BFS traversal for all nodes takes O(V + E), where V is the number of nodes and E is the number of edges.
- Checking if a component is complete involves counting nodes and edges, which is O(1) for each component.
- Overall time complexity: O(V + E).

Space Complexity Analysis:
- The adjacency list requires O(V + E) space.
- The visited set and queue require O(V) space.
- Overall space complexity: O(V + E).

Topic: Graphs
"""