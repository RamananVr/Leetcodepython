"""
LeetCode Problem #1557: Minimum Number of Vertices to Reach All Nodes

Problem Statement:
Given a directed acyclic graph (DAG) with `n` nodes labeled from `0` to `n-1`, 
and an array `edges` where `edges[i] = [fromi, toi]` represents a directed edge 
from node `fromi` to node `toi`, find the smallest set of vertices from which 
all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

You may return the vertices in any order.

Example 1:
Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
Explanation: It's not possible to reach all the nodes from a smaller set of vertices.

Example 2:
Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Output: [0,2,3]
Explanation: Notice that nodes 0, 2, and 3 are sufficient to reach all nodes.

Constraints:
- 2 <= n <= 10^5
- 1 <= edges.length <= min(10^5, n * (n - 1) / 2)
- edges[i].length == 2
- 0 <= fromi, toi < n
- All pairs (fromi, toi) are distinct.

"""

# Python Solution
def findSmallestSetOfVertices(n, edges):
    """
    This function finds the minimum set of vertices from which all nodes in the graph are reachable.
    
    Args:
    n (int): Number of nodes in the graph.
    edges (List[List[int]]): List of directed edges in the graph.

    Returns:
    List[int]: List of vertices that form the minimum set.
    """
    # Step 1: Create a set to track nodes with incoming edges
    has_incoming = set()

    # Step 2: Populate the set with all nodes that have incoming edges
    for _, to in edges:
        has_incoming.add(to)

    # Step 3: The result is all nodes that do not have incoming edges
    return [node for node in range(n) if node not in has_incoming]


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 6
    edges1 = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
    print(findSmallestSetOfVertices(n1, edges1))  # Output: [0, 3]

    # Test Case 2
    n2 = 5
    edges2 = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
    print(findSmallestSetOfVertices(n2, edges2))  # Output: [0, 2, 3]

    # Test Case 3
    n3 = 4
    edges3 = [[1, 0], [2, 0], [3, 0]]
    print(findSmallestSetOfVertices(n3, edges3))  # Output: [1, 2, 3]

    # Test Case 4
    n4 = 3
    edges4 = [[0, 1], [1, 2]]
    print(findSmallestSetOfVertices(n4, edges4))  # Output: [0]

    # Test Case 5
    n5 = 7
    edges5 = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 6]]
    print(findSmallestSetOfVertices(n5, edges5))  # Output: [0, 4]


# Time and Space Complexity Analysis

# Time Complexity:
# - Iterating through the `edges` list takes O(E), where E is the number of edges.
# - Checking all nodes from 0 to n-1 to see if they are in the `has_incoming` set takes O(n).
# - Overall time complexity: O(n + E).

# Space Complexity:
# - The `has_incoming` set stores at most n elements, so it takes O(n) space.
# - The result list also takes O(n) space in the worst case.
# - Overall space complexity: O(n).

# Topic: Graphs