"""
LeetCode Question #2685: Count the Number of Complete Components

Problem Statement:
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph in which there is a path between every pair of vertices, and which is connected to no additional vertices in the supergraph.

A connected component is said to be complete if there is an edge between every pair of vertices in the component.

Examples:
Example 1:
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3
Explanation: From the picture above, one can see that there are 3 connected components: [0, 1, 2], [3, 4], and [5].
The component [0, 1, 2] has edges between every pair of vertices, so it is complete.
The component [3, 4] has only 1 edge but needs 1 edge (since there are 2 vertices), so it is complete.
The component [5] has no edges but needs 0 edges (since there is only 1 vertex), so it is complete.

Example 2:
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output: 1
Explanation: The component [0, 1, 2] is complete since there is an edge between every pair of vertices.
The component [3, 4, 5] is not complete since there is no edge between 4 and 5.
The component [3, 4, 5] needs 3 edges but only has 2.

Constraints:
- 1 <= n <= 50
- 0 <= edges.length <= n * (n - 1) / 2
- edges[i].length == 2
- 0 <= ai, bi <= n - 1
- ai != bi
- There are no repeated edges.
"""

from typing import List, Set
from collections import defaultdict, deque

def countCompleteComponents(n: int, edges: List[List[int]]) -> int:
    """
    Count complete connected components using DFS.
    
    A complete component has edges between every pair of vertices.
    For a component with k vertices, it needs k*(k-1)/2 edges.
    
    Time Complexity: O(n + m) where m is number of edges
    Space Complexity: O(n + m)
    """
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * n
    complete_components = 0
    
    def dfs(node: int, component: Set[int]) -> None:
        visited[node] = True
        component.add(node)
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, component)
    
    # Find all connected components
    for i in range(n):
        if not visited[i]:
            component = set()
            dfs(i, component)
            
            # Check if component is complete
            component_size = len(component)
            expected_edges = component_size * (component_size - 1) // 2
            
            # Count actual edges in this component
            actual_edges = 0
            for node in component:
                for neighbor in graph[node]:
                    if neighbor in component and neighbor > node:
                        actual_edges += 1
            
            if actual_edges == expected_edges:
                complete_components += 1
    
    return complete_components

