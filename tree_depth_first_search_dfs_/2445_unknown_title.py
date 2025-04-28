"""
LeetCode Problem #2445: Number of Nodes in the Sub-Tree With the Same Label

Problem Statement:
You are given a tree (i.e., a connected, undirected graph that has no cycles) consisting of `n` nodes numbered from `0` to `n - 1` and exactly `n - 1` edges. The root of the tree is the node `0`, and each node has a label represented by a string `labels` (of length `n`), where `labels[i]` is the label of the `i-th` node.

The tree is represented by a 2D array `edges` of size `n - 1`, where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the tree.

Return an array `result` of size `n` where `result[i]` is the number of nodes in the subtree of the `i-th` node that have the same label as node `i`.

Example:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
Output: [2,1,1,1,1,1,1]

Constraints:
- `1 <= n <= 10^5`
- `edges.length == n - 1`
- `0 <= ai, bi < n`
- `ai != bi`
- `labels.length == n`
- `labels` consists of only lowercase English letters.

"""

# Solution
from collections import defaultdict

def countSubTrees(n, edges, labels):
    # Build adjacency list for the tree
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # Result array to store the count for each node
    result = [0] * n
    
    # Helper function for DFS traversal
    def dfs(node, parent):
        # Frequency map for labels in the subtree
        freq = defaultdict(int)
        
        # Count the current node's label
        freq[labels[node]] += 1
        
        # Traverse children
        for child in tree[node]:
            if child != parent:  # Avoid revisiting the parent node
                child_freq = dfs(child, node)
                # Merge child frequencies into the current node's frequency map
                for label, count in child_freq.items():
                    freq[label] += count
        
        # Update the result for the current node
        result[node] = freq[labels[node]]
        
        return freq
    
    # Start DFS from the root node (0)
    dfs(0, -1)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 7
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    labels = "abaedcd"
    print(countSubTrees(n, edges, labels))  # Output: [2,1,1,1,1,1,1]

    # Test Case 2
    n = 4
    edges = [[0,1],[1,2],[0,3]]
    labels = "bbbb"
    print(countSubTrees(n, edges, labels))  # Output: [4,3,1,1]

    # Test Case 3
    n = 5
    edges = [[0,1],[0,2],[1,3],[0,4]]
    labels = "aabab"
    print(countSubTrees(n, edges, labels))  # Output: [3,2,1,1,1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the adjacency list takes O(n) since there are `n-1` edges.
- The DFS traversal visits each node once and processes its children, resulting in O(n) time complexity.
- Merging frequency maps during DFS is proportional to the number of unique labels, which is constant (26 lowercase English letters). Thus, this step is O(1) per node.
- Overall time complexity: O(n).

Space Complexity:
- The adjacency list requires O(n) space.
- The frequency map used during DFS is O(1) (constant space for 26 labels).
- The recursion stack for DFS can go up to O(n) in the worst case (tree height).
- Result array requires O(n) space.
- Overall space complexity: O(n).

Topic: Tree, Depth-First Search (DFS)
"""