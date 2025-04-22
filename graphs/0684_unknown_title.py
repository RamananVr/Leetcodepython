"""
LeetCode Problem #684: Redundant Connection

Problem Statement:
In this problem, a tree is an undirected graph that is connected and has no cycles. 
You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, 
with one additional edge added. The added edge has created a cycle in the graph, 
and you need to find that edge and return it.

The input is a 2D array `edges` of length `n` where `edges[i] = [ui, vi]` indicates 
that there is an undirected edge between nodes `ui` and `vi`.

Return an edge that can be removed so that the resulting graph is a tree of `n` nodes. 
If there are multiple answers, return the edge that occurs last in the input.

Constraints:
- `n == edges.length`
- `3 <= n <= 1000`
- `edges[i].length == 2`
- `1 <= ui < vi <= n`
- The input is guaranteed to form a graph that has exactly one cycle.

Example:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
"""

# Solution
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False  # Cycle detected
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

def findRedundantConnection(edges):
    n = len(edges)
    uf = UnionFind(n + 1)  # Initialize Union-Find for nodes 1 to n
    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    edges1 = [[1, 2], [1, 3], [2, 3]]
    print(findRedundantConnection(edges1))  # Output: [2, 3]

    # Test Case 2
    edges2 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    print(findRedundantConnection(edges2))  # Output: [1, 4]

    # Test Case 3
    edges3 = [[1, 2], [2, 3], [3, 4], [4, 5], [2, 5]]
    print(findRedundantConnection(edges3))  # Output: [2, 5]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The `find` operation uses path compression, which has an amortized time complexity of O(α(n)), 
  where α(n) is the inverse Ackermann function. For all practical purposes, α(n) is a very small constant.
- The `union` operation also has an amortized time complexity of O(α(n)).
- Since we process each edge once, the overall time complexity is O(n * α(n)), which is effectively O(n).

Space Complexity:
- The Union-Find data structure uses O(n) space to store the `parent` and `rank` arrays.
- Thus, the space complexity is O(n).

Topic: Graphs
"""