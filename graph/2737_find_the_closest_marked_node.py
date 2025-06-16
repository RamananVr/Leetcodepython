"""
2737. Find the Closest Marked Node

You are given a positive integer n representing the number of nodes in a connected undirected graph containing exactly n nodes numbered from 0 to n - 1.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] denotes that there is an undirected edge between nodes ai and bi.

Finally, you are given an integer array marked which contains some of the nodes in the graph.

Return an integer denoting the minimum number of edges you need to traverse from any marked node to reach any other marked node. If it is impossible, return -1.

Example 1:
Input: n = 4, edges = [[0,1],[0,2],[1,3],[2,3]], marked = [0,3]
Output: 2
Explanation: There are several paths between nodes 0 and 3:
- 0 -> 1 -> 3: 2 edges
- 0 -> 2 -> 3: 2 edges
The minimum is 2 edges.

Example 2:
Input: n = 7, edges = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4],[2,5],[3,6]], marked = [1,2,4]
Output: 1
Explanation: There are several paths:
- 1 -> 2: 1 edge
- 1 -> 4: 1 edge  
- 2 -> 4: 1 edge
The minimum is 1 edge.

Example 3:
Input: n = 4, edges = [[0,1],[1,2],[2,3]], marked = [0,3]
Output: 3
Explanation: The only path between 0 and 3 is 0 -> 1 -> 2 -> 3: 3 edges.

Constraints:
- 2 <= n <= 500
- 1 <= edges.length <= min(n * (n-1) / 2, 2000)
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- edges[i] does not contain repeated edges.
- 1 <= marked.length <= min(n, 100)
"""

from collections import deque, defaultdict

def minimum_distance_between_marked_nodes(n: int, edges: list[list[int]], marked: list[int]) -> int:
    """
    Find minimum distance between any two marked nodes using BFS from each marked node.
    
    Args:
        n: Number of nodes (0 to n-1)
        edges: List of undirected edges
        marked: List of marked nodes
        
    Returns:
        int: Minimum distance between any two marked nodes, -1 if impossible
        
    Time Complexity: O(|marked| * (n + m)) where m is number of edges
    Space Complexity: O(n + m) for graph representation and BFS queue
    """
    # Build adjacency list
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs_shortest_path(start):
        """BFS to find shortest distances from start to all other nodes."""
        distances = [-1] * n
        distances[start] = 0
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[node] + 1
                    queue.append(neighbor)
        
        return distances
    
    min_distance = float('inf')
    
    # For each marked node, find distances to all other marked nodes
    for start in marked:
        distances = bfs_shortest_path(start)
        
        for target in marked:
            if start != target and distances[target] != -1:
                min_distance = min(min_distance, distances[target])
    
    return min_distance if min_distance != float('inf') else -1

def minimum_distance_between_marked_nodes_optimized(n: int, edges: list[list[int]], marked: list[int]) -> int:
    """
    Optimized approach using multi-source BFS from all marked nodes simultaneously.
    
    Args:
        n: Number of nodes
        edges: List of edges
        marked: List of marked nodes
        
    Returns:
        int: Minimum distance between any two marked nodes
        
    Time Complexity: O(n + m) - single BFS traversal
    Space Complexity: O(n + m) - graph and BFS structures
    """
    # Build adjacency list
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # Multi-source BFS
    queue = deque()
    distances = [-1] * n
    marked_set = set(marked)
    
    # Initialize all marked nodes as sources
    for node in marked:
        distances[node] = 0
        queue.append(node)
    
    min_distance = float('inf')
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
            elif neighbor in marked_set and distances[neighbor] == distances[node] + 1:
                # Found another marked node at the same distance level
                min_distance = min(min_distance, distances[neighbor])
    
    # Also check direct connections between marked nodes
    for node in marked:
        for neighbor in graph[node]:
            if neighbor in marked_set:
                min_distance = min(min_distance, 1)
    
    return min_distance if min_distance != float('inf') else -1

