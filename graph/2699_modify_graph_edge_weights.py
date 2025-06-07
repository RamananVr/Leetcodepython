"""
2699. Modify Graph Edge Weights

PROBLEM STATEMENT:
You are given an undirected weighted connected graph containing n nodes labeled from 0 to n - 1, 
and an array edges where edges[i] = [ai, bi, wi] indicates that there is an edge between nodes 
ai and bi with weight wi.

Some edges have a weight of -1 (wi = -1), which means that the weight is not yet determined.

You are also given integers source, destination, and target.

Return the modified graph where you have assigned a positive weight to every edge with wi = -1 
such that the shortest distance from source to destination becomes equal to target. If there are 
multiple valid assignments, return any of them. If it is not possible to make the shortest 
distance equal to target, return an empty array.

EXAMPLES:
Example 1:
Input: n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5
Output: [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
Explanation: The shortest distance from 0 to 1 is 5.

Example 2:
Input: n = 3, edges = [[0,1,-1],[0,2,1]], source = 0, destination = 2, target = 5
Output: []
Explanation: The shortest distance from 0 to 2 is 1, and we cannot increase it to 5.

CONSTRAINTS:
- 1 <= n <= 100
- 1 <= edges.length <= n * (n - 1) / 2
- edges[i].length == 3
- 0 <= ai, bi < n
- wi = -1 or 1 <= wi <= 10^7
- ai != bi
- 0 <= source, destination < n
- source != destination
- 1 <= target <= 10^7
- The graph is connected.
"""

import heapq
from typing import List, Tuple, Dict

