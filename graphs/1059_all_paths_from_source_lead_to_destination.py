"""
LeetCode Question #1059: All Paths from Source Lead to Destination

Problem Statement:
Given a directed graph, you need to determine if all paths starting from the source node lead to the destination node. 
The graph is represented by its edges, where edges[i] = [u, v] indicates a direct edge from node u to node v.

The graph has the following properties:
1. The number of nodes in the graph is between 1 and 10000.
2. Each node has at most 100 edges.
3. The graph may contain self-loops and duplicate edges.

Constraints:
- The source and destination nodes are distinct.
- The graph may not be connected.

Your task is to return true if and only if all paths from the source lead to the destination.

Example 1:
Input: n = 3, edges = [[0,1],[0,2],[1,2]], source = 0, destination = 2
Output: true

Example 2:
Input: n = 4, edges = [[0,1],[0,3],[1,2],[2,1]], source = 0, destination = 3
Output: false

Example 3:
Input: n = 2, edges = [[0,1],[1,1]], source = 0, destination = 1
Output: false

Follow-up:
Can you solve this problem using DFS or BFS?
"""

from collections import defaultdict

def leadsToDestination(n, edges, source, destination):
    """
    Determines if all paths from the source node lead to the destination node.

    :param n: int - Number of nodes in the graph
    :param edges: List[List[int]] - List of directed edges
    :param source: int - Source node
    :param destination: int - Destination node
    :return: bool - True if all paths from source lead to destination, False otherwise
    """
    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    # Helper function for DFS
    def dfs(node, visited):
        # If we reach a node that is not the destination and has no outgoing edges, return False
        if not graph[node] and node != destination:
            return False
        
        # If we reach the destination, return True
        if node == destination:
            return True
        
        # If the node is already visited, it means we are in a cycle
        if node in visited:
            return False
        
        # Mark the node as visited
        visited.add(node)
        
        # Explore all neighbors
        for neighbor in graph[node]:
            if not dfs(neighbor, visited):
                return False
        
        # Unmark the node after exploring all paths
        visited.remove(node)
        
        return True
    
    # Start DFS from the source node
    return dfs(source, set())

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 3
    edges1 = [[0, 1], [0, 2], [1, 2]]
    source1 = 0
    destination1 = 2
    print(leadsToDestination(n1, edges1, source1, destination1))  # Output: True

    # Test Case 2
    n2 = 4
    edges2 = [[0, 1], [0, 3], [1, 2], [2, 1]]
    source2 = 0
    destination2 = 3
    print(leadsToDestination(n2, edges2, source2, destination2))  # Output: False

    # Test Case 3
    n3 = 2
    edges3 = [[0, 1], [1, 1]]
    source3 = 0
    destination3 = 1
    print(leadsToDestination(n3, edges3, source3, destination3))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses DFS to explore the graph. In the worst case, we visit each node and edge once.
- Let V be the number of nodes and E be the number of edges. The time complexity is O(V + E).

Space Complexity:
- The space complexity is determined by the recursion stack and the visited set.
- The recursion stack can go as deep as the number of nodes, and the visited set can store up to V nodes.
- Therefore, the space complexity is O(V).

Topic: Graphs
"""