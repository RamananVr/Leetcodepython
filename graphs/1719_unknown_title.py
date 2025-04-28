"""
LeetCode Problem #1719: Number Of Ways To Reconstruct A Tree

Problem Statement:
You are given an array pairs, where pairs[i] = [xi, yi], and:
- There are no duplicates.
- xi < yi.

Let us define a rooted tree as follows:
- The root is the only node with no parent.
- Each node with a parent has exactly one parent.
- A pair [xi, yi] exists in pairs if and only if xi is an ancestor of yi or yi is an ancestor of xi (in other words, xi and yi are connected directly or indirectly).

Given pairs, you need to answer the following questions:
1. Is it possible to reconstruct exactly one rooted tree that satisfies the above conditions?
2. If it is possible, return 1.
3. If there are multiple ways to reconstruct the tree, return 2.
4. If it is impossible to reconstruct any tree, return 0.

Constraints:
- 1 <= pairs.length <= 10^5
- 1 <= xi < yi <= 500
- The input is guaranteed to be a set of unique pairs.

"""

from collections import defaultdict, deque

def checkWays(pairs):
    # Step 1: Build the adjacency list
    adj = defaultdict(set)
    for x, y in pairs:
        adj[x].add(y)
        adj[y].add(x)

    # Step 2: Find the root (node with the maximum degree)
    root = -1
    for node in adj:
        if root == -1 or len(adj[node]) > len(adj[root]):
            root = node

    # If the root cannot connect to all other nodes, return 0
    if len(adj[root]) != len(adj) - 1:
        return 0

    # Step 3: Check the tree structure
    res = 1
    for node in adj:
        if node == root:
            continue

        # Find the parent of the current node
        parent = -1
        curr_degree = len(adj[node])
        for neighbor in adj[node]:
            if len(adj[neighbor]) > curr_degree:
                if parent == -1 or len(adj[neighbor]) < len(adj[parent]):
                    parent = neighbor

        # If no valid parent is found, return 0
        if parent == -1:
            return 0

        # Check if the current node's neighbors are a subset of the parent's neighbors
        if not adj[node].issubset(adj[parent]):
            return 0

        # If there are multiple valid parent-child relationships, set res to 2
        if len(adj[node]) == len(adj[parent]):
            res = 2

    return res

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Single valid tree
    pairs1 = [[1, 2], [2, 3]]
    print(checkWays(pairs1))  # Output: 1

    # Test Case 2: Multiple valid trees
    pairs2 = [[1, 2], [2, 3], [1, 3]]
    print(checkWays(pairs2))  # Output: 2

    # Test Case 3: Impossible to form a tree
    pairs3 = [[1, 2], [2, 3], [2, 4], [1, 5]]
    print(checkWays(pairs3))  # Output: 0

    # Test Case 4: Single node tree
    pairs4 = [[1, 2]]
    print(checkWays(pairs4))  # Output: 1

"""
Time Complexity:
- Building the adjacency list takes O(pairs.length).
- Finding the root takes O(V), where V is the number of unique nodes.
- Checking the tree structure involves iterating over all nodes and their neighbors, which takes O(V + E), where E is the number of edges.
- Overall time complexity: O(V + E), where V is the number of unique nodes and E is the number of edges (pairs.length).

Space Complexity:
- The adjacency list requires O(V + E) space.
- Additional variables and sets require O(V) space.
- Overall space complexity: O(V + E).

Topic: Graphs
"""