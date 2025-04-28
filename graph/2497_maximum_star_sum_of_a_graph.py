"""
LeetCode Question #2497: Maximum Star Sum of a Graph

Problem Statement:
You are given a graph represented as an integer array `vals` and a 2D integer array `edges`. 
The graph has `n` nodes numbered from `0` to `n - 1`. The `vals[i]` represents the value of the `i-th` node.

You are also given an integer `k`. A star graph is a subset of the graph consisting of a center node and 
at most `k` neighbors. The star sum is the sum of the values of the center node and the values of its neighbors.

Return the maximum star sum of the graph.

Constraints:
- `n == vals.length`
- `1 <= n <= 10^5`
- `-10^4 <= vals[i] <= 10^4`
- `0 <= edges.length <= min(10^5, n * (n - 1) / 2)`
- `edges[i].length == 2`
- `0 <= edges[i][0], edges[i][1] < n`
- `edges[i][0] != edges[i][1]`
- `0 <= k <= n`
"""

# Solution
from collections import defaultdict

def maxStarSum(vals, edges, k):
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(vals[v])
        graph[v].append(vals[u])
    
    max_sum = float('-inf')
    
    for node in range(len(vals)):
        # Sort neighbors by value in descending order
        neighbors = sorted(graph[node], reverse=True)
        # Take up to k neighbors with the highest values
        max_neighbors_sum = sum(neighbors[:k])
        # Calculate star sum for the current node
        star_sum = vals[node] + max_neighbors_sum
        # Update the maximum star sum
        max_sum = max(max_sum, star_sum)
    
    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    vals = [1, 2, 3, 4]
    edges = [[0, 1], [0, 2], [0, 3]]
    k = 2
    print(maxStarSum(vals, edges, k))  # Expected Output: 10

    # Test Case 2
    vals = [-5, -2, 0, 1, 2]
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    k = 1
    print(maxStarSum(vals, edges, k))  # Expected Output: 3

    # Test Case 3
    vals = [10, -10, 20, -20, 30]
    edges = [[0, 1], [0, 2], [1, 3], [2, 4]]
    k = 3
    print(maxStarSum(vals, edges, k))  # Expected Output: 60

# Time and Space Complexity Analysis
"""
Time Complexity:
- Building the adjacency list takes O(edges.length).
- Sorting the neighbors for each node takes O(n * k log k) in the worst case, where k is the number of neighbors.
- Overall, the time complexity is O(edges.length + n * k log k).

Space Complexity:
- The adjacency list requires O(edges.length) space.
- Sorting neighbors temporarily requires O(k) space for each node.
- Overall, the space complexity is O(edges.length + k).

Topic: Graph
"""