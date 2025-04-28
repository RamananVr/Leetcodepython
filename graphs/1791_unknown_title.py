"""
LeetCode Problem #1791: Find Center of Star Graph

Problem Statement:
There is an undirected star graph consisting of `n` nodes labeled from `1` to `n`. 
A star graph is a graph where there is one center node and exactly `n - 1` edges 
that connect the center node with every other node.

You are given a 2D integer array `edges` where each `edges[i] = [ui, vi]` indicates 
that there is an edge between the nodes `ui` and `vi`. Return the center of the given star graph.

Constraints:
- 3 <= n <= 10^5
- edges.length == n - 1
- edges[i].length == 2
- 1 <= ui, vi <= n
- ui != vi
- The given `edges` represent a valid star graph.

Example 1:
Input: edges = [[1,2],[2,3],[4,2]]
Output: 2

Example 2:
Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1
"""

# Solution
def findCenter(edges):
    """
    Function to find the center of a star graph.

    Args:
    edges (List[List[int]]): List of edges representing the star graph.

    Returns:
    int: The center node of the star graph.
    """
    # The center node must appear in both the first and second edges.
    # We can simply check which node is common between the two edges.
    return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    edges1 = [[1, 2], [2, 3], [4, 2]]
    print(findCenter(edges1))  # Output: 2

    # Test Case 2
    edges2 = [[1, 2], [5, 1], [1, 3], [1, 4]]
    print(findCenter(edges2))  # Output: 1

    # Test Case 3
    edges3 = [[3, 4], [4, 2], [4, 1]]
    print(findCenter(edges3))  # Output: 4

    # Test Case 4
    edges4 = [[6, 7], [7, 8], [7, 9], [7, 10]]
    print(findCenter(edges4))  # Output: 7

"""
Time Complexity Analysis:
- The solution only checks the first two edges, which is an O(1) operation.
- Therefore, the time complexity is O(1).

Space Complexity Analysis:
- The solution uses a constant amount of extra space.
- Therefore, the space complexity is O(1).

Topic: Graphs
"""