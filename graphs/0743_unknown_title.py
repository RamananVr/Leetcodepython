"""
LeetCode Problem #743: Network Delay Time

Problem Statement:
You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (u, v, w)`, where `u` is the source node, `v` is the target node, and `w` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return the time it takes for all the `n` nodes to receive the signal. If it is impossible for all the nodes to receive the signal, return `-1`.

Constraints:
- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`
- `1 <= u, v <= n`
- `u != v`
- `0 <= w <= 100`
- All the edges `times[i]` are directed.

"""

# Solution
import heapq
from collections import defaultdict

def networkDelayTime(times, n, k):
    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    # Min-heap to store (time, node)
    min_heap = [(0, k)]  # (current_time, starting_node)
    visited = set()
    max_time = 0
    
    while min_heap:
        time, node = heapq.heappop(min_heap)
        
        # Skip if the node is already visited
        if node in visited:
            continue
        
        # Mark the node as visited
        visited.add(node)
        max_time = max(max_time, time)
        
        # Explore neighbors
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (time + weight, neighbor))
    
    # Check if all nodes are visited
    return max_time if len(visited) == n else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    times1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n1 = 4
    k1 = 2
    print(networkDelayTime(times1, n1, k1))  # Expected Output: 2

    # Test Case 2
    times2 = [[1, 2, 1]]
    n2 = 2
    k2 = 1
    print(networkDelayTime(times2, n2, k2))  # Expected Output: 1

    # Test Case 3
    times3 = [[1, 2, 1]]
    n3 = 2
    k3 = 2
    print(networkDelayTime(times3, n3, k3))  # Expected Output: -1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph takes O(times.length).
- Dijkstra's algorithm runs in O((V + E) * log(V)), where V is the number of nodes (n) and E is the number of edges (times.length).
- Overall time complexity: O(times.length + (n + times.length) * log(n)).

Space Complexity:
- The graph representation takes O(times.length).
- The min-heap can store up to O(n) elements.
- The visited set takes O(n) space.
- Overall space complexity: O(times.length + n).

Topic: Graphs
"""