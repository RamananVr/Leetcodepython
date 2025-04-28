"""
LeetCode Problem #2065: Maximum Path Quality of a Graph

Problem Statement:
You are given an undirected graph with `n` nodes numbered from `0` to `n - 1` (inclusive). 
You are also given a 0-indexed integer array `values` where `values[i]` is the value of the `i-th` node. 
You are further given a 2D integer array `edges`, where `edges[j] = [u_j, v_j, time_j]` indicates that 
there is an undirected edge between the nodes `u_j` and `v_j`, and it takes `time_j` seconds to travel between them. 
Finally, you are given an integer `maxTime`.

A valid path in the graph is any path that starts at node `0` and ends at node `0` and takes at most `maxTime` seconds 
to complete. You may visit the same node multiple times. The quality of a valid path is the sum of the values of the 
unique nodes visited in the path (each node is counted only once, even if visited multiple times).

Return the maximum quality of a valid path.

Constraints:
- `n == values.length`
- `1 <= n <= 1000`
- `0 <= values[i] <= 10^8`
- `0 <= edges.length <= 2000`
- `edges[j].length == 3`
- `0 <= u_j, v_j < n`
- `1 <= time_j <= 10^6`
- `1 <= maxTime <= 10^9`

"""

from collections import defaultdict

def maximalPathQuality(values, edges, maxTime):
    def dfs(node, time_left, visited, current_quality):
        nonlocal max_quality
        if time_left < 0:
            return
        
        # Add the value of the current node if it's the first visit
        if visited[node] == 0:
            current_quality += values[node]
        
        # Mark the node as visited
        visited[node] += 1
        
        # If we return to node 0, update the maximum quality
        if node == 0:
            max_quality = max(max_quality, current_quality)
        
        # Explore neighbors
        for neighbor, travel_time in graph[node]:
            dfs(neighbor, time_left - travel_time, visited, current_quality)
        
        # Backtrack
        visited[node] -= 1
        if visited[node] == 0:
            current_quality -= values[node]
    
    # Build the graph
    graph = defaultdict(list)
    for u, v, time in edges:
        graph[u].append((v, time))
        graph[v].append((u, time))
    
    # Initialize variables
    max_quality = 0
    visited = [0] * len(values)
    
    # Start DFS from node 0
    dfs(0, maxTime, visited, 0)
    
    return max_quality

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    values = [0, 32, 10, 43]
    edges = [[0, 1, 10], [1, 2, 15], [0, 3, 10]]
    maxTime = 49
    print(maximalPathQuality(values, edges, maxTime))  # Output: 75

    # Test Case 2
    values = [5, 10, 15, 20]
    edges = [[0, 1, 10], [1, 2, 10], [0, 3, 10]]
    maxTime = 30
    print(maximalPathQuality(values, edges, maxTime))  # Output: 25

    # Test Case 3
    values = [1, 2, 3]
    edges = [[0, 1, 10], [1, 2, 10], [0, 2, 1]]
    maxTime = 10
    print(maximalPathQuality(values, edges, maxTime))  # Output: 4

"""
Time Complexity:
- Let `n` be the number of nodes and `e` be the number of edges.
- In the worst case, the DFS explores all possible paths in the graph. 
  Since there are `n` nodes and each node can be visited multiple times, the time complexity is O(n * 2^n).
- Building the graph takes O(e), where `e` is the number of edges.

Space Complexity:
- The space complexity is O(n + e) for storing the graph and O(n) for the recursion stack and visited array.

Topic: Graph, Depth-First Search (DFS), Backtracking
"""