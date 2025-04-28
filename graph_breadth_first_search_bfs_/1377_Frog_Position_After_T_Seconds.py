"""
LeetCode Problem #1377: Frog Position After T Seconds

Problem Statement:
Given an undirected tree consisting of `n` vertices numbered from `1` to `n`, where the tree is represented as a list of `edges` (each edge is a pair `[u, v]` representing a bidirectional connection between vertices `u` and `v`), and a frog starting at vertex `1`. At each second, the frog jumps to one of its adjacent vertices with equal probability. If the frog cannot jump to any other vertex, it will stay in its current position.

You are given the integer `t` (the number of seconds) and the integer `target` (the vertex the frog wants to reach). Return the probability that the frog is on the `target` vertex after `t` seconds.

Constraints:
- `1 <= n <= 100`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `1 <= u, v <= n`
- `1 <= t <= 50`
- `1 <= target <= n`
- Answers within `10^-5` of the actual value will be accepted as correct.
"""

from collections import defaultdict, deque

def frogPosition(n, edges, t, target):
    # Build the adjacency list for the tree
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS to calculate probabilities
    queue = deque([(1, 1.0, 0)])  # (current_node, probability, time_elapsed)
    visited = set()
    visited.add(1)
    
    while queue:
        node, prob, time = queue.popleft()
        
        # If we reach the target and time matches, return the probability
        if node == target:
            # If the frog cannot jump further, return the probability
            if time == t or len([neighbor for neighbor in graph[node] if neighbor not in visited]) == 0:
                return prob
            else:
                return 0.0
        
        # If time exceeds t, stop processing
        if time >= t:
            continue
        
        # Count unvisited neighbors
        unvisited_neighbors = [neighbor for neighbor in graph[node] if neighbor not in visited]
        num_unvisited = len(unvisited_neighbors)
        
        # If there are no unvisited neighbors, the frog stays at the current node
        if num_unvisited == 0:
            queue.append((node, prob, time + 1))
        else:
            # Distribute probability among unvisited neighbors
            for neighbor in unvisited_neighbors:
                visited.add(neighbor)
                queue.append((neighbor, prob / num_unvisited, time + 1))
    
    return 0.0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 7
    edges = [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]]
    t = 2
    target = 4
    print(frogPosition(n, edges, t, target))  # Expected Output: 0.16666666666666666

    # Test Case 2
    n = 7
    edges = [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]]
    t = 1
    target = 7
    print(frogPosition(n, edges, t, target))  # Expected Output: 0.3333333333333333

    # Test Case 3
    n = 3
    edges = [[1, 2], [1, 3]]
    t = 3
    target = 2
    print(frogPosition(n, edges, t, target))  # Expected Output: 0.0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the adjacency list takes O(n).
- BFS traversal processes each node and edge once, resulting in O(n + edges) = O(n).
Thus, the overall time complexity is O(n).

Space Complexity:
- The adjacency list requires O(n) space.
- The queue used in BFS can store up to O(n) nodes.
- The visited set also requires O(n) space.
Thus, the overall space complexity is O(n).

Topic: Graph, Breadth-First Search (BFS)
"""