def modified_graph_edges(n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
    """
    Modify graph edge weights to achieve target shortest path distance.
    
    Args:
        n: Number of nodes
        edges: List of edges [a, b, weight] where weight can be -1
        source: Source node
        destination: Destination node  
        target: Target shortest path distance
    
    Returns:
        Modified edges with all weights positive, or empty list if impossible
    """
    
    def dijkstra(graph: Dict[int, List[Tuple[int, int]]], src: int, dest: int) -> int:
        """
        Find shortest path using Dijkstra's algorithm.
        
        Args:
            graph: Adjacency list representation
            src: Source node
            dest: Destination node
        
        Returns:
            Shortest distance, or float('inf') if no path
        """
        dist = [float('inf')] * n
        dist[src] = 0
        pq = [(0, src)]
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if u == dest:
                return d
            
            if d > dist[u]:
                continue
            
            for v, weight in graph.get(u, []):
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
        
        return dist[dest]
    
    def build_graph(edge_list: List[List[int]]) -> Dict[int, List[Tuple[int, int]]]:
        """Build adjacency list from edge list."""
        graph = {}
        for a, b, w in edge_list:
            if w > 0:  # Only include positive weights
                if a not in graph:
                    graph[a] = []
                if b not in graph:
                    graph[b] = []
                graph[a].append((b, w))
                graph[b].append((a, w))
        return graph
    
    # Separate unknown edges (-1) from known edges
    unknown_edges = []
    known_edges = []
    
    for i, (a, b, w) in enumerate(edges):
        if w == -1:
            unknown_edges.append(i)
        else:
            known_edges.append([a, b, w])
    
    # First, check shortest path with only known edges
    known_graph = build_graph(known_edges)
    known_dist = dijkstra(known_graph, source, destination)
    
    # If known edges already achieve target, set all unknown edges to 1
    if known_dist == target:
        result = edges[:]
        for i in unknown_edges:
            result[i][2] = 1
        return result
    
    # If known edges give distance > target, impossible
    if known_dist < target:
        return []
    
    # Try to use unknown edges to achieve target distance
    result = edges[:]
    
    # Set all unknown edges to 1 initially
    for i in unknown_edges:
        result[i][2] = 1
    
    # Check if setting all to 1 gives distance <= target
    temp_graph = build_graph(result)
    temp_dist = dijkstra(temp_graph, source, destination)
    
    # If still > target with all 1s, impossible
    if temp_dist > target:
        return []
    
    # If exactly target, we're done
    if temp_dist == target:
        return result
    
    # temp_dist < target, so we need to increase some edge weights
    # Binary search approach: try to find the right combination
    
    # Try adjusting edges one by one
    for i in unknown_edges:
        a, b, _ = result[i]
        
        # Binary search for the right weight for this edge
        left, right = 1, target
        best_weight = 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Temporarily set this edge weight
            result[i][2] = mid
            
            # Check shortest path
            temp_graph = build_graph(result)
            temp_dist = dijkstra(temp_graph, source, destination)
            
            if temp_dist == target:
                return result
            elif temp_dist < target:
                best_weight = mid
                left = mid + 1
            else:
                right = mid - 1
        
        # Set to best weight found
        result[i][2] = best_weight
        
        # Check if we've achieved target
        temp_graph = build_graph(result)
        if dijkstra(temp_graph, source, destination) == target:
            return result
    
    return []

def modified_graph_edges_advanced(n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
    """
    Advanced approach using incremental edge modification.
    
    Args:
        n: Number of nodes
        edges: List of edges
        source: Source node
        destination: Destination node
        target: Target distance
    
    Returns:
        Modified edges or empty list if impossible
    """
    
    def dijkstra_with_path(graph, src, dest):
        """Dijkstra with path tracking."""
        dist = [float('inf')] * n
        parent = [-1] * n
        dist[src] = 0
        pq = [(0, src)]
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if u == dest:
                break
                
            if d > dist[u]:
                continue
            
            for v, weight, edge_idx in graph.get(u, []):
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    parent[v] = u
                    heapq.heappush(pq, (dist[v], v))
        
        # Reconstruct path
        path = []
        curr = dest
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
        path.reverse()
        
        return dist[dest], path
    
    # Build graph with edge indices
    def build_graph_with_indices(edge_list):
        graph = {}
        for i, (a, b, w) in enumerate(edge_list):
            if w > 0:
                if a not in graph:
                    graph[a] = []
                if b not in graph:
                    graph[b] = []
                graph[a].append((b, w, i))
                graph[b].append((a, w, i))
        return graph
    
    result = edges[:]
    
    # Set all -1 edges to 1 initially
    for i in range(len(result)):
        if result[i][2] == -1:
            result[i][2] = 1
    
    graph = build_graph_with_indices(result)
    current_dist, path = dijkstra_with_path(graph, source, destination)
    
    if current_dist > target:
        return []
    
    if current_dist == target:
        return result
    
    # current_dist < target, need to increase
    # Find unknown edges on the shortest path and increase them
    unknown_on_path = []
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        # Find edge between u and v
        for edge_idx, (a, b, w) in enumerate(edges):
            if ((a == u and b == v) or (a == v and b == u)) and edges[edge_idx][2] == -1:
                unknown_on_path.append(edge_idx)
                break
    
    if not unknown_on_path:
        return []
    
    # Increase weight of first unknown edge on path
    edge_to_modify = unknown_on_path[0]
    needed_increase = target - current_dist
    result[edge_to_modify][2] = 1 + needed_increase
    
    # Verify the result
    final_graph = build_graph_with_indices(result)
    final_dist, _ = dijkstra_with_path(final_graph, source, destination)
    
    if final_dist == target:
        return result
    else:
        return []

def test_modified_graph_edges():
    """Test the graph edge modification implementation."""
    
    # Test 1: Example 1
    n1 = 5
    edges1 = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]
    source1, destination1, target1 = 0, 1, 5
    result1 = modified_graph_edges(n1, edges1, source1, destination1, target1)
    
    # Verify the result gives correct shortest path
    if result1:
        # Build graph and check distance
        graph = {}
        for a, b, w in result1:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append((b, w))
            graph[b].append((a, w))
        
        # Simple BFS/Dijkstra to verify
        dist = [float('inf')] * n1
        dist[source1] = 0
        pq = [(0, source1)]
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, weight in graph.get(u, []):
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
        
        assert dist[destination1] == target1, f"Expected {target1}, got {dist[destination1]}"
    
    # Test 2: Example 2 (impossible case)
    n2 = 3
    edges2 = [[0,1,-1],[0,2,1]]
    source2, destination2, target2 = 0, 2, 5
    result2 = modified_graph_edges(n2, edges2, source2, destination2, target2)
    assert result2 == [], "Should return empty array for impossible case"
    
    # Test 3: Simple case
    n3 = 3
    edges3 = [[0,1,-1],[1,2,2]]
    source3, destination3, target3 = 0, 2, 5
    result3 = modified_graph_edges(n3, edges3, source3, destination3, target3)
    
    if result3:
        # Edge (0,1) should be set to 3 to make total distance 5
        assert result3[0][2] == 3
    
    # Test 4: No unknown edges
    n4 = 3
    edges4 = [[0,1,2],[1,2,3]]
    source4, destination4, target4 = 0, 2, 5
    result4 = modified_graph_edges(n4, edges4, source4, destination4, target4)
    assert result4 == edges4, "Should return original edges when target matches"
    
    print("All test cases passed!")

def demonstrate_algorithm():
    """Demonstrate the algorithm with detailed steps."""
    
    print("Graph Edge Weight Modification Algorithm")
    print("=" * 50)
    
    # Example case
    n = 5
    edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]
    source, destination, target = 0, 1, 5
    
    print(f"Input:")
    print(f"  Nodes: {n}")
    print(f"  Edges: {edges}")
    print(f"  Source: {source}, Destination: {destination}")
    print(f"  Target distance: {target}")
    
    result = modified_graph_edges(n, edges, source, destination, target)
    
    print(f"\nResult: {result}")
    
    if result:
        print("\nModifications made:")
        for i, (orig, new) in enumerate(zip(edges, result)):
            if orig[2] != new[2]:
                print(f"  Edge ({orig[0]}, {orig[1]}): {orig[2]} -> {new[2]}")
    else:
        print("No valid modification possible")

if __name__ == "__main__":
    test_modified_graph_edges()
    demonstrate_algorithm()

"""
COMPLEXITY ANALYSIS:
- Time Complexity: O(E * (V + E) * log V) where V is number of vertices, E is number of edges
  - For each unknown edge, we may run Dijkstra's algorithm (V + E) log V
  - In worst case, we try all unknown edges
- Space Complexity: O(V + E) for graph representation and Dijkstra's data structures

TOPICS: Graph Theory, Shortest Path, Dijkstra's Algorithm, Binary Search, Greedy

KEY INSIGHTS:
1. Need to balance between making shortest path achievable and not exceeding target
2. Binary search can help find optimal edge weights efficiently
3. Setting all unknown edges to 1 initially gives lower bound on shortest path
4. If known edges already exceed target, modification is impossible
5. Incremental modification along shortest path can be more efficient than trying all combinations
"""
