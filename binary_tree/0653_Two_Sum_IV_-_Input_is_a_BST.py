"""
LeetCode Problem #653: Two Sum IV - Input is a BST

Problem Statement:
Given the root of a Binary Search Tree (BST) and an integer `k`, return `true` if there exist two elements in the BST such that their sum is equal to `k`, otherwise return `false`.

Example 1:
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^4 <= Node.val <= 10^4
- root is guaranteed to be a valid BST.
- -10^5 <= k <= 10^5
"""

# Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget(root: TreeNode, k: int) -> bool:
    """
    This function checks if there exist two elements in the BST such that their sum equals k.
    """
    def inorder_traversal(node):
        """Perform an inorder traversal to get the sorted list of values."""
        if not node:
            return []
        return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
    
    # Get all values in sorted order using inorder traversal
    values = inorder_traversal(root)
    
    # Use two pointers to find if there exists a pair with sum k
    left, right = 0, len(values) - 1
    while left < right:
        current_sum = values[left] + values[right]
        if current_sum == k:
            return True
        elif current_sum < k:
            left += 1
        else:
            right -= 1
    
    return False

# Example Test Cases
if __name__ == "__main__":
    # Helper function to build a BST from a list
    def insert_into_bst(root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = insert_into_bst(root.left, val)
        else:
            root.right = insert_into_bst(root.right, val)
        return root

    def build_bst(values):
        root = None
        for val in values:
            root = insert_into_bst(root, val)
        return root

    # Test Case 1
    root1 = build_bst([5, 3, 6, 2, 4, 7])
    k1 = 9
    print(findTarget(root1, k1))  # Output: True

    # Test Case 2
    root2 = build_bst([5, 3, 6, 2, 4, 7])
    k2 = 28
    print(findTarget(root2, k2))  # Output: False

    # Test Case 3
    root3 = build_bst([2, 1, 3])
    k3 = 4
    print(findTarget(root3, k3))  # Output: True

    # Test Case 4
    root4 = build_bst([2, 1, 3])
    k4 = 7
    print(findTarget(root4, k4))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- Inorder traversal takes O(n), where n is the number of nodes in the BST.
- The two-pointer approach to find the pair with sum k takes O(n) in the worst case.
- Overall time complexity: O(n).

Space Complexity:
- The space required for the inorder traversal list is O(n).
- The recursion stack for the inorder traversal takes O(h), where h is the height of the tree.
- In the worst case (skewed tree), h = n. In the best case (balanced tree), h = log(n).
- Overall space complexity: O(n).

Topic: Binary Tree
"""