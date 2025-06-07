"""
LeetCode Problem #2647: Count Paths That Can Form a Palindrome in a Tree

Problem Statement:
You are given a tree (i.e., a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.

You are given a 2D integer array edges, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi. You are also given an array colors, where colors[i] is the color of node i.

Find the number of paths in the tree such that there is no node that appears in the path more than once (i.e., simple paths) and the sequence of colors of the nodes in the path can be rearranged to form a palindrome.

Return the number of such paths.

A palindrome is a string that reads the same forward and backward.

Example 1:
Input: edges = [[0,1],[1,2],[2,3],[3,4]], colors = "abcda"
Output: 6
Explanation:
The paths that can form a palindrome are:
- Node 0: "a" (always palindrome)
- Node 1: "b" (always palindrome)  
- Node 2: "c" (always palindrome)
- Node 3: "d" (always palindrome)
- Node 4: "a" (always palindrome)
- Path [0,1,2,3,4]: "abcda" can be rearranged to "acbca"

Example 2:
Input: edges = [[0,1],[1,2],[1,3]], colors = "aabc"
Output: 8
Explanation:
The paths that can form a palindrome are:
- Single nodes: 4 paths
- Path [0,1]: "aa" 
- Path [1,2]: "ab" cannot form palindrome
- Path [1,3]: "ac" cannot form palindrome
- Path [0,1,2]: "aab" can be rearranged to "aba"
- Path [0,1,3]: "aac" can be rearranged to "aca"

Constraints:
- n == colors.length
- 1 <= n <= 10^5
- edges.length == n - 1
- edges[i].length == 2
- 0 <= ui, vi <= n - 1
- colors is a string consisting of lowercase English letters.
"""

from collections import defaultdict
from typing import List

def countPalindromePaths(edges: List[List[int]], colors: str) -> int:
    """
    Approach using DFS and bitmask:
    1. For a path to form palindrome, at most one character can have odd frequency
    2. Use bitmask to represent character frequencies (odd/even)
    3. For each node, compute paths ending at that node
    4. Two paths can be combined if their XOR has at most 1 bit set
    """
    n = len(colors)
    if n == 1:
        return 1
    
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    result = 0
    
    def dfs(node: int, parent: int, mask: int, depth: int):
        nonlocal result
        
        # Current character bitmask
        char_bit = 1 << (ord(colors[node]) - ord('a'))
        mask ^= char_bit
        
        # Count single node paths (always palindromes)
        if parent == -1:  # Root node
            result += 1
        
        # For paths ending at current node
        # Check paths that can form palindrome with current path
        path_masks = []
        
        def collect_paths(curr: int, par: int, curr_mask: int):
            nonlocal result
            
            if curr != node:  # Don't count starting node again
                # Check if curr_mask ^ mask can form palindrome
                # (at most 1 bit set in XOR)
                xor_mask = curr_mask ^ mask
                if bin(xor_mask).count('1') <= 1:
                    result += 1
            
            for neighbor in graph[curr]:
                if neighbor != par and neighbor != node:  # Don't go back to starting node
                    neighbor_bit = 1 << (ord(colors[neighbor]) - ord('a'))
                    collect_paths(neighbor, curr, curr_mask ^ neighbor_bit)
        
        # Check paths from other subtrees
        for neighbor in graph[node]:
            if neighbor != parent:
                neighbor_bit = 1 << (ord(colors[neighbor]) - ord('a'))
                collect_paths(neighbor, node, neighbor_bit)
        
        # Continue DFS
        for neighbor in graph[node]:
            if neighbor != parent:
                dfs(neighbor, node, mask, depth + 1)
    
    dfs(0, -1, 0, 0)
    return result

