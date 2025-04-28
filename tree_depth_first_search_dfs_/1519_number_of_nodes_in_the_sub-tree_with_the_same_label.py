"""
LeetCode Question #1519: Number of Nodes in the Sub-Tree With the Same Label

Problem Statement:
You are given a tree (i.e., a connected, undirected graph that has no cycles) consisting of `n` nodes numbered from `0` to `n - 1` and exactly `n - 1` edges. The root of the tree is the node `0`, and each node has a label represented by a lowercase English letter. The `labels` array is a string of length `n` where `labels[i]` is the label of the `i-th` node in the tree.

The tree is represented by a 2D array `edges` of size `n - 1`, where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the tree.

Return an array of size `n` where `ans[i]` is the number of nodes in the subtree of the `i-th` node which have the same label as node `i`.

Example 1:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
Output: [2,1,1,1,1,1,1]

Example 2:
Input: n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"
Output: [4,2,1,1]

Example 3:
Input: n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"
Output: [3,2,1,1,1]

Constraints:
- `1 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= ai, bi < n`
- `labels.length == n`
- `labels` contains only lowercase English letters.
"""

from collections import defaultdict

def countSubTrees(n, edges, labels):
    # Build the adjacency list for the tree
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # Result array to store the count for each node
    result = [0] * n
    
    # Helper function for DFS traversal
    def dfs(node, parent):
        # Frequency map for labels in the subtree rooted at `node`
        label_count = defaultdict(int)
        
        # Increment the count for the current node's label
        label_count[labels[node]] += 1
        
        # Traverse all children (neighbors) of the current node
        for neighbor in tree[node]:
            if neighbor != parent:  # Avoid revisiting the parent node
                child_count = dfs(neighbor, node)
                # Merge the child's label counts into the current node's label count
                for label, count in child_count.items():
                    label_count[label] += count
        
        # Update the result for the current node
        result[node] = label_count[labels[node]]
        
        return label_count
    
    # Start DFS from the root node (0) with no parent (-1)
    dfs(0, -1)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 7
    edges1 = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    labels1 = "abaedcd"
    print(countSubTrees(n1, edges1, labels1))  # Output: [2,1,1,1,1,1,1]

    # Test Case 2
    n2 = 4
    edges2 = [[0,1],[1,2],[0,3]]
    labels2 = "bbbb"
    print(countSubTrees(n2, edges2, labels2))  # Output: [4,2,1,1]

    # Test Case 3
    n3 = 5
    edges3 = [[0,1],[0,2],[1,3],[0,4]]
    labels3 = "aabab"
    print(countSubTrees(n3, edges3, labels3))  # Output: [3,2,1,1,1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the adjacency list takes O(n) since there are `n-1` edges.
- The DFS traversal visits each node once and processes its neighbors, resulting in O(n) time complexity.
- Overall, the time complexity is O(n).

Space Complexity:
- The adjacency list requires O(n) space.
- The result array requires O(n) space.
- The label_count dictionary used during DFS requires O(26) space (constant space for lowercase English letters).
- The recursion stack in the worst case requires O(n) space.
- Overall, the space complexity is O(n).

Topic: Tree, Depth-First Search (DFS)
"""