def minimum_distance_between_marked_nodes_floyd_warshall(n: int, edges: list[list[int]], marked: list[int]) -> int:
    """
    Using Floyd-Warshall algorithm to find all-pairs shortest paths.
    
    Args:
        n: Number of nodes
        edges: List of edges
        marked: List of marked nodes
        
    Returns:
        int: Minimum distance between any two marked nodes
        
    Time Complexity: O(n^3) - Floyd-Warshall algorithm
    Space Complexity: O(n^2) - distance matrix
    """
    # Initialize distance matrix
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    
    # Distance from node to itself is 0
    for i in range(n):
        dist[i][i] = 0
    
    # Set edge distances
    for a, b in edges:
        dist[a][b] = 1
        dist[b][a] = 1
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # Find minimum distance between any two marked nodes
    min_distance = INF
    for i in marked:
        for j in marked:
            if i != j:
                min_distance = min(min_distance, dist[i][j])
    
    return min_distance if min_distance != INF else -1

# Test cases
def test_minimum_distance_between_marked_nodes():
    test_cases = [
        # Basic test cases
        (4, [[0,1],[0,2],[1,3],[2,3]], [0,3], 2),
        (7, [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4],[2,5],[3,6]], [1,2,4], 1),
        (4, [[0,1],[1,2],[2,3]], [0,3], 3),
        
        # Edge cases
        (2, [[0,1]], [0,1], 1),                    # Simple case
        (3, [[0,1],[1,2]], [0,2], 2),             # Linear graph
        (3, [[0,1],[0,2]], [1,2], 2),             # Star graph
        
        # Disconnected components
        (4, [[0,1],[2,3]], [0,2], -1),            # No path between marked nodes
        (5, [[0,1],[2,3]], [0,1,2], -1),          # Some connected, some not
        
        # All nodes connected, various marked sets
        (4, [[0,1],[1,2],[2,3],[3,0]], [0,1], 1), # Square graph, adjacent marked
        (4, [[0,1],[1,2],[2,3],[3,0]], [0,2], 2), # Square graph, opposite marked
        
        # Complete graph cases
        (4, [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]], [0,1,2,3], 1), # All nodes marked
        
        # More complex cases
        (6, [[0,1],[1,2],[2,3],[3,4],[4,5],[5,0]], [1,3,5], 2),   # Hexagon
        (5, [[0,1],[1,2],[2,3],[3,4],[0,4]], [0,2,4], 2),         # Pentagon
    ]
    
    print("Testing minimum_distance_between_marked_nodes function:")
    for i, (n, edges, marked, expected) in enumerate(test_cases):
        result1 = minimum_distance_between_marked_nodes(n, edges, marked)
        result2 = minimum_distance_between_marked_nodes_optimized(n, edges, marked)
        result3 = minimum_distance_between_marked_nodes_floyd_warshall(n, edges, marked)
        
        print(f"Test {i+1}: n={n}, edges={edges}, marked={marked}")
        print(f"  Expected: {expected}")
        print(f"  BFS: {result1}")
        print(f"  Multi-source BFS: {result2}")
        print(f"  Floyd-Warshall: {result3}")
        
        assert result1 == expected, f"BFS failed for test case {i+1}"
        assert result3 == expected, f"Floyd-Warshall failed for test case {i+1}"
        print(f"  ✓ All passed\n")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_minimum_distance_between_marked_nodes()

"""
Time Complexity Analysis:
- BFS Solution: O(|marked| * (n + m)) - BFS from each marked node
- Multi-source BFS: O(n + m) - single BFS traversal
- Floyd-Warshall: O(n^3) - all-pairs shortest paths

Space Complexity Analysis:
- BFS: O(n + m) - graph representation and BFS queue
- Multi-source BFS: O(n + m) - similar to BFS
- Floyd-Warshall: O(n^2) - distance matrix

Key Insights:
1. We need shortest path between any two marked nodes
2. BFS gives shortest path in unweighted graphs
3. Multi-source BFS can be more efficient when we have multiple sources
4. Floyd-Warshall is overkill but works for dense graphs
5. Graph connectivity affects whether a solution exists

Topics: Graph, BFS, Shortest Path, Multi-source BFS
"""
