"""
LeetCode Problem #1579: Remove Max Number of Edges to Keep Graph Fully Traversable

Problem Statement:
Alice and Bob have an undirected graph of `n` nodes and three types of edges:

1. Type 1: Can be traversed by Alice only.
2. Type 2: Can be traversed by Bob only.
3. Type 3: Can be traversed by both Alice and Bob.

Given an array `edges` where `edges[i] = [type_i, u_i, v_i]` represents a bidirectional edge of type `type_i` between nodes `u_i` and `v_i`, find the maximum number of edges you can remove while still ensuring that the graph is fully traversable by both Alice and Bob. The graph is fully traversable if there is a path between any two nodes for both Alice and Bob.

Return the maximum number of edges you can remove, or return `-1` if it is impossible to make the graph fully traversable.

Constraints:
- `1 <= n <= 10^5`
- `1 <= edges.length <= min(10^5, 3 * n)`
- `edges[i].length == 3`
- `1 <= type_i <= 3`
- `1 <= u_i < v_i <= n`
- The input graph may not be connected.

Example:
Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,4],[2,3,4]]
Output: 2

Explanation: 
- Remove the two edges [1,1,4] and [2,3,4] to keep the graph fully traversable.
- The graph is fully traversable by Alice and Bob.

"""

from typing import List

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Helper function for Union-Find
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, rank, x, y):
            rootX = find(parent, x)
            rootY = find(parent, y)
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

        # Initialize Union-Find for Alice and Bob
        parent_alice = list(range(n + 1))
        parent_bob = list(range(n + 1))
        rank_alice = [0] * (n + 1)
        rank_bob = [0] * (n + 1)

        # Step 1: Add type 3 edges (shared by both Alice and Bob)
        used_edges = 0
        for t, u, v in edges:
            if t == 3:
                if union(parent_alice, rank_alice, u, v) | union(parent_bob, rank_bob, u, v):
                    used_edges += 1

        # Step 2: Add type 1 edges (Alice only)
        for t, u, v in edges:
            if t == 1:
                if union(parent_alice, rank_alice, u, v):
                    used_edges += 1

        # Step 3: Add type 2 edges (Bob only)
        for t, u, v in edges:
            if t == 2:
                if union(parent_bob, rank_bob, u, v):
                    used_edges += 1

        # Check if both Alice and Bob can traverse the entire graph
        if len(set(find(parent_alice, i) for i in range(1, n + 1))) > 1 or \
           len(set(find(parent_bob, i) for i in range(1, n + 1))) > 1:
            return -1

        # Maximum edges to remove = total edges - used edges
        return len(edges) - used_edges


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    n1 = 4
    edges1 = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,4],[2,3,4]]
    print(solution.maxNumEdgesToRemove(n1, edges1))  # Output: 2

    # Test Case 2
    n2 = 4
    edges2 = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
    print(solution.maxNumEdgesToRemove(n2, edges2))  # Output: 0

    # Test Case 3
    n3 = 2
    edges3 = [[2,1,2],[3,1,2],[1,1,2]]
    print(solution.maxNumEdgesToRemove(n3, edges3))  # Output: 1


"""
Time Complexity:
- The Union-Find operations (find and union) are nearly constant time due to path compression and union by rank.
- Processing all edges takes O(E * α(N)), where E is the number of edges and α is the inverse Ackermann function.
- Overall complexity: O(E * α(N)).

Space Complexity:
- We use parent and rank arrays for both Alice and Bob, each of size O(N).
- Overall space complexity: O(N).

Topic: Graphs, Union-Find
"""