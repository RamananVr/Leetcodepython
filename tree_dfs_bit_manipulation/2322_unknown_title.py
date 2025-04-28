"""
LeetCode Problem #2322: Minimum Score After Removals on a Tree

Problem Statement:
You are given a tree (i.e., a connected, undirected graph with no cycles) consisting of `n` nodes numbered from `0` to `n - 1` and exactly `n - 1` edges. The tree is represented by a 2D integer array `edges` of length `n - 1`, where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi`.

Each node has a value associated with it, given by an integer array `nums` of length `n`.

You need to perform the following steps:
1. Remove any two edges from the tree, resulting in three connected components.
2. Take the XOR of all the values in each component to get three integers.
3. Return the minimum score possible, where the score is defined as the difference between the maximum and minimum of these three integers.

Constraints:
- `n == nums.length`
- `1 <= n <= 1000`
- `nums[i]` is a positive integer.
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`
- The input is guaranteed to be a valid tree.

"""

from collections import defaultdict
from itertools import combinations

def minimumScore(nums, edges):
    """
    Function to calculate the minimum score after removing two edges from the tree.
    """
    # Step 1: Build the tree as an adjacency list
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    # Step 2: Perform DFS to calculate XOR values for all subtrees
    n = len(nums)
    xor = [0] * n
    parent = [-1] * n

    def dfs(node, par):
        xor[node] = nums[node]
        parent[node] = par
        for neighbor in tree[node]:
            if neighbor != par:
                dfs(neighbor, node)
                xor[node] ^= xor[neighbor]

    dfs(0, -1)

    # Step 3: Generate all possible pairs of edges to remove
    def get_subtree_xor(node, exclude):
        result = xor[node]
        for neighbor in tree[node]:
            if neighbor != parent[node] and neighbor != exclude:
                result ^= xor[neighbor]
        return result

    min_score = float('inf')
    for u, v in edges:
        for x, y in edges:
            if (u, v) == (x, y):
                continue
            # Remove edges (u, v) and (x, y)
            subtree1 = get_subtree_xor(u, v)
            subtree2 = get_subtree_xor(x, y)
            subtree3 = xor[0] ^ subtree1 ^ subtree2

            # Calculate score
            score = max(subtree1, subtree2, subtree3) - min(subtree1, subtree2, subtree3)
            min_score = min(min_score, score)

    return min_score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [1, 5, 5, 4, 11]
    edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
    print(minimumScore(nums, edges))  # Expected Output: 9

    # Test Case 2
    nums = [1, 3, 5, 7]
    edges = [[0, 1], [1, 2], [2, 3]]
    print(minimumScore(nums, edges))  # Expected Output: 6

    # Test Case 3
    nums = [2, 4, 6, 8, 10]
    edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
    print(minimumScore(nums, edges))  # Expected Output: 14

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the adjacency list takes O(n).
- DFS traversal to calculate XOR values takes O(n).
- Generating all pairs of edges to remove takes O((n-1)^2), where n-1 is the number of edges.
- Calculating subtree XOR values for each pair of edges takes O(n) in the worst case.
- Overall time complexity: O(n + (n-1)^2 * n) ≈ O(n^3).

Space Complexity:
- The adjacency list takes O(n) space.
- The `xor` and `parent` arrays take O(n) space.
- The recursion stack for DFS takes O(n) space in the worst case.
- Overall space complexity: O(n).

Topic: Tree, DFS, Bit Manipulation
"""