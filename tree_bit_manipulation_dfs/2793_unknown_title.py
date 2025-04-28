"""
LeetCode Problem #2793: Count Paths That Can Form a Palindrome in a Tree

Problem Statement:
You are given a tree (an undirected graph with no cycles) consisting of `n` nodes numbered from `0` to `n-1`, and an array `parent` of size `n` where `parent[i]` is the parent of node `i`. The tree is rooted at node `0`.

You are also given a string `s` of length `n` where `s[i]` is the character assigned to node `i`.

A path in the tree is a sequence of nodes starting at some node and ending at another node, such that every adjacent pair of nodes in the sequence is connected by an edge in the tree.

A path is said to "form a palindrome" if the characters assigned to the nodes in the path can be rearranged to form a palindrome.

Return the number of paths in the tree that can form a palindrome.

Constraints:
- `1 <= n <= 10^5`
- `parent.length == n`
- `parent[0] == -1` (indicating that node `0` is the root)
- `0 <= parent[i] <= n-1` for all `i > 0`
- `s.length == n`
- `s` consists of lowercase English letters.

"""

from collections import defaultdict, Counter

def countPalindromePaths(parent, s):
    """
    Function to count the number of paths in the tree that can form a palindrome.

    :param parent: List[int], parent array representing the tree structure
    :param s: str, string of characters assigned to the nodes
    :return: int, number of paths that can form a palindrome
    """
    # Step 1: Build the adjacency list for the tree
    n = len(parent)
    tree = defaultdict(list)
    for i in range(1, n):
        tree[parent[i]].append(i)
        tree[i].append(parent[i])

    # Step 2: Perform DFS to calculate the "parity mask" for each node
    def dfs(node, mask, visited):
        visited.add(node)
        mask ^= 1 << (ord(s[node]) - ord('a'))  # Update the mask for the current node
        masks[node] = mask
        for neighbor in tree[node]:
            if neighbor not in visited:
                dfs(neighbor, mask, visited)

    masks = {}
    visited = set()
    dfs(0, 0, visited)

    # Step 3: Count the number of valid paths using the masks
    mask_count = Counter()
    mask_count[0] = 1  # Base case: empty path
    result = 0

    for mask in masks.values():
        # Case 1: Check if the current mask itself can form a palindrome
        result += mask_count[mask]

        # Case 2: Check if flipping one bit in the mask can form a palindrome
        for i in range(26):  # There are 26 lowercase English letters
            flipped_mask = mask ^ (1 << i)
            result += mask_count[flipped_mask]

        # Update the mask count
        mask_count[mask] += 1

    return result


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    parent = [-1, 0, 0, 1, 1, 2]
    s = "abacbe"
    print(countPalindromePaths(parent, s))  # Expected Output: 7

    # Test Case 2
    parent = [-1, 0, 1, 2]
    s = "aaaa"
    print(countPalindromePaths(parent, s))  # Expected Output: 10

    # Test Case 3
    parent = [-1, 0, 0, 0]
    s = "abcd"
    print(countPalindromePaths(parent, s))  # Expected Output: 4


"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the adjacency list takes O(n).
- The DFS traversal takes O(n) since we visit each node once.
- For each node, we perform up to 26 checks for flipped masks, resulting in O(26 * n) = O(n).
- Overall time complexity: O(n).

Space Complexity:
- The adjacency list takes O(n) space.
- The masks dictionary takes O(n) space.
- The mask_count Counter takes O(n) space in the worst case.
- Overall space complexity: O(n).

Topic: Tree, Bit Manipulation, DFS
"""