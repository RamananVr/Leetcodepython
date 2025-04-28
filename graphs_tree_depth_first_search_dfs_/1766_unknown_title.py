"""
LeetCode Problem #1766: Tree of Coprimes

Problem Statement:
You are given a tree (i.e., a connected, undirected graph that has no cycles) consisting of `n` nodes numbered from `0` to `n - 1` and exactly `n - 1` edges. The root of the tree is node `0`, and each node has a value associated with it, given in the integer array `nums`.

When traversing the tree, you can select a node and move to one of its adjacent nodes. You are tasked with finding the closest ancestor node to each node `i` such that the values of the ancestor node and node `i` are coprime. Two integers `x` and `y` are coprime if `gcd(x, y) == 1`.

Return an array `ans` of size `n`, where `ans[i]` is the closest ancestor node to node `i` that is coprime with `nums[i]`, or `-1` if there is no such ancestor.

Example:
Input: nums = [2, 3, 6, 2, 5, 12], edges = [[0, 1], [1, 2], [1, 3], [2, 4], [2, 5]]
Output: [-1, 0, -1, 1, 2, -1]

Constraints:
1. `nums.length == n`
2. `1 <= nums[i] <= 50`
3. `1 <= n <= 10^4`
4. `edges.length == n - 1`
5. `edges[i].length == 2`
6. `0 <= edges[i][0], edges[i][1] < n`
7. `edges` represents a valid tree.

"""

from math import gcd
from collections import defaultdict, deque

def coprimeAncestors(nums, edges):
    # Helper function to check if two numbers are coprime
    def are_coprime(a, b):
        return gcd(a, b) == 1

    # Build the tree as an adjacency list
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Result array
    n = len(nums)
    result = [-1] * n

    # Store the last seen node for each value (1 to 50)
    last_seen = defaultdict(list)

    # DFS function
    def dfs(node, parent, depth):
        # Find the closest coprime ancestor
        closest_ancestor = -1
        max_depth = -1
        for value, ancestors in last_seen.items():
            if are_coprime(nums[node], value):
                for ancestor, ancestor_depth in ancestors:
                    if ancestor_depth > max_depth:
                        max_depth = ancestor_depth
                        closest_ancestor = ancestor
        result[node] = closest_ancestor

        # Add the current node to the last_seen for its value
        last_seen[nums[node]].append((node, depth))

        # Recurse for children
        for neighbor in tree[node]:
            if neighbor != parent:
                dfs(neighbor, node, depth + 1)

        # Backtrack: remove the current node from last_seen
        last_seen[nums[node]].pop()

    # Start DFS from the root (node 0)
    dfs(0, -1, 0)

    return result

# Example Test Cases
if __name__ == "__main__":
    nums = [2, 3, 6, 2, 5, 12]
    edges = [[0, 1], [1, 2], [1, 3], [2, 4], [2, 5]]
    print(coprimeAncestors(nums, edges))  # Output: [-1, 0, -1, 1, 2, -1]

    nums = [10, 15, 20, 25, 30]
    edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
    print(coprimeAncestors(nums, edges))  # Output: [-1, 0, 1, 1, 3]

# Time Complexity Analysis:
# - The DFS traversal visits each node once, so the time complexity is O(n).
# - For each node, we check coprimality with at most 50 values (since nums[i] <= 50), which is O(1) per node.
# - Overall time complexity: O(n).

# Space Complexity Analysis:
# - The adjacency list representation of the tree takes O(n) space.
# - The `last_seen` dictionary can store at most 50 keys, each with a list of ancestors, so its space complexity is O(n).
# - Overall space complexity: O(n).

# Topic: Graphs, Tree, Depth-First Search (DFS)