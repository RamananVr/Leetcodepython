"""
LeetCode Problem #1724: Checking Existence of Edge Length Limited Paths

Problem Statement:
An undirected graph of `n` nodes is defined by `edgeList`, where `edgeList[i] = [u, v, dis]` denotes a bidirectional edge 
between nodes `u` and `v` with distance `dis`. You are also given a 2D array `queries`, where `queries[j] = [p, q, limit]`.

The task is to determine for each query whether there is a path between `p` and `q` such that every edge on the path 
has a distance strictly less than `limit[j]`. Return a boolean array `answer`, where `answer[j]` is the answer to the 
`j-th` query.

Constraints:
- `2 <= n <= 10^5`
- `1 <= edgeList.length, queries.length <= 10^5`
- `edgeList[i].length == 3`
- `queries[j].length == 3`
- `0 <= u, v, p, q <= n - 1`
- `u != v`
- `p != q`
- `1 <= dis, limit <= 10^9`
- There may be multiple edges between two nodes.

Example:
Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8]], queries = [[0,1,2],[0,2,5]]
Output: [False, True]
Explanation:
- For the first query, there is no path from 0 to 1 with all edges having a distance strictly less than 2.
- For the second query, there is a path from 0 to 2 via 0 -> 1 -> 2 with all edges having a distance less than 5.
"""

from typing import List

class UnionFind:
    """Union-Find (Disjoint Set Union) data structure with path compression and union by rank."""
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True

def distanceLimitedPathsExist(n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
    # Sort edgeList by distance
    edgeList.sort(key=lambda x: x[2])
    # Add indices to queries and sort by limit
    queries = [(p, q, limit, i) for i, (p, q, limit) in enumerate(queries)]
    queries.sort(key=lambda x: x[2])

    uf = UnionFind(n)
    result = [False] * len(queries)
    edgeIndex = 0

    # Process each query
    for p, q, limit, queryIndex in queries:
        # Add all edges with distance < limit to the union-find structure
        while edgeIndex < len(edgeList) and edgeList[edgeIndex][2] < limit:
            u, v, dis = edgeList[edgeIndex]
            uf.union(u, v)
            edgeIndex += 1
        # Check if p and q are connected
        result[queryIndex] = uf.find(p) == uf.find(q)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 3
    edgeList1 = [[0, 1, 2], [1, 2, 4], [2, 0, 8]]
    queries1 = [[0, 1, 2], [0, 2, 5]]
    print(distanceLimitedPathsExist(n1, edgeList1, queries1))  # Output: [False, True]

    # Test Case 2
    n2 = 5
    edgeList2 = [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]]
    queries2 = [[0, 4, 14], [1, 4, 13], [2, 3, 6]]
    print(distanceLimitedPathsExist(n2, edgeList2, queries2))  # Output: [True, False, False]

# Time Complexity:
# - Sorting edgeList: O(E log E), where E is the number of edges.
# - Sorting queries: O(Q log Q), where Q is the number of queries.
# - Union-Find operations: O(α(N)) per operation, where α is the inverse Ackermann function.
# Overall: O(E log E + Q log Q + (E + Q) α(N))

# Space Complexity:
# - Union-Find data structure: O(N), where N is the number of nodes.
# - Result array: O(Q).
# Overall: O(N + Q)

# Topic: Graphs, Union-Find (Disjoint Set Union)