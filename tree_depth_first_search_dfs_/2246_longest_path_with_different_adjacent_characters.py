"""
LeetCode Question #2246: Longest Path With Different Adjacent Characters

Problem Statement:
You are given a tree (i.e., a connected, undirected graph with no cycles) rooted at node 0 consisting of `n` nodes numbered from `0` to `n - 1`. The tree is represented by a 0-indexed array `parent` of size `n`, where `parent[i]` is the parent of node `i`. Since node `0` is the root, `parent[0] == -1`.

You are also given a string `s` of length `n`, where `s[i]` is the character assigned to node `i`.

Return the length of the longest path in the tree such that no two adjacent nodes on the path have the same character.

Example 1:
Input: parent = [-1, 0, 0, 1, 1, 2], s = "abacbe"
Output: 3
Explanation: The longest path is "abc" (nodes 0 -> 1 -> 3).

Example 2:
Input: parent = [-1, 0, 0, 0], s = "aabc"
Output: 3
Explanation: The longest path is "abc" (nodes 0 -> 2 -> 3).

Constraints:
- `n == parent.length == s.length`
- `1 <= n <= 10^5`
- `0 <= parent[i] <= n - 1` for all `i >= 1`
- `parent[0] == -1`
- `s` consists of only lowercase English letters.
"""

# Python Solution
from collections import defaultdict

def longestPath(parent, s):
    def dfs(node):
        nonlocal max_path
        max1, max2 = 0, 0  # Top two longest paths from the current node
        
        for child in tree[node]:
            child_length = dfs(child)
            if s[child] != s[node]:  # Only consider paths with different adjacent characters
                if child_length > max1:
                    max2 = max1
                    max1 = child_length
                elif child_length > max2:
                    max2 = child_length
        
        # Update the global maximum path length
        max_path = max(max_path, max1 + max2 + 1)
        
        return max1 + 1

    # Build the tree as an adjacency list
    tree = defaultdict(list)
    for i, p in enumerate(parent):
        if p != -1:
            tree[p].append(i)
    
    max_path = 0
    dfs(0)  # Start DFS from the root node (0)
    return max_path

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    parent = [-1, 0, 0, 1, 1, 2]
    s = "abacbe"
    print(longestPath(parent, s))  # Output: 3

    # Test Case 2
    parent = [-1, 0, 0, 0]
    s = "aabc"
    print(longestPath(parent, s))  # Output: 3

    # Test Case 3
    parent = [-1, 0, 1, 2, 3]
    s = "abcde"
    print(longestPath(parent, s))  # Output: 5

    # Test Case 4
    parent = [-1, 0, 0, 1, 1, 2, 2]
    s = "aaaaaaa"
    print(longestPath(parent, s))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm performs a single DFS traversal of the tree, visiting each node exactly once.
- Building the adjacency list also takes O(n) time.
- Therefore, the overall time complexity is O(n), where n is the number of nodes.

Space Complexity:
- The adjacency list `tree` requires O(n) space.
- The recursion stack for DFS can go as deep as O(n) in the worst case (e.g., a skewed tree).
- Thus, the overall space complexity is O(n).

Topic: Tree, Depth-First Search (DFS)
"""