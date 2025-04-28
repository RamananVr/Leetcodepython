"""
LeetCode Problem #310: Minimum Height Trees

Problem Statement:
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree with `n` nodes labeled from `0` to `n-1`, and an array of `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between the two nodes `ai` and `bi`, you need to find all the minimum height trees (MHTs) and return their root labels in an array. 

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

A node can be a root of a tree only if it minimizes the height of the tree. When there are multiple MHTs, return all of them in any order.

The given graph is guaranteed to be a tree, so there will always be a solution.

Constraints:
- `1 <= n <= 2 * 10^4`
- `edges.length == n - 1`
- `0 <= ai, bi < n`
- `ai != bi`
- All the pairs `(ai, bi)` are distinct.

Example 1:
Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]
Output: [1]

Example 2:
Input: n = 6, edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
Output: [3, 4]

Follow up:
Can you find the solution in linear time complexity?
"""

from collections import defaultdict, deque

def findMinHeightTrees(n, edges):
    """
    Finds all the minimum height trees (MHTs) and returns their root labels.

    :param n: int - Number of nodes in the tree
    :param edges: List[List[int]] - List of edges in the tree
    :return: List[int] - List of root labels of MHTs
    """
    if n == 1:
        return [0]
    
    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # Initialize leaves (nodes with only one connection)
    leaves = deque([node for node in range(n) if len(graph[node]) == 1])
    
    # Trim leaves layer by layer until 2 or fewer nodes remain
    remaining_nodes = n
    while remaining_nodes > 2:
        leaves_count = len(leaves)
        remaining_nodes -= leaves_count
        for _ in range(leaves_count):
            leaf = leaves.popleft()
            # Remove the leaf from its neighbor's adjacency list
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            # If the neighbor becomes a leaf, add it to the queue
            if len(graph[neighbor]) == 1:
                leaves.append(neighbor)
    
    # The remaining nodes are the roots of the MHTs
    return list(leaves)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 4
    edges1 = [[1, 0], [1, 2], [1, 3]]
    print(findMinHeightTrees(n1, edges1))  # Output: [1]

    # Test Case 2
    n2 = 6
    edges2 = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    print(findMinHeightTrees(n2, edges2))  # Output: [3, 4]

    # Test Case 3
    n3 = 1
    edges3 = []
    print(findMinHeightTrees(n3, edges3))  # Output: [0]

    # Test Case 4
    n4 = 2
    edges4 = [[0, 1]]
    print(findMinHeightTrees(n4, edges4))  # Output: [0, 1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph takes O(n) time since there are n-1 edges.
- The trimming process involves visiting each node and edge once, which also takes O(n) time.
- Overall, the time complexity is O(n).

Space Complexity:
- The adjacency list representation of the graph takes O(n) space.
- The queue for leaves and other auxiliary data structures also take O(n) space.
- Overall, the space complexity is O(n).

Topic: Graphs
"""