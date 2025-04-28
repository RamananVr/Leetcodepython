"""
LeetCode Question #1382: Balance a Binary Search Tree

Problem Statement:
Given a binary search tree, return a balanced binary search tree with the same node values. 
A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

If there is more than one answer, return any of them.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- The value of each node is unique.

Example:
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def balanceBST(root: TreeNode) -> TreeNode:
    """
    Function to balance a binary search tree.
    """
    def inorder_traversal(node):
        """
        Perform an inorder traversal to collect nodes in sorted order.
        """
        if not node:
            return []
        return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

    def build_balanced_bst(sorted_values, left, right):
        """
        Build a balanced BST from sorted values using divide-and-conquer.
        """
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(sorted_values[mid])
        root.left = build_balanced_bst(sorted_values, left, mid - 1)
        root.right = build_balanced_bst(sorted_values, mid + 1, right)
        return root

    # Step 1: Get sorted values from the BST using inorder traversal
    sorted_values = inorder_traversal(root)

    # Step 2: Build a balanced BST from the sorted values
    return build_balanced_bst(sorted_values, 0, len(sorted_values) - 1)

# Example Test Cases
def print_tree(root):
    """
    Helper function to print the tree in level order for testing purposes.
    """
    if not root:
        return []
    from collections import deque
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

if __name__ == "__main__":
    # Example 1
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    balanced_root = balanceBST(root)
    print(print_tree(balanced_root))  # Output: [2, 1, 3, None, None, None, 4]

    # Example 2
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    balanced_root = balanceBST(root)
    print(print_tree(balanced_root))  # Output: [3, 1, 4, None, 2]

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The `inorder_traversal` function visits each node exactly once, so its time complexity is O(n), 
     where n is the number of nodes in the tree.
   - The `build_balanced_bst` function constructs the tree in O(n) time, as it processes each element of the sorted list once.
   - Overall time complexity: O(n).

2. Space Complexity:
   - The `inorder_traversal` function uses O(n) space to store the sorted values.
   - The recursion stack for `build_balanced_bst` can go up to O(log n) in the best case (balanced tree) or O(n) in the worst case (completely unbalanced tree).
   - Overall space complexity: O(n).

Topic: Binary Tree
"""