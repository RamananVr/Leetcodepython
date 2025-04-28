"""
LeetCode Problem #1489: Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

Problem Statement:
Given a weighted undirected connected graph with `n` vertices numbered from `0` to `n-1`, and an array `edges` where `edges[i] = [ui, vi, weighti]` represents a bidirectional and weighted edge between nodes `ui` and `vi`. A minimum spanning tree (MST) is a subset of the edges of the graph that connects all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the MST of the graph. An edge is critical if removing it will make the MST weight increase or make it impossible to form an MST. An edge is pseudo-critical if it can appear in some MSTs but is not critical.

Return a list `answer` of size 2 where:
- `answer[0]` is a list of all critical edges.
- `answer[1]` is a list of all pseudo-critical edges.

Constraints:
- `2 <= n <= 100`
- `1 <= edges.length <= min(200, n * (n - 1) / 2)`
- `edges[i].length == 3`
- `0 <= ui < vi < n`
- `1 <= weighti <= 1000`
- All pairs `(ui, vi)` are distinct.

Example:
Input: n = 5, edges = [[0,1,1],[0,2,1],[1,2,1],[1,3,1],[2,3,1],[3,4,1]]
Output: [[0,1],[2,3,4]]
"""

from typing import List

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Add index to edges for tracking
        edges = [(u, v, w, i) for i, (u, v, w) in enumerate(edges)]
        edges.sort(key=lambda x: x[2])  # Sort edges by weight

        # Helper function to find MST weight using Union-Find
        def find_mst_weight(n, edges, include=None, exclude=None):
            parent = list(range(n))
            rank = [0] * n

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            def union(x, y):
                rootX, rootY = find(x), find(y)
                if rootX != rootY:
                    if rank[rootX] > rank[rootY]:
                        parent[rootY] = rootX
                    elif rank[rootX] < rank[rootY]:
                        parent[rootX] = rootY
                    else:
                        parent[rootY] = rootX
                        rank[rootX] += 1
                    return True
                return False

            mst_weight = 0
            edges_used = 0

            # Include the "include" edge first if provided
            if include is not None:
                u, v, w, _ = include
                if union(u, v):
                    mst_weight += w
                    edges_used += 1

            # Process all edges
            for u, v, w, idx in edges:
                if idx == exclude:  # Skip the "exclude" edge
                    continue
                if union(u, v):
                    mst_weight += w
                    edges_used += 1

            # Check if we used exactly n-1 edges (valid MST)
            return mst_weight if edges_used == n - 1 else float('inf')

        # Find the weight of the original MST
        original_mst_weight = find_mst_weight(n, edges)

        critical = []
        pseudo_critical = []

        for u, v, w, idx in edges:
            # Check if the edge is critical
            if find_mst_weight(n, edges, exclude=idx) > original_mst_weight:
                critical.append(idx)
            # Check if the edge is pseudo-critical
            elif find_mst_weight(n, edges, include=(u, v, w, idx)) == original_mst_weight:
                pseudo_critical.append(idx)

        return [critical, pseudo_critical]

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    n1 = 5
    edges1 = [[0,1,1],[0,2,1],[1,2,1],[1,3,1],[2,3,1],[3,4,1]]
    print(solution.findCriticalAndPseudoCriticalEdges(n1, edges1))  # Output: [[0,1],[2,3,4]]

    # Test Case 2
    n2 = 4
    edges2 = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
    print(solution.findCriticalAndPseudoCriticalEdges(n2, edges2))  # Output: [[], [0,1,2,3]]

    # Test Case 3
    n3 = 6
    edges3 = [[0,1,2],[0,2,5],[2,3,5],[1,4,4],[2,5,5],[4,5,2]]
    print(solution.findCriticalAndPseudoCriticalEdges(n3, edges3))  # Output: [[0,3,5],[1,2,4]]

"""
Time Complexity:
- Sorting the edges takes O(E log E), where E is the number of edges.
- For each edge, we compute the MST weight twice (once for exclude and once for include), which takes O(E α(V)) using Union-Find, where α is the inverse Ackermann function.
- Total complexity: O(E log E + E^2 α(V)).

Space Complexity:
- O(V) for the Union-Find data structure.

Topic: Graphs, Minimum Spanning Tree, Union-Find
"""