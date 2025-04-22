"""
LeetCode Question #236: Lowest Common Ancestor of a Binary Tree

Problem Statement:
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
"The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself)."

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the tree.

Example:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Input: root = [1,2], p = 1, q = 2
Output: 1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        This function finds the lowest common ancestor of two nodes in a binary tree.
        """
        # Base case: if the current node is None, p, or q, return the current node
        if not root or root == p or root == q:
            return root
        
        # Recur for the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right are non-null, the current node is the LCA
        if left and right:
            return root
        
        # Otherwise, return the non-null child (either left or right)
        return left if left else right

# Example Test Cases
def test_lowest_common_ancestor():
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
    root = build_tree([3,5,1,6,2,0,8,None,None,7,4])
    p = root.left  # Node with value 5
    q = root.right  # Node with value 1
    assert Solution().lowestCommonAncestor(root, p, q).val == 3

    # Test Case 2
    root = build_tree([3,5,1,6,2,0,8,None,None,7,4])
    p = root.left  # Node with value 5
    q = root.left.right.right  # Node with value 4
    assert Solution().lowestCommonAncestor(root, p, q).val == 5

    # Test Case 3
    root = build_tree([1,2])
    p = root  # Node with value 1
    q = root.left  # Node with value 2
    assert Solution().lowestCommonAncestor(root, p, q).val == 1

    print("All test cases passed!")

# Run the test cases
test_lowest_common_ancestor()

"""
Time Complexity:
- The time complexity is O(N), where N is the number of nodes in the binary tree.
  This is because, in the worst case, we may need to visit all nodes in the tree.

Space Complexity:
- The space complexity is O(H), where H is the height of the binary tree.
  This is due to the recursive call stack, which can go as deep as the height of the tree.
  In the worst case (skewed tree), H = N. In the best case (balanced tree), H = log(N).

Topic: Binary Tree
"""