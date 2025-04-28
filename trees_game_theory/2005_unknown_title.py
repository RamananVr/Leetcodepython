"""
LeetCode Problem #2005: Subtree Removal Game with Fibonacci Tree

Problem Statement:
You are given a tree with `n` nodes, where the nodes are numbered from `1` to `n`. The tree is rooted at node `1`. 
Each node has a value associated with it. The tree is a Fibonacci tree, meaning the number of nodes in the tree 
is a Fibonacci number.

Two players, Alice and Bob, play a game on this tree. They take turns removing a subtree rooted at any node 
that has not been removed yet. The player who cannot make a move loses the game. Alice always goes first.

Write a function `subtreeRemovalGame(n: int, edges: List[List[int]]) -> str` that determines the winner of the game 
if both players play optimally. Return "Alice" if Alice wins and "Bob" if Bob wins.

Constraints:
- 1 <= n <= 10^5
- edges is a list of `n-1` edges, where each edge connects two nodes in the tree.
- The tree is connected and has no cycles.
"""

from collections import defaultdict

def subtreeRemovalGame(n, edges):
    """
    Determines the winner of the subtree removal game on a Fibonacci tree.

    :param n: int - Number of nodes in the tree
    :param edges: List[List[int]] - List of edges in the tree
    :return: str - "Alice" if Alice wins, "Bob" if Bob wins
    """
    # Build the adjacency list for the tree
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Helper function to calculate the size of each subtree
    def calculate_subtree_sizes(node, parent):
        size = 1
        for neighbor in tree[node]:
            if neighbor != parent:
                size += calculate_subtree_sizes(neighbor, node)
        subtree_sizes[node] = size
        return size

    # Helper function to determine if a node is a winning position
    def is_winning_position(node, parent):
        xor_sum = 0
        for neighbor in tree[node]:
            if neighbor != parent:
                xor_sum ^= subtree_sizes[neighbor]
        return xor_sum != 0

    # Calculate subtree sizes
    subtree_sizes = {}
    calculate_subtree_sizes(1, -1)

    # Check if the root is a winning position
    if is_winning_position(1, -1):
        return "Alice"
    else:
        return "Bob"

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 5
    edges1 = [[1, 2], [1, 3], [3, 4], [3, 5]]
    print(subtreeRemovalGame(n1, edges1))  # Expected Output: "Alice"

    # Test Case 2
    n2 = 3
    edges2 = [[1, 2], [1, 3]]
    print(subtreeRemovalGame(n2, edges2))  # Expected Output: "Bob"

    # Test Case 3
    n3 = 7
    edges3 = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7]]
    print(subtreeRemovalGame(n3, edges3))  # Expected Output: "Alice"

"""
Time Complexity Analysis:
- Building the adjacency list takes O(n) time.
- Calculating subtree sizes using DFS takes O(n) time.
- Checking if the root is a winning position takes O(n) time.
Overall, the time complexity is O(n).

Space Complexity Analysis:
- The adjacency list takes O(n) space.
- The subtree_sizes dictionary takes O(n) space.
- The recursion stack for DFS takes O(h) space, where h is the height of the tree. In the worst case, h = O(n).
Overall, the space complexity is O(n).

Topic: Trees, Game Theory
"""