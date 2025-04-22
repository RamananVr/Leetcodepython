"""
LeetCode Question #144: Binary Tree Preorder Traversal

Problem Statement:
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Preorder traversal is a type of depth-first traversal where the nodes are visited in the following order:
1. Visit the root node.
2. Traverse the left subtree.
3. Traverse the right subtree.

Example:
Input: root = [1,null,2,3]
Output: [1,2,3]

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

Follow-up:
Recursive solutions are straightforward. Could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    """
    Perform preorder traversal of a binary tree iteratively.

    :param root: TreeNode, the root of the binary tree
    :return: List[int], the preorder traversal of the binary tree
    """
    if not root:
        return []
    
    stack = [root]
    result = []
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Push right child first so that left child is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    print(preorderTraversal(root1))  # Output: [1, 2, 3]

    # Example 2
    root2 = None
    print(preorderTraversal(root2))  # Output: []

    # Example 3
    root3 = TreeNode(1)
    print(preorderTraversal(root3))  # Output: [1]

    # Example 4
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.left = TreeNode(4)
    root4.left.right = TreeNode(5)
    root4.right.left = TreeNode(6)
    root4.right.right = TreeNode(7)
    print(preorderTraversal(root4))  # Output: [1, 2, 4, 5, 3, 6, 7]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each node is visited exactly once, and the operations performed on each node (appending to result, pushing/popping from stack) take constant time.
- Therefore, the time complexity is O(n), where n is the number of nodes in the binary tree.

Space Complexity:
- In the worst case, the stack will contain all the nodes in the tree (e.g., when the tree is completely unbalanced).
- Therefore, the space complexity is O(n), where n is the number of nodes in the binary tree.

Topic: Binary Tree
"""