def countCompleteComponentsBFS(n: int, edges: List[List[int]]) -> int:
    """
    Count complete connected components using BFS.
    
    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * n
    complete_components = 0
    
    def bfs(start: int) -> Set[int]:
        queue = deque([start])
        component = set([start])
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    component.add(neighbor)
        
        return component
    
    # Find all connected components
    for i in range(n):
        if not visited[i]:
            component = bfs(i)
            
            # Check if component is complete
            component_size = len(component)
            expected_edges = component_size * (component_size - 1) // 2
            
            # Count actual edges in this component
            actual_edges = 0
            for node in component:
                for neighbor in graph[node]:
                    if neighbor in component and neighbor > node:
                        actual_edges += 1
            
            if actual_edges == expected_edges:
                complete_components += 1
    
    return complete_components

def countCompleteComponentsUnionFind(n: int, edges: List[List[int]]) -> int:
    """
    Use Union-Find to group components, then check completeness.
    
    Time Complexity: O(n + m * α(n)) where α is inverse Ackermann
    Space Complexity: O(n)
    """
    parent = list(range(n))
    
    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x: int, y: int) -> None:
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    
    # Union all connected vertices
    for u, v in edges:
        union(u, v)
    
    # Group vertices by component
    components = defaultdict(list)
    for i in range(n):
        components[find(i)].append(i)
    
    # Build adjacency list for edge counting
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    complete_components = 0
    
    # Check each component
    for component_vertices in components.values():
        component_size = len(component_vertices)
        expected_edges = component_size * (component_size - 1) // 2
        
        # Count actual edges
        actual_edges = 0
        component_set = set(component_vertices)
        
        for node in component_vertices:
            for neighbor in graph[node]:
                if neighbor in component_set and neighbor > node:
                    actual_edges += 1
        
        if actual_edges == expected_edges:
            complete_components += 1
    
    return complete_components

def countCompleteComponentsOptimized(n: int, edges: List[List[int]]) -> int:
    """
    Optimized version that counts edges while building components.
    
    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    """
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    visited = [False] * n
    complete_components = 0
    
    def dfs(node: int, component: List[int]) -> int:
        visited[node] = True
        component.append(node)
        edges_count = 0
        
        for neighbor in graph[node]:
            # Count edges within component (avoid double counting)
            if neighbor in graph and neighbor > node:
                edges_count += 1
            
            if not visited[neighbor]:
                edges_count += dfs(neighbor, component)
        
        return edges_count
    
    # Find all connected components
    for i in range(n):
        if not visited[i]:
            component = []
            edges_in_component = 0
            
            # Count edges while finding component
            def dfs_with_edge_count(node: int) -> None:
                nonlocal edges_in_component
                visited[node] = True
                component.append(node)
                
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        dfs_with_edge_count(neighbor)
            
            dfs_with_edge_count(i)
            
            # Count edges in this component
            component_set = set(component)
            for node in component:
                for neighbor in graph[node]:
                    if neighbor in component_set and neighbor > node:
                        edges_in_component += 1
            
            # Check if complete
            component_size = len(component)
            expected_edges = component_size * (component_size - 1) // 2
            
            if edges_in_component == expected_edges:
                complete_components += 1
    
    return complete_components

# Test Cases
if __name__ == "__main__":
    test_cases = [
        (6, [[0,1],[0,2],[1,2],[3,4]], 3),
        (6, [[0,1],[0,2],[1,2],[3,4],[3,5]], 1),
        (4, [[0,1],[1,2],[2,3],[3,0]], 0),  # Cycle is not complete
        (3, [[0,1],[1,2],[0,2]], 1),        # Triangle is complete
        (1, [], 1),                         # Single vertex
        (5, [], 5),                         # All isolated vertices
        (4, [[0,1],[2,3]], 2),             # Two pairs
        (3, [[0,1]], 0)                     # One edge, not complete
    ]
    
    print("Testing main DFS approach:")
    for n, edges, expected in test_cases:
        result = countCompleteComponents(n, edges)
        print(f"countCompleteComponents({n}, {edges}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting BFS approach:")
    for n, edges, expected in test_cases:
        result = countCompleteComponentsBFS(n, edges)
        print(f"countCompleteComponentsBFS({n}, {edges}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting Union-Find approach:")
    for n, edges, expected in test_cases:
        result = countCompleteComponentsUnionFind(n, edges)
        print(f"countCompleteComponentsUnionFind({n}, {edges}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting optimized approach:")
    for n, edges, expected in test_cases:
        result = countCompleteComponentsOptimized(n, edges)
        print(f"countCompleteComponentsOptimized({n}, {edges}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    # Detailed analysis for first test case
    print("\nDetailed analysis for test case 1:")
    n, edges = 6, [[0,1],[0,2],[1,2],[3,4]]
    print(f"Graph: {n} vertices, edges: {edges}")
    
    # Component analysis
    print("Components found:")
    print("- [0,1,2]: 3 vertices, needs 3 edges, has 3 edges → Complete")
    print("- [3,4]: 2 vertices, needs 1 edge, has 1 edge → Complete") 
    print("- [5]: 1 vertex, needs 0 edges, has 0 edges → Complete")
    print("Total complete components: 3")

"""
Time and Space Complexity Analysis:

DFS Approach:
Time Complexity: O(n + m) - Visit each vertex and edge once
Space Complexity: O(n + m) - Adjacency list and recursion stack

BFS Approach:
Time Complexity: O(n + m) - Visit each vertex and edge once
Space Complexity: O(n + m) - Adjacency list and queue

Union-Find Approach:
Time Complexity: O(n + m * α(n)) - Union-Find operations
Space Complexity: O(n) - Parent array and component grouping

Optimized Approach:
Time Complexity: O(n + m) - Single pass through graph
Space Complexity: O(n + m) - Adjacency list storage

Key Insights:
1. A complete component with k vertices needs exactly k*(k-1)/2 edges
2. Must first find connected components, then check completeness
3. Can use DFS, BFS, or Union-Find for component detection
4. Edge counting within components is crucial for validation
5. Single vertices are trivially complete (0 edges needed)

Complete Graph Properties:
- Every pair of vertices is connected
- Maximum number of edges for given vertices
- Clique in graph theory terminology
- Symmetric and transitive relationships

Applications:
- Social network analysis (finding cliques)
- Bioinformatics (finding protein complexes)
- Recommendation systems
- Network reliability analysis

Topic: Graph Theory, Connected Components, DFS, BFS, Union-Find
"""
