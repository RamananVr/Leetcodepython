"""
LeetCode Problem #685: Redundant Connection II

Problem Statement:
In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, and every node has exactly one parent, except for the root node which has no parent.

The given input is a directed graph that started as a rooted tree with `n` nodes (with distinct values from 1 to `n`), with one additional directed edge added. The added edge has two different cases:

1. The edge causes a node to have two parents.
2. The edge creates a cycle in the graph.

Your task is to return an edge that can be removed so that the resulting graph is a rooted tree of `n` nodes. If there are multiple answers, return the edge that occurs last in the input.

Constraints:
- `n == edges.length`
- `2 <= n <= 1000`
- `edges[i].length == 2`
- `1 <= ai, bi <= n`
- `ai != bi`

Example 1:
Input: edges = [[1,2], [1,3], [2,3]]
Output: [2,3]

Example 2:
Input: edges = [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
"""

from typing import List

def findRedundantDirectedConnection(edges: List[List[int]]) -> List[int]:
    parent = {}
    candidate1 = candidate2 = None

    # Step 1: Check for a node with two parents
    for u, v in edges:
        if v in parent:
            candidate1 = [parent[v], v]
            candidate2 = [u, v]
            break
        parent[v] = u

    # Union-Find to detect cycles
    def find(uf, x):
        if uf[x] != x:
            uf[x] = find(uf, uf[x])
        return uf[x]

    def union(uf, x, y):
        rootX = find(uf, x)
        rootY = find(uf, y)
        if rootX == rootY:
            return False
        uf[rootX] = rootY
        return True

    # Step 2: Check for cycles
    uf = {i: i for i in range(1, len(edges) + 1)}
    for u, v in edges:
        if [u, v] == candidate2:
            continue
        if not union(uf, u, v):
            # If there's a cycle and no node has two parents
            if not candidate1:
                return [u, v]
            # If there's a cycle and a node has two parents
            return candidate1

    # If no cycle but a node has two parents
    return candidate2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    edges1 = [[1, 2], [1, 3], [2, 3]]
    print(findRedundantDirectedConnection(edges1))  # Output: [2, 3]

    # Test Case 2
    edges2 = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]
    print(findRedundantDirectedConnection(edges2))  # Output: [4, 1]

    # Test Case 3
    edges3 = [[2, 1], [3, 1], [4, 2], [1, 4]]
    print(findRedundantDirectedConnection(edges3))  # Output: [2, 1]

"""
Time Complexity:
- The Union-Find operations (find and union) are nearly constant time due to path compression and union by rank.
- Iterating through the edges takes O(n), where n is the number of edges.
- Overall time complexity: O(n).

Space Complexity:
- The space complexity is O(n) for the Union-Find data structure and the parent dictionary.

Topic: Graphs, Union-Find
"""