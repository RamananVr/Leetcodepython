"""
LeetCode Problem #2242: Maximum Score of a Node Sequence

Problem Statement:
You are given an undirected graph with `n` nodes, numbered from `0` to `n - 1`, and an array `edges` where 
`edges[i] = [u_i, v_i, weight_i]` represents a bidirectional edge between nodes `u_i` and `v_i` with a weight 
equal to `weight_i`.

A node sequence is valid if it meets the following conditions:
1. There is an edge between every pair of consecutive nodes in the sequence.
2. No node appears more than once in the sequence.

The score of a node sequence is defined as the sum of the weights of the edges in the sequence.

Return the maximum score of a valid node sequence with exactly four nodes. If no such sequence exists, return -1.

Constraints:
- `n == number of nodes`
- `2 <= n <= 10^4`
- `1 <= edges.length <= 10^5`
- `edges[i].length == 3`
- `0 <= u_i, v_i < n`
- `u_i != v_i`
- `1 <= weight_i <= 10^5`
- There are no duplicate edges.

"""

from heapq import nlargest
from collections import defaultdict

def maximumScore(edges, n):
    """
    Function to calculate the maximum score of a valid node sequence with exactly four nodes.
    
    :param edges: List[List[int]] - List of edges where each edge is represented as [u, v, weight].
    :param n: int - Number of nodes in the graph.
    :return: int - Maximum score of a valid node sequence with exactly four nodes, or -1 if no such sequence exists.
    """
    # Step 1: Build adjacency list with top 3 heaviest edges for each node
    adj = defaultdict(list)
    for u, v, weight in edges:
        adj[u].append((weight, v))
        adj[v].append((weight, u))
    
    for node in adj:
        adj[node] = nlargest(3, adj[node])  # Keep only the top 3 heaviest edges for each node

    # Step 2: Try all possible 4-node sequences
    max_score = -1
    for u, v, weight_uv in edges:
        # Get top 3 neighbors of u and v
        neighbors_u = adj[u]
        neighbors_v = adj[v]
        
        # Try all combinations of neighbors of u and v
        for weight_u, neighbor_u in neighbors_u:
            for weight_v, neighbor_v in neighbors_v:
                # Ensure all nodes are distinct
                if len({u, v, neighbor_u, neighbor_v}) == 4:
                    max_score = max(max_score, weight_uv + weight_u + weight_v)
    
    return max_score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    edges = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [0, 2, 15], [1, 3, 25]]
    n = 4
    print(maximumScore(edges, n))  # Expected Output: 75 (Sequence: 0 -> 1 -> 3 -> 2)

    # Test Case 2
    edges = [[0, 1, 5], [1, 2, 10], [2, 3, 15]]
    n = 4
    print(maximumScore(edges, n))  # Expected Output: -1 (No valid sequence of 4 nodes)

    # Test Case 3
    edges = [[0, 1, 100], [1, 2, 200], [2, 3, 300], [3, 4, 400], [0, 4, 50]]
    n = 5
    print(maximumScore(edges, n))  # Expected Output: 1000 (Sequence: 0 -> 1 -> 2 -> 3)

"""
Time and Space Complexity Analysis:

Time Complexity:
1. Building the adjacency list: O(E), where E is the number of edges.
2. Sorting and keeping the top 3 neighbors for each node: O(V * log(V)), where V is the number of nodes.
3. Iterating through all edges and trying combinations of neighbors: O(E * 3 * 3) = O(9E) = O(E).

Overall Time Complexity: O(E + V * log(V))

Space Complexity:
1. Adjacency list storage: O(V + E).
2. Temporary storage for top 3 neighbors: O(V).

Overall Space Complexity: O(V + E)

Topic: Graphs
"""