"""
LeetCode Problem #2378: Choose Edges to Maximize Score in a Tree

Problem Statement:
You are given a tree (an undirected graph with no cycles) consisting of `n` nodes numbered from `0` to `n-1` and `n-1` edges. 
Each edge has a score associated with it, represented by the array `scores` of size `n-1`, where `scores[i]` is the score of the `i-th` edge.

You are tasked to choose a subset of edges such that:
1. The chosen edges form a connected subgraph of the tree.
2. The sum of the scores of the chosen edges is maximized.

Return the maximum possible score.

Constraints:
- `1 <= n <= 10^5`
- `scores.length == n-1`
- `1 <= scores[i] <= 10^6`

Note: The input is given as an adjacency list representation of the tree, where `edges` is a list of tuples `(u, v, i)` representing an edge between nodes `u` and `v` with index `i` in the `scores` array.

"""

from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def maximizeTreeScore(n, edges, scores):
    """
    Function to calculate the maximum possible score by choosing edges in a tree.

    :param n: int - Number of nodes in the tree
    :param edges: List[Tuple[int, int, int]] - List of edges in the form (u, v, i), where i is the index in scores
    :param scores: List[int] - List of scores for each edge
    :return: int - Maximum possible score
    """
    # Build adjacency list for the tree
    graph = defaultdict(list)
    for u, v, i in edges:
        graph[u].append((v, i))
        graph[v].append((u, i))
    
    # Initialize variables
    visited = [False] * n
    max_score = 0

    def dfs(node):
        nonlocal max_score
        visited[node] = True
        local_score = 0

        for neighbor, edge_index in graph[node]:
            if not visited[neighbor]:
                # Perform DFS on the child node
                child_score = dfs(neighbor)
                # Add the score of the edge connecting the current node and the child
                local_score += child_score + scores[edge_index]
        
        # Update the global maximum score
        max_score = max(max_score, local_score)
        return local_score

    # Start DFS from node 0 (or any arbitrary node, since it's a connected tree)
    dfs(0)
    return max_score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 5
    edges1 = [(0, 1, 0), (1, 2, 1), (1, 3, 2), (3, 4, 3)]
    scores1 = [1, 2, 3, 4]
    print(maximizeTreeScore(n1, edges1, scores1))  # Expected Output: 10

    # Test Case 2
    n2 = 3
    edges2 = [(0, 1, 0), (1, 2, 1)]
    scores2 = [5, 10]
    print(maximizeTreeScore(n2, edges2, scores2))  # Expected Output: 15

    # Test Case 3
    n3 = 4
    edges3 = [(0, 1, 0), (1, 2, 1), (2, 3, 2)]
    scores3 = [3, 6, 9]
    print(maximizeTreeScore(n3, edges3, scores3))  # Expected Output: 18

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the adjacency list takes O(n) time, where n is the number of nodes.
- The DFS traversal visits each node and edge exactly once, taking O(n) time.
- Overall time complexity: O(n).

Space Complexity:
- The adjacency list requires O(n) space.
- The visited array requires O(n) space.
- The recursion stack in the DFS can go up to O(n) in the worst case.
- Overall space complexity: O(n).

Topic: Graphs, Trees, DFS
"""