"""
LeetCode Question #94: Binary Tree Inorder Traversal

Problem Statement:
Given the root of a binary tree, return the inorder traversal of its nodes' values.

In an inorder traversal, the nodes are recursively visited in this order:
1. Left subtree
2. Root node
3. Right subtree

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

Follow-up:
Recursive solution is straightforward. Could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution: Recursive Inorder Traversal
def inorderTraversal(root):
    """
    Perform an inorder traversal of a binary tree.

    :param root: TreeNode, the root of the binary tree
    :return: List[int], the inorder traversal of the tree
    """
    def helper(node, result):
        if not node:
            return
        # Traverse the left subtree
        helper(node.left, result)
        # Visit the root node
        result.append(node.val)
        # Traverse the right subtree
        helper(node.right, result)
    
    result = []
    helper(root, result)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    print(inorderTraversal(root1))  # Output: [1, 3, 2]

    # Example 2
    root2 = None
    print(inorderTraversal(root2))  # Output: []

    # Example 3
    root3 = TreeNode(1)
    print(inorderTraversal(root3))  # Output: [1]

    # Example 4
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    print(inorderTraversal(root4))  # Output: [2, 1, 3]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each node in the binary tree is visited exactly once.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- In the worst case, the recursion stack can go as deep as the height of the tree.
- For a balanced binary tree, the height is O(log n), and for a skewed tree, the height is O(n).
- Additionally, we use a list to store the result, which takes O(n) space.
- Overall space complexity is O(n).

Topic: Binary Tree
"""