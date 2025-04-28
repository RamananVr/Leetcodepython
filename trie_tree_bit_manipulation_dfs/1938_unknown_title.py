"""
LeetCode Problem #1938: Maximum Genetic Difference Query

Problem Statement:
There is a rooted tree consisting of `n` nodes numbered `0` to `n - 1`. Each node's number represents its genetic value. The tree is given as a 2D array `edges` where `edges[i] = [parent_i, child_i]` indicates that `parent_i` is the parent of `child_i`.

You are also given an array `queries` where `queries[j] = [node_j, val_j]`. For each query `j`, you need to find the maximum genetic difference between `val_j` and any node's genetic value in the subtree of `node_j`. The maximum genetic difference is defined as the bitwise XOR between two values.

Return an array `ans` where `ans[j]` is the answer to the `j`th query.

Constraints:
- `2 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= parent_i, child_i < n`
- `0 <= val_j < 2^20`
- `1 <= queries.length <= 3 * 10^4`
- `queries[j].length == 2`
- `0 <= node_j < n`

The input is guaranteed to be valid.

---

Solution:
The problem can be solved efficiently using a Trie data structure to store the genetic values of nodes in the subtree. The Trie allows us to compute the maximum XOR efficiently for each query.

"""

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0  # Tracks how many numbers are in the subtree of this Trie node

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root
        for i in range(19, -1, -1):  # Traverse bits from 19 to 0
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            node.count += 1
    
    def remove(self, num):
        node = self.root
        for i in range(19, -1, -1):
            bit = (num >> i) & 1
            node = node.children[bit]
            node.count -= 1
    
    def max_xor(self, num):
        node = self.root
        xor_sum = 0
        for i in range(19, -1, -1):
            bit = (num >> i) & 1
            # Try to take the opposite bit for maximum XOR
            opposite_bit = 1 - bit
            if opposite_bit in node.children and node.children[opposite_bit].count > 0:
                xor_sum |= (1 << i)
                node = node.children[opposite_bit]
            else:
                node = node.children[bit]
        return xor_sum

def maxGeneticDifference(parents, queries):
    # Step 1: Build the tree
    tree = defaultdict(list)
    root = -1
    for child, parent in enumerate(parents):
        if parent == -1:
            root = child
        else:
            tree[parent].append(child)
    
    # Step 2: Group queries by node
    query_map = defaultdict(list)
    for i, (node, val) in enumerate(queries):
        query_map[node].append((val, i))
    
    # Step 3: DFS and process queries using Trie
    trie = Trie()
    result = [0] * len(queries)
    
    def dfs(node):
        # Add the current node's genetic value to the Trie
        trie.insert(node)
        
        # Process all queries for the current node
        for val, idx in query_map[node]:
            result[idx] = trie.max_xor(val)
        
        # Recurse for all children
        for child in tree[node]:
            dfs(child)
        
        # Remove the current node's genetic value from the Trie
        trie.remove(node)
    
    dfs(root)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    parents = [-1, 0, 0, 1, 1, 2]
    queries = [[0, 2], [3, 3], [2, 5]]
    print(maxGeneticDifference(parents, queries))  # Output: [2, 3, 7]

    # Test Case 2
    parents = [-1, 0, 1, 1]
    queries = [[1, 4], [2, 7], [3, 2]]
    print(maxGeneticDifference(parents, queries))  # Output: [5, 6, 3]

"""
Time Complexity:
- Building the tree: O(n)
- Processing queries: O(Q * 20) = O(Q), where Q is the number of queries
- DFS traversal: O(n * 20) = O(n)
Overall: O(n + Q)

Space Complexity:
- Trie storage: O(n * 20) = O(n)
- Tree and query storage: O(n + Q)
Overall: O(n + Q)

Topic: Trie, Tree, Bit Manipulation, DFS
"""