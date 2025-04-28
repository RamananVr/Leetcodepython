"""
LeetCode Problem #1273: Delete Tree Nodes

Problem Statement:
You are given a tree with `n` nodes numbered from `0` to `n-1` in the form of an array `parent` where `parent[i]` is the parent of node `i`. The root node is `0`, so `parent[0] = -1`. You are also given an array `value` where `value[i]` is the value of the `i-th` node.

You need to delete every subtree whose sum of values is equal to `0`.

After doing so, return the number of nodes remaining in the tree.

Constraints:
- `1 <= n <= 10^4`
- `parent.length == n`
- `value.length == n`
- `parent[0] == -1`
- The input is guaranteed to form a valid tree.

Example:
Input: parent = [-1,0,0,1,1,2,2], value = [1,-2,4,0,-2,-1,-1]
Output: 2
Explanation: 
    The sum of the values of the subtree of node 1 is -2 + 0 + (-2) = -4, which is not zero.
    The sum of the values of the subtree of node 2 is 4 + (-1) + (-1) = 2, which is not zero.
    The sum of the values of the subtree of node 0 is 1 + (-4) + 2 = -1, which is not zero.
    Therefore, all nodes remain in the tree.

Topic: Tree
"""

from collections import defaultdict

def deleteTreeNodes(n, parent, value):
    # Step 1: Build the tree structure using adjacency list
    tree = defaultdict(list)
    for i in range(n):
        if parent[i] != -1:
            tree[parent[i]].append(i)
    
    # Step 2: Post-order traversal to calculate subtree sums and prune nodes
    def dfs(node):
        subtree_sum = value[node]
        subtree_size = 1  # Count the current node
        for child in tree[node]:
            child_sum, child_size = dfs(child)
            subtree_sum += child_sum
            subtree_size += child_size
        
        # If the subtree sum is zero, prune the subtree
        if subtree_sum == 0:
            subtree_size = 0
        
        return subtree_sum, subtree_size
    
    # Start DFS from the root node (node 0)
    _, remaining_nodes = dfs(0)
    return remaining_nodes

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    parent = [-1, 0, 0, 1, 1, 2, 2]
    value = [1, -2, 4, 0, -2, -1, -1]
    print(deleteTreeNodes(7, parent, value))  # Output: 2

    # Test Case 2
    parent = [-1, 0, 0, 1, 1]
    value = [1, -1, -1, 0, 0]
    print(deleteTreeNodes(5, parent, value))  # Output: 1

    # Test Case 3
    parent = [-1, 0, 0, 1, 1, 2, 2]
    value = [1, 2, -3, 0, 0, 0, 0]
    print(deleteTreeNodes(7, parent, value))  # Output: 7

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the tree takes O(n) time.
- The DFS traversal visits each node exactly once, and for each node, we process its children. 
  Therefore, the DFS traversal also takes O(n) time.
- Overall time complexity: O(n).

Space Complexity:
- The adjacency list representation of the tree takes O(n) space.
- The recursion stack for DFS can go as deep as the height of the tree, which is O(n) in the worst case for a skewed tree.
- Overall space complexity: O(n).

Topic: Tree
"""