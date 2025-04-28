"""
LeetCode Problem #2791: Count Paths That Can Form a Palindrome in a Tree

Problem Statement:
You are given a tree (i.e., a connected, undirected graph with no cycles) consisting of `n` nodes numbered from `0` to `n - 1` and exactly `n - 1` edges. Each node has a lowercase English letter assigned to it. The tree is represented by a 0-indexed array `parent` of size `n`, where `parent[i]` is the parent of node `i`. Since node `0` is the root, `parent[0] == -1`.

You are also given a string `s` of length `n`, where `s[i]` is the character assigned to the `i-th` node.

Return the number of pairs of nodes `(u, v)` such that the characters on the path from `u` to `v` can be rearranged to form a palindrome.

A string is a palindrome if it reads the same forward and backward.

Constraints:
- `n == parent.length == s.length`
- `1 <= n <= 10^5`
- `parent[0] == -1`
- `0 <= parent[i] <= n - 1` for all `i > 0`
- `parent` represents a valid tree.
- `s` consists of only lowercase English letters.

---

Solution:
"""

from collections import defaultdict
from functools import lru_cache

def countPalindromePaths(parent, s):
    def dfs(node, mask):
        nonlocal result
        # Update the current mask for the node
        mask ^= 1 << (ord(s[node]) - ord('a'))
        
        # Check if the current mask has been seen before
        result += mask_count[mask]
        
        # Check for masks that differ by exactly one bit (single character change)
        for i in range(26):
            result += mask_count[mask ^ (1 << i)]
        
        # Increment the count of the current mask
        mask_count[mask] += 1
        
        # Recur for all children
        for child in tree[node]:
            dfs(child, mask)
        
        # Backtrack: Decrement the count of the current mask
        mask_count[mask] -= 1

    # Build the tree from the parent array
    n = len(parent)
    tree = defaultdict(list)
    for i in range(1, n):
        tree[parent[i]].append(i)
    
    # Initialize variables
    mask_count = defaultdict(int)
    mask_count[0] = 1  # Base case: empty path
    result = 0
    
    # Start DFS from the root node (0) with an initial mask of 0
    dfs(0, 0)
    
    return result

"""
Example Test Cases:
"""

if __name__ == "__main__":
    # Test Case 1
    parent = [-1, 0, 0, 1, 1, 2]
    s = "acaabc"
    print(countPalindromePaths(parent, s))  # Expected Output: 8

    # Test Case 2
    parent = [-1, 0, 0, 0]
    s = "aabb"
    print(countPalindromePaths(parent, s))  # Expected Output: 6

    # Test Case 3
    parent = [-1, 0, 1, 2]
    s = "abcd"
    print(countPalindromePaths(parent, s))  # Expected Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the tree takes O(n).
- The DFS traversal visits each node once, and for each node, we perform O(26) operations to check masks.
- Thus, the overall time complexity is O(n + 26 * n) = O(n).

Space Complexity:
- The tree representation uses O(n) space.
- The mask_count dictionary can have at most 2^26 entries in the worst case, but in practice, it will be much smaller.
- The recursion stack in DFS can go up to O(n) in the worst case.
- Thus, the overall space complexity is O(n + 2^26) ≈ O(n).

---

Topic: Tree, Bit Manipulation, Depth-First Search (DFS)
"""