"""
2791. Count Paths That Can Form a Palindrome in a Tree

Problem Statement:
You are given a tree (i.e., a connected, undirected graph with no cycles) rooted at node 0 
consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array 
parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, 
parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

Return the number of pairs of nodes (u, v) such that u < v and the concatenation of characters 
assigned to nodes on the path from u to v can be rearranged to form a palindrome.

Constraints:
- n == parent.length == s.length
- 1 <= n <= 10^5
- 0 <= parent[i] <= n - 1 for all i >= 1
- parent[0] == -1
- s consists of only lowercase English letters.

Test Cases:
1. Input: parent = [-1,0,0,1,1,2], s = "acaabc"
   Output: 8
   
2. Input: parent = [-1,0,0,0], s = "aabc"
   Output: 6
"""

from collections import defaultdict, deque
from typing import List

def countPalindromePaths(parent: List[int], s: str) -> int:
    """
    Count paths that can form a palindrome in a tree.
    
    Algorithm:
    1. Build the tree from parent array
    2. For each node, compute the bitmask representing character frequency from root
    3. Use DFS to traverse and count palindromic paths
    4. A path can form palindrome if at most one character has odd frequency
    
    Time Complexity: O(n * 26) = O(n)
    Space Complexity: O(n)
    """
    n = len(parent)
    if n <= 1:
        return 0
    
    # Build adjacency list
    graph = defaultdict(list)
    for i in range(1, n):
        graph[parent[i]].append(i)
        graph[i].append(parent[i])
    
    # For each node, store bitmask of character frequencies from root
    masks = [0] * n
    visited = [False] * n
    result = 0
    
    def dfs(node, parent_node, mask):
        nonlocal result
        
        # Update mask for current character
        char_bit = 1 << (ord(s[node]) - ord('a'))
        mask ^= char_bit
        masks[node] = mask
        
        # Count nodes with compatible masks seen so far
        # Compatible means: same mask (even frequencies) or differ by one bit (one odd frequency)
        
        # Count paths ending at current node
        for prev_node in range(node):
            if visited[prev_node]:
                prev_mask = masks[prev_node]
                # Check if path from prev_node to current node can form palindrome
                path_mask = prev_mask ^ mask
                
                # Can form palindrome if at most one character has odd frequency
                if bin(path_mask).count('1') <= 1:
                    result += 1
        
        visited[node] = True
        
        # Continue DFS to children
        for child in graph[node]:
            if child != parent_node:
                dfs(child, node, mask)
    
    dfs(0, -1, 0)
    return result

def countPalindromePathsOptimized(parent: List[int], s: str) -> int:
    """
    Optimized solution using frequency counting of masks.
    
    Time Complexity: O(n * 26) = O(n)
    Space Complexity: O(n)
    """
    n = len(parent)
    if n <= 1:
        return 0
    
    # Build adjacency list
    graph = defaultdict(list)
    for i in range(1, n):
        graph[parent[i]].append(i)
        graph[i].append(parent[i])
    
    result = 0
    mask_count = defaultdict(int)
    
    def dfs(node, parent_node, mask):
        nonlocal result
        
        # Update mask for current character
        char_bit = 1 << (ord(s[node]) - ord('a'))
        mask ^= char_bit
        
        # Count palindromic paths ending at current node
        # 1. Paths with even character frequencies (same mask)
        result += mask_count[mask]
        
        # 2. Paths with exactly one odd character frequency
        for i in range(26):
            target_mask = mask ^ (1 << i)
            result += mask_count[target_mask]
        
        # Add current mask to count
        mask_count[mask] += 1
        
        # Continue DFS to children
        for child in graph[node]:
            if child != parent_node:
                dfs(child, node, mask)
        
        # Remove current mask when backtracking
        mask_count[mask] -= 1
    
    dfs(0, -1, 0)
    return result

# Test cases
def test_count_palindrome_paths():
    # Test case 1
    parent1 = [-1, 0, 0, 1, 1, 2]
    s1 = "acaabc"
    result1 = countPalindromePathsOptimized(parent1, s1)
    print(f"Test 1 - Expected: 8, Got: {result1}")
    
    # Test case 2
    parent2 = [-1, 0, 0, 0]
    s2 = "aabc"
    result2 = countPalindromePathsOptimized(parent2, s2)
    print(f"Test 2 - Expected: 6, Got: {result2}")
    
    # Test case 3: Single node
    parent3 = [-1]
    s3 = "a"
    result3 = countPalindromePathsOptimized(parent3, s3)
    print(f"Test 3 - Expected: 0, Got: {result3}")

if __name__ == "__main__":
    test_count_palindrome_paths()

"""
Topic Classification: Arrays, Hash Table, Tree, DFS, Bit Manipulation

Key Insights:
1. Use bitmask to represent character frequency parity
2. Two nodes can form palindromic path if their masks differ by at most one bit
3. DFS traversal with frequency counting of masks for efficiency
4. Backtracking to avoid double counting

Complexity Analysis:
- Time Complexity: O(n * 26) = O(n), where n is number of nodes
- Space Complexity: O(n) for recursion stack and hash table
"""
