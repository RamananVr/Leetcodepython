"""
LeetCode Question #235: Lowest Common Ancestor of a Binary Search Tree

Problem Statement:
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p and q are different and both values will exist in the BST.

Example:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Finds the lowest common ancestor of two nodes in a binary search tree.

    Args:
    root (TreeNode): The root of the binary search tree.
    p (TreeNode): The first node.
    q (TreeNode): The second node.

    Returns:
    TreeNode: The lowest common ancestor of p and q.
    """
    # Traverse the tree starting from the root
    while root:
        # If both p and q are smaller than root, LCA must be in the left subtree
        if p.val < root.val and q.val < root.val:
            root = root.left
        # If both p and q are greater than root, LCA must be in the right subtree
        elif p.val > root.val and q.val > root.val:
            root = root.right
        # If p and q are on opposite sides of root, or one of them equals root, root is the LCA
        else:
            return root
    return None  # This line should never be reached if p and q are guaranteed to exist in the BST

# Example Test Cases
if __name__ == "__main__":
    # Helper function to build a tree from a list
    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        for i, node in enumerate(nodes):
            if node:
                if 2 * i + 1 < len(nodes):
                    node.left = nodes[2 * i + 1]
                if 2 * i + 2 < len(nodes):
                    node.right = nodes[2 * i + 2]
        return nodes[0]

    # Test Case 1
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = root.left  # Node with value 2
    q = root.right  # Node with value 8
    print(lowestCommonAncestor(root, p, q).val)  # Output: 6

    # Test Case 2
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = root.left  # Node with value 2
    q = root.left.right  # Node with value 4
    print(lowestCommonAncestor(root, p, q).val)  # Output: 2

    # Test Case 3
    root = build_tree([2, 1])
    p = root  # Node with value 2
    q = root.left  # Node with value 1
    print(lowestCommonAncestor(root, p, q).val)  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm traverses the tree starting from the root and moves either left or right at each step.
- In the worst case, the traversal will go down the height of the tree.
- For a balanced BST, the height is O(log n), and for a skewed BST, the height is O(n).
- Therefore, the time complexity is O(h), where h is the height of the tree.

Space Complexity:
- The algorithm uses constant space, as it does not use any additional data structures and performs the traversal iteratively.
- Therefore, the space complexity is O(1).

Topic: Binary Tree
"""