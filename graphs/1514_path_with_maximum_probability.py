"""
LeetCode Question #1514: Path with Maximum Probability

Problem Statement:
You are given an undirected graph with `n` nodes (labeled from `0` to `n - 1`) and an array `edges` where `edges[i] = [a, b]` indicates that there is an edge between nodes `a` and `b`. You are also given a `succProb` array, where `succProb[i]` is the success probability of the edge `edges[i]`.

Given two nodes `start` and `end`, find the path with the maximum probability of success to go from `start` to `end` and return its success probability. If there is no path from `start` to `end`, return `0`.

The success probability of a path is the product of probabilities of the edges in the path.

Constraints:
- `2 <= n <= 10^4`
- `0 <= edges.length <= 2 * 10^4`
- `edges[i].length == 2`
- `0 <= a, b < n`
- `a != b`
- `0 <= succProb.length == edges.length <= 2 * 10^4`
- `0 <= succProb[i] <= 1`
- There is at most one edge between any two nodes.

Example:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25
Explanation: The path with the maximum probability is 0 -> 1 -> 2 with a probability of 0.5 * 0.5 = 0.25.

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.3
Explanation: The path with the maximum probability is 0 -> 2 with a probability of 0.3.

Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0
Explanation: There is no path from 0 to 2.
"""

from collections import defaultdict
import heapq

def maxProbability(n, edges, succProb, start, end):
    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for i, (a, b) in enumerate(edges):
        graph[a].append((b, succProb[i]))
        graph[b].append((a, succProb[i]))
    
    # Max-heap to store the probabilities (negative for max-heap behavior)
    max_heap = [(-1.0, start)]  # (-probability, node)
    visited = set()
    probabilities = [0.0] * n
    probabilities[start] = 1.0
    
    while max_heap:
        prob, node = heapq.heappop(max_heap)
        prob = -prob  # Convert back to positive probability
        
        if node in visited:
            continue
        visited.add(node)
        
        # If we reach the end node, return the probability
        if node == end:
            return prob
        
        # Update neighbors
        for neighbor, edge_prob in graph[node]:
            if neighbor not in visited:
                new_prob = prob * edge_prob
                if new_prob > probabilities[neighbor]:
                    probabilities[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
    
    return 0.0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.2]
    start = 0
    end = 2
    print(maxProbability(n, edges, succProb, start, end))  # Output: 0.25

    # Test Case 2
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.3]
    start = 0
    end = 2
    print(maxProbability(n, edges, succProb, start, end))  # Output: 0.3

    # Test Case 3
    n = 3
    edges = [[0,1]]
    succProb = [0.5]
    start = 0
    end = 2
    print(maxProbability(n, edges, succProb, start, end))  # Output: 0.0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph takes O(edges.length).
- The Dijkstra-like algorithm processes each node and edge once. Since there are at most `edges.length` edges and `n` nodes, the complexity is O(n + edges.length * log(n)) due to the heap operations.

Space Complexity:
- The graph uses O(edges.length) space.
- The heap can store up to O(n) elements.
- The probabilities array uses O(n) space.
- Total space complexity is O(n + edges.length).

Topic: Graphs
"""