"""
LeetCode Problem #2581: Count Number of Possible Root Nodes

Problem Statement:
You are given a tree with `n` nodes labeled from `1` to `n` and an array `edges` of size `n-1` where `edges[i] = [u, v]` 
indicates that there is an undirected edge between nodes `u` and `v`. You are also given an array `guesses` where 
`guesses[i] = [u, v]` indicates that you guess node `u` is the parent of node `v`.

A node `x` is called a "possible root" if the number of correct guesses for the tree rooted at `x` is greater than or 
equal to a given integer `k`.

Return the number of possible roots.

Constraints:
- `n == edges.length + 1`
- `2 <= n <= 10^5`
- `1 <= edges[i][0], edges[i][1] <= n`
- `1 <= guesses.length <= 10^5`
- `1 <= guesses[i][0], guesses[i][1] <= n`
- `0 <= k <= guesses.length`

"""

from collections import defaultdict

def rootCount(edges, guesses, k):
    """
    Function to count the number of possible root nodes.

    :param edges: List[List[int]] - List of edges in the tree.
    :param guesses: List[List[int]] - List of guesses about parent-child relationships.
    :param k: int - Minimum number of correct guesses required.
    :return: int - Number of possible root nodes.
    """
    # Build the adjacency list for the tree
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Convert guesses into a set for O(1) lookup
    guess_set = set((u, v) for u, v in guesses)

    # Helper function to calculate the initial number of correct guesses
    def dfs(node, parent):
        nonlocal initial_correct
        for neighbor in tree[node]:
            if neighbor != parent:
                if (node, neighbor) in guess_set:
                    initial_correct += 1
                dfs(neighbor, node)

    # Helper function to calculate the number of correct guesses for each root
    def reroot(node, parent, correct):
        nonlocal possible_roots
        # Check if the current root satisfies the condition
        if correct >= k:
            possible_roots += 1
        for neighbor in tree[node]:
            if neighbor != parent:
                # Adjust the correct count when rerooting
                if (node, neighbor) in guess_set:
                    correct -= 1
                if (neighbor, node) in guess_set:
                    correct += 1
                reroot(neighbor, node, correct)
                # Revert the changes to correct count
                if (node, neighbor) in guess_set:
                    correct += 1
                if (neighbor, node) in guess_set:
                    correct -= 1

    # Initialize variables
    initial_correct = 0
    possible_roots = 0

    # Perform the first DFS to calculate the initial number of correct guesses
    dfs(1, -1)

    # Perform the second DFS to count the number of possible roots
    reroot(1, -1, initial_correct)

    return possible_roots

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    edges = [[1, 2], [1, 3], [3, 4], [3, 5]]
    guesses = [[1, 2], [3, 4], [3, 5], [4, 3]]
    k = 3
    print(rootCount(edges, guesses, k))  # Output: 1

    # Test Case 2
    edges = [[1, 2], [2, 3], [3, 4], [4, 5]]
    guesses = [[1, 2], [2, 3], [3, 4], [4, 5]]
    k = 2
    print(rootCount(edges, guesses, k))  # Output: 4

    # Test Case 3
    edges = [[1, 2], [2, 3], [2, 4]]
    guesses = [[1, 2], [2, 3], [2, 4]]
    k = 1
    print(rootCount(edges, guesses, k))  # Output: 3

"""
Time Complexity:
- Building the adjacency list: O(n)
- First DFS to calculate initial correct guesses: O(n)
- Second DFS to reroot and count possible roots: O(n)
- Total: O(n)

Space Complexity:
- Adjacency list: O(n)
- Guess set: O(g), where g is the number of guesses
- Recursive stack space: O(n) in the worst case
- Total: O(n + g)

Topic: Trees, DFS
"""