def countPalindromePathsOptimized(edges: List[List[int]], colors: str) -> int:
    """
    Optimized approach using centroid decomposition concept
    """
    n = len(colors)
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    result = n  # All single nodes are palindromes
    
    def dfs_paths(start: int):
        nonlocal result
        visited = set()
        
        def dfs(node: int, mask: int, depth: int):
            if node in visited:
                return
            visited.add(node)
            
            if depth > 0:  # Not the starting node
                # Check if current mask can form palindrome
                if bin(mask).count('1') <= 1:
                    result += 1
                
                # Check if mask with one bit flipped can form palindrome
                for i in range(26):
                    if mask ^ (1 << i) in mask_counts:
                        result += mask_counts[mask ^ (1 << i)]
            
            if depth > 0:
                mask_counts[mask] = mask_counts.get(mask, 0) + 1
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    char_bit = 1 << (ord(colors[neighbor]) - ord('a'))
                    dfs(neighbor, mask ^ char_bit, depth + 1)
        
        mask_counts = {}
        char_bit = 1 << (ord(colors[start]) - ord('a'))
        dfs(start, char_bit, 0)
    
    for i in range(n):
        dfs_paths(i)
    
    return result // 2  # Each path counted twice

def countPalindromePathsCorrect(edges: List[List[int]], colors: str) -> int:
    """
    Correct approach using DFS and bitmask counting
    """
    n = len(colors)
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    result = 0
    
    def dfs(node: int, parent: int):
        nonlocal result
        
        # Count paths starting from this node
        mask_count = defaultdict(int)
        mask_count[0] = 1  # Empty path
        
        for neighbor in graph[node]:
            if neighbor != parent:
                neighbor_masks = defaultdict(int)
                
                def collect_masks(curr: int, par: int, mask: int):
                    char_bit = 1 << (ord(colors[curr]) - ord('a'))
                    mask ^= char_bit
                    neighbor_masks[mask] += 1
                    
                    for next_node in graph[curr]:
                        if next_node != par:
                            collect_masks(next_node, curr, mask)
                
                collect_masks(neighbor, node, 0)
                
                # Count valid pairs with existing masks
                for mask in neighbor_masks:
                    # Check if mask can form palindrome with existing masks
                    if mask in mask_count:
                        result += neighbor_masks[mask] * mask_count[mask]
                    
                    # Check if mask with one bit flipped exists
                    for i in range(26):
                        flipped = mask ^ (1 << i)
                        if flipped in mask_count:
                            result += neighbor_masks[mask] * mask_count[flipped]
                
                # Add neighbor masks to current count
                for mask in neighbor_masks:
                    mask_count[mask] += neighbor_masks[mask]
        
        # Continue DFS for subtrees
        for neighbor in graph[node]:
            if neighbor != parent:
                dfs(neighbor, node)
    
    dfs(0, -1)
    return result + n  # Add single node paths

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    edges1 = [[0,1],[1,2],[2,3],[3,4]]
    colors1 = "abcda"
    print(f"Test Case 1: {countPalindromePathsCorrect(edges1, colors1)}")  # Expected: 6
    
    # Test Case 2
    edges2 = [[0,1],[1,2],[1,3]]
    colors2 = "aabc"
    print(f"Test Case 2: {countPalindromePathsCorrect(edges2, colors2)}")  # Expected: 8
    
    # Test Case 3: Single node
    edges3 = []
    colors3 = "a"
    print(f"Test Case 3: {countPalindromePathsCorrect(edges3, colors3)}")  # Expected: 1
    
    # Test Case 4: All same color
    edges4 = [[0,1],[1,2]]
    colors4 = "aaa"
    print(f"Test Case 4: {countPalindromePathsCorrect(edges4, colors4)}")  # Expected: 6
    
    # Test Case 5: Binary tree
    edges5 = [[0,1],[0,2],[1,3],[1,4]]
    colors5 = "abcde"
    print(f"Test Case 5: {countPalindromePathsCorrect(edges5, colors5)}")  # Expected: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- DFS traversal: O(n)
- For each node, we may traverse all paths in subtree: O(n^2) in worst case
- Bitmask operations: O(26) = O(1) for each comparison
- Overall: O(n^2)

Space Complexity:
- Graph adjacency list: O(n)
- Recursion stack: O(n)
- Mask counting dictionaries: O(n) per node
- Overall: O(n^2)

Topic: Tree, DFS, Bit Manipulation, Palindrome
"""
