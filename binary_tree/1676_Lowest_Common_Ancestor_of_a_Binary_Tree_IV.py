"""
LeetCode Problem #1676: Lowest Common Ancestor of a Binary Tree IV

Problem Statement:
Given the `root` of a binary tree and an array of `TreeNode` objects called `nodes`, 
return the lowest common ancestor (LCA) of all the nodes in `nodes`. All the nodes 
will exist in the tree, and the tree is not necessarily a binary search tree.

The lowest common ancestor of a set of nodes is the lowest node in the tree that has 
all the nodes as descendants (where we allow a node to be a descendant of itself).

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^9 <= Node.val <= 10^9
- All `Node.val` are unique.
- All `nodes[i]` will exist in the tree.
- The number of nodes in `nodes` is in the range [1, 10^4].

Example:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
Output: 2
Explanation: The lowest common ancestor of nodes 4 and 7 is 2.

Follow-up:
Can you solve the problem in O(n) time complexity, where n is the number of nodes in the tree?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, nodes: list[TreeNode]) -> TreeNode:
        # Convert the list of nodes into a set for quick lookup
        node_set = set(nodes)
        
        def dfs(node):
            if not node:
                return None
            # If the current node is in the set, return it
            if node in node_set:
                return node
            
            # Recur for left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If both left and right are not None, this node is the LCA
            if left and right:
                return node
            
            # Otherwise, return the non-None child (if any)
            return left if left else right
        
        return dfs(root)

# Example Test Cases
if __name__ == "__main__":
    # Helper function to build a binary tree from a list
    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    # Test Case 1
    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    nodes = [TreeNode(4), TreeNode(7)]
    solution = Solution()
    lca = solution.lowestCommonAncestor(root, nodes)
    print(f"Test Case 1: {lca.val}")  # Expected Output: 2

    # Test Case 2
    root = build_tree([1, 2])
    nodes = [TreeNode(1), TreeNode(2)]
    lca = solution.lowestCommonAncestor(root, nodes)
    print(f"Test Case 2: {lca.val}")  # Expected Output: 1

"""
Time Complexity:
- The algorithm performs a single traversal of the binary tree, visiting each node once.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack, which in the worst case 
  (for a skewed tree) can go up to O(h), where h is the height of the tree.
- In the average case for a balanced tree, the space complexity is O(log n).

Topic: Binary Tree
"""