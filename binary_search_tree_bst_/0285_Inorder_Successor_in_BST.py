"""
LeetCode Problem #285: Inorder Successor in BST

Problem Statement:
Given the `root` of a binary search tree and a node `p` in it, return the in-order successor of that node in the BST. 
If the given node has no in-order successor in the tree, return `None`.

The successor of a node `p` is the node with the smallest key greater than `p.val`.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5
- All values in the tree are unique.
- `p` is a node in the BST.

Example:
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor is 2.

Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: None
Explanation: 6 has no in-order successor because it is the largest node in the tree.
"""

# Python Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        successor = None
        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor

# Example Test Cases
def test_inorder_successor():
    # Helper function to build a BST from a list
    def insert_into_bst(root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = insert_into_bst(root.left, val)
        else:
            root.right = insert_into_bst(root.right, val)
        return root

    # Test Case 1
    root = None
    for val in [2, 1, 3]:
        root = insert_into_bst(root, val)
    p = root.left  # Node with value 1
    assert Solution().inorderSuccessor(root, p).val == 2

    # Test Case 2
    root = None
    for val in [5, 3, 6, 2, 4, 1]:
        root = insert_into_bst(root, val)
    p = root.right  # Node with value 6
    assert Solution().inorderSuccessor(root, p) is None

    # Test Case 3
    root = None
    for val in [20, 9, 25, 5, 12, 11, 14]:
        root = insert_into_bst(root, val)
    p = root.left.right.right  # Node with value 14
    assert Solution().inorderSuccessor(root, p).val == 20

    print("All test cases passed!")

# Run the test cases
if __name__ == "__main__":
    test_inorder_successor()

"""
Time Complexity Analysis:
- The algorithm traverses the tree from the root to a leaf in the worst case. 
  Since the height of a balanced BST is O(log n), the time complexity is O(log n).
- In the worst case of a completely unbalanced tree, the height is O(n), so the time complexity is O(n).

Space Complexity Analysis:
- The algorithm uses O(1) additional space since it does not use recursion or any auxiliary data structures.

Topic: Binary Search Tree (BST)
"""