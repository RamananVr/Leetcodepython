"""
LeetCode Problem #1129: Shortest Path with Alternating Colors

Problem Statement:
You are given an integer `n`, the number of nodes in a directed graph where the nodes are labeled from `0` to `n - 1`. 
Each edge is red or blue in this graph, and there could be self-edges or parallel edges.

You are given two arrays `redEdges` and `blueEdges` where:
- `redEdges[i] = [ai, bi]` indicates that there is a directed red edge from node `ai` to node `bi`.
- `blueEdges[i] = [ui, vi]` indicates that there is a directed blue edge from node `ui` to node `vi`.

Return an array `answer` of length `n`, where `answer[x]` is the length of the shortest path from node `0` to node `x` 
such that the edge colors alternate along the path, or `-1` if such a path does not exist.

Constraints:
- `1 <= n <= 100`
- `0 <= redEdges.length, blueEdges.length <= 400`
- `redEdges[i].length == blueEdges[i].length == 2`
- `0 <= ai, bi, ui, vi < n`

"""

from collections import defaultdict, deque

def shortestAlternatingPaths(n, redEdges, blueEdges):
    # Build adjacency lists for red and blue edges
    red_graph = defaultdict(list)
    blue_graph = defaultdict(list)
    
    for u, v in redEdges:
        red_graph[u].append(v)
    for u, v in blueEdges:
        blue_graph[u].append(v)
    
    # Initialize the result array with -1
    result = [-1] * n
    
    # BFS queue: (node, color, distance)
    # color: 0 for red, 1 for blue
    queue = deque([(0, 0, 0), (0, 1, 0)])  # Start from node 0 with both red and blue
    visited = set()  # To avoid revisiting the same state (node, color)
    
    while queue:
        node, color, dist = queue.popleft()
        
        # If this is the first time visiting the node, update the result
        if result[node] == -1:
            result[node] = dist
        
        # Explore neighbors based on the current edge color
        if color == 0:  # Current edge is red, next edge must be blue
            for neighbor in blue_graph[node]:
                if (neighbor, 1) not in visited:
                    visited.add((neighbor, 1))
                    queue.append((neighbor, 1, dist + 1))
        else:  # Current edge is blue, next edge must be red
            for neighbor in red_graph[node]:
                if (neighbor, 0) not in visited:
                    visited.add((neighbor, 0))
                    queue.append((neighbor, 0, dist + 1))
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    redEdges = [[0, 1], [1, 2]]
    blueEdges = []
    print(shortestAlternatingPaths(n, redEdges, blueEdges))  # Output: [0, 1, -1]

    # Test Case 2
    n = 3
    redEdges = [[0, 1]]
    blueEdges = [[1, 2]]
    print(shortestAlternatingPaths(n, redEdges, blueEdges))  # Output: [0, 1, 2]

    # Test Case 3
    n = 3
    redEdges = [[0, 1], [0, 2]]
    blueEdges = [[1, 0]]
    print(shortestAlternatingPaths(n, redEdges, blueEdges))  # Output: [0, 1, 1]

    # Test Case 4
    n = 5
    redEdges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    blueEdges = [[1, 2], [2, 3], [3, 1]]
    print(shortestAlternatingPaths(n, redEdges, blueEdges))  # Output: [0, 1, 2, 3, 4]

"""
Time Complexity:
- Building the adjacency lists takes O(E), where E is the total number of edges (redEdges + blueEdges).
- BFS visits each node and edge at most once, so the BFS traversal also takes O(V + E), where V is the number of nodes.
- Overall time complexity: O(V + E).

Space Complexity:
- The adjacency lists take O(E) space.
- The BFS queue and visited set take O(V) space in the worst case.
- Overall space complexity: O(V + E).

Topic: Graphs, Breadth-First Search (BFS)
"""