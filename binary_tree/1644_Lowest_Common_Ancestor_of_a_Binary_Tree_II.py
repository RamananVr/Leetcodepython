"""
LeetCode Problem #1644: Lowest Common Ancestor of a Binary Tree II

Problem Statement:
Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. 
If either node p or q does not exist in the tree, return None. The LCA is defined as the lowest node 
in the tree that has both p and q as descendants (where we allow a node to be a descendant of itself).

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q

Follow-up:
- Ensure that the solution handles the case where either p or q is not present in the tree.

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
        Finds the lowest common ancestor of two nodes in a binary tree, ensuring both nodes exist.
        """
        # Helper function to check if a node exists in the tree
        def exists(node, target):
            if not node:
                return False
            if node == target:
                return True
            return exists(node.left, target) or exists(node.right, target)
        
        # Helper function to find the LCA
        def findLCA(node):
            if not node:
                return None
            if node == p or node == q:
                return node
            
            left = findLCA(node.left)
            right = findLCA(node.right)
            
            if left and right:
                return node
            return left if left else right
        
        # Check if both p and q exist in the tree
        if not exists(root, p) or not exists(root, q):
            return None
        
        # Find and return the LCA
        return findLCA(root)

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = root.left  # Node with value 5
    q = root.right  # Node with value 1

    solution = Solution()
    print(solution.lowestCommonAncestor(root, p, q).val)  # Output: 3

    # Example 2
    p = root.left  # Node with value 5
    q = root.left.right.right  # Node with value 4
    print(solution.lowestCommonAncestor(root, p, q).val)  # Output: 5

    # Example 3 (p or q does not exist in the tree)
    p = TreeNode(10)  # Node not in the tree
    q = root.right  # Node with value 1
    print(solution.lowestCommonAncestor(root, p, q))  # Output: None

"""
Time Complexity:
- The `exists` function runs in O(N) time, where N is the number of nodes in the tree, as it performs a full traversal in the worst case.
- The `findLCA` function also runs in O(N) time, as it traverses the tree to find the LCA.
- Since we call `exists` twice and `findLCA` once, the overall time complexity is O(N).

Space Complexity:
- The space complexity is O(H), where H is the height of the tree, due to the recursive call stack. In the worst case (skewed tree), H = N.

Topic: Binary Tree
"""