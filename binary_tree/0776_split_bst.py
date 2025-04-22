"""
LeetCode Question #776: Split BST

Problem Statement:
You are given the root of a Binary Search Tree (BST) and an integer `target`. 
Your task is to split the tree into two subtrees: one subtree contains all nodes with values less than or equal to `target`, 
and the other subtree contains all nodes with values greater than `target`. 
Return the two subtrees as a list of two TreeNode objects `[leftSubtree, rightSubtree]`.

Note:
- The input tree is guaranteed to be a BST.
- If the tree is empty, return `[None, None]`.
- The left subtree should contain all nodes with values <= `target`.
- The right subtree should contain all nodes with values > `target`.

Constraints:
- The number of nodes in the tree is in the range [0, 500].
- `-10^4 <= Node.val <= 10^4`
- `-10^4 <= target <= 10^4`
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def splitBST(root: TreeNode, target: int):
    """
    Splits the BST into two subtrees based on the target value.

    Args:
    root (TreeNode): The root of the BST.
    target (int): The target value to split the tree.

    Returns:
    List[TreeNode]: A list containing the roots of the two subtrees [leftSubtree, rightSubtree].
    """
    if not root:
        return [None, None]
    
    if root.val <= target:
        # Split the right subtree
        leftSubtree, rightSubtree = splitBST(root.right, target)
        root.right = leftSubtree
        return [root, rightSubtree]
    else:
        # Split the left subtree
        leftSubtree, rightSubtree = splitBST(root.left, target)
        root.left = rightSubtree
        return [leftSubtree, root]

# Example Test Cases
def print_tree(root):
    """Helper function to print the tree in-order."""
    if not root:
        return []
    return print_tree(root.left) + [root.val] + print_tree(root.right)

if __name__ == "__main__":
    # Example 1
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    target = 2
    leftSubtree, rightSubtree = splitBST(root, target)
    print("Left Subtree:", print_tree(leftSubtree))  # Output: [1, 2]
    print("Right Subtree:", print_tree(rightSubtree))  # Output: [3, 4, 5, 6, 7]

    # Example 2
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)

    target = 5
    leftSubtree, rightSubtree = splitBST(root, target)
    print("Left Subtree:", print_tree(leftSubtree))  # Output: [1, 3, 4, 5]
    print("Right Subtree:", print_tree(rightSubtree))  # Output: [6, 7, 8, 10, 13, 14]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function visits each node of the BST exactly once, so the time complexity is O(n), 
  where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is O(h), where h is the height of the tree. This is due to the recursive call stack.
  In the worst case (skewed tree), h = n. In the best case (balanced tree), h = log(n).
"""

# Topic: Binary Tree