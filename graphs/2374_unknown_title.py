"""
LeetCode Problem #2374: Node With Highest Edge Score

Problem Statement:
You are given a directed graph with `n` nodes labeled from `0` to `n - 1`, where each node has exactly one outgoing edge.

The graph is represented by a 0-indexed integer array `edges` of length `n`, where `edges[i]` indicates that there is a directed edge from node `i` to node `edges[i]`.

The edge score of a node `i` is the sum of `i` over all nodes `j` such that there is a directed edge from `j` to `i`.

Return the node with the highest edge score. If multiple nodes have the same edge score, return the smallest index.

Constraints:
- `n == edges.length`
- `2 <= n <= 10^5`
- `0 <= edges[i] < n`
- `edges[i] != i`

Example:
Input: edges = [1,0,0,0,0,7,7,5]
Output: 7
Explanation:
- The edge score of node 0 is: 1 + 2 + 3 + 4 = 10.
- The edge score of node 1 is: 0.
- The edge score of node 5 is: 7.
- The edge score of node 7 is: 5 + 6 = 11.
Node 7 has the highest edge score, so we return 7.
"""

# Python Solution
from collections import defaultdict

def edgeScore(edges):
    """
    Function to find the node with the highest edge score.
    
    :param edges: List[int] - The directed graph represented as an array.
    :return: int - The node with the highest edge score.
    """
    edge_scores = defaultdict(int)
    
    # Calculate edge scores
    for i, target in enumerate(edges):
        edge_scores[target] += i
    
    # Find the node with the highest edge score
    max_score = -1
    result_node = -1
    for node, score in edge_scores.items():
        if score > max_score or (score == max_score and node < result_node):
            max_score = score
            result_node = node
    
    return result_node

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    edges = [1, 0, 0, 0, 0, 7, 7, 5]
    print(edgeScore(edges))  # Output: 7

    # Test Case 2
    edges = [2, 0, 0, 2]
    print(edgeScore(edges))  # Output: 0

    # Test Case 3
    edges = [1, 2, 0]
    print(edgeScore(edges))  # Output: 0

    # Test Case 4
    edges = [1, 2, 3, 0]
    print(edgeScore(edges))  # Output: 0

"""
Time Complexity Analysis:
- Calculating edge scores involves iterating through the `edges` array once, which takes O(n) time.
- Finding the node with the highest edge score involves iterating through the `edge_scores` dictionary, which has at most `n` entries. This also takes O(n) time.
- Overall time complexity: O(n).

Space Complexity Analysis:
- The `edge_scores` dictionary stores at most `n` entries, where each entry corresponds to a node. This requires O(n) space.
- Overall space complexity: O(n).

Topic: Graphs
"""