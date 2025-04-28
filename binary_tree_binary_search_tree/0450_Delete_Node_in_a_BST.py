"""
LeetCode Problem #450: Delete Node in a BST

Problem Statement:
Given a root node reference of a BST (Binary Search Tree) and a key, delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.

The deletion can be divided into three cases:
1. Node to be deleted is a leaf node (no children).
2. Node to be deleted has only one child.
3. Node to be deleted has two children:
   - Replace the node with its in-order successor (smallest node in the right subtree).

Note:
- The BST property must be maintained after deletion.
- It is guaranteed that the key exists in the BST.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5
- Each node has a unique value.
"""

# Python Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        # Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node to be deleted found
            # Case 1: Node has no children
            if not root.left and not root.right:
                return None
            # Case 2: Node has only one child
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Case 3: Node has two children
            else:
                # Find the in-order successor (smallest node in the right subtree)
                successor = self.findMin(root.right)
                # Replace the current node's value with the successor's value
                root.val = successor.val
                # Delete the successor node from the right subtree
                root.right = self.deleteNode(root.right, successor.val)
        
        return root

    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node

# Example Test Cases
def print_inorder(root):
    """Helper function to print the tree in-order."""
    if not root:
        return []
    return print_inorder(root.left) + [root.val] + print_inorder(root.right)

if __name__ == "__main__":
    # Example 1
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    key = 3

    solution = Solution()
    new_root = solution.deleteNode(root, key)
    print("In-order traversal after deletion:", print_inorder(new_root))  # Output: [2, 4, 5, 6, 7]

    # Example 2
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    key = 5

    new_root = solution.deleteNode(root, key)
    print("In-order traversal after deletion:", print_inorder(new_root))  # Output: [2, 3, 4, 6, 7]

# Time and Space Complexity Analysis
# Time Complexity:
# - In the worst case, we traverse the height of the tree to find the node to delete, which is O(h), where h is the height of the tree.
# - For a balanced BST, h = O(log n), and for a skewed BST, h = O(n).
# - Finding the in-order successor and deleting it also takes O(h).
# - Overall time complexity: O(h).

# Space Complexity:
# - The space complexity is O(h) due to the recursive call stack, where h is the height of the tree.
# - For a balanced BST, h = O(log n), and for a skewed BST, h = O(n).

# Topic: Binary Tree, Binary Search Tree