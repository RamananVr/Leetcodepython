"""
LeetCode Problem #1697: Checking Existence of Edge Length Limited Paths

Problem Statement:
An undirected graph of `n` nodes (0-indexed) is given, represented by an edge list where `edges[i] = [u, v, dis]` denotes a bidirectional edge between nodes `u` and `v` with distance `dis`. You are also given a query list `queries[j] = [p, q, limit]`, where `p` and `q` are nodes and `limit` is an integer.

Return a boolean array `answer` where `answer[j]` is `true` if there is a path between `p` and `q` such that every edge on the path has a distance strictly less than `limit[j]`, and `false` otherwise.

Constraints:
- `2 <= n <= 10^5`
- `1 <= edges.length, queries.length <= 10^5`
- `edges[i].length == 3`
- `queries[j].length == 3`
- `0 <= u, v, p, q <= n - 1`
- `u != v`
- `p != q`
- `1 <= dis, limit <= 10^9`
- There may be multiple edges between two nodes.

"""

from typing import List

class Solution:
    def distanceLimitedPathsExist(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Sort edges by distance
        edges.sort(key=lambda x: x[2])
        
        # Add indices to queries and sort by limit
        queries = [(p, q, limit, i) for i, (p, q, limit) in enumerate(queries)]
        queries.sort(key=lambda x: x[2])
        
        # Union-Find (Disjoint Set Union) implementation
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
        
        # Process queries
        answer = [False] * len(queries)
        edge_index = 0
        
        for p, q, limit, query_index in queries:
            # Add all edges with distance < limit to the union-find structure
            while edge_index < len(edges) and edges[edge_index][2] < limit:
                u, v, dis = edges[edge_index]
                union(u, v)
                edge_index += 1
            
            # Check if p and q are connected
            if find(p) == find(q):
                answer[query_index] = True
        
        return answer

# Example Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    n = 3
    edges = [[0, 1, 4], [1, 2, 3], [0, 2, 5]]
    queries = [[0, 2, 6], [0, 2, 3]]
    print(sol.distanceLimitedPathsExist(n, edges, queries))  # Output: [True, False]
    
    # Test Case 2
    n = 5
    edges = [[0, 1, 2], [0, 2, 4], [1, 2, 1], [3, 4, 3]]
    queries = [[0, 4, 5], [0, 1, 2], [2, 3, 3]]
    print(sol.distanceLimitedPathsExist(n, edges, queries))  # Output: [False, True, False]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the edges: O(E * log(E)), where E is the number of edges.
- Sorting the queries: O(Q * log(Q)), where Q is the number of queries.
- Union-Find operations: O(α(N)) per operation, where α is the inverse Ackermann function (nearly constant).
  In the worst case, we process all edges and queries, so the total complexity is O(E + Q) for union-find operations.
- Overall: O(E * log(E) + Q * log(Q) + E + Q) ≈ O(E * log(E) + Q * log(Q)).

Space Complexity:
- Union-Find parent and rank arrays: O(N), where N is the number of nodes.
- Storing the sorted edges and queries: O(E + Q).
- Overall: O(N + E + Q).

Topic: Union-Find (Disjoint Set Union)
"""