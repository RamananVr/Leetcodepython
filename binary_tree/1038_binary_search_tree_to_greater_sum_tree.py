"""
LeetCode Question #1038: Binary Search Tree to Greater Sum Tree

Problem Statement:
Given the root of a Binary Search Tree (BST), convert it to a Greater Sum Tree (GST) such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a Binary Search Tree is a tree that satisfies these constraints:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Note: This problem is the same as LeetCode Question #538: Convert BST to Greater Tree.

Example 1:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Example 2:
Input: root = [0,null,1]
Output: [1,null,1]

Constraints:
- The number of nodes in the tree is in the range [1, 100].
- 0 <= Node.val <= 100.
- All the values in the tree are unique.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        Convert the given BST to a Greater Sum Tree (GST).
        """
        self.running_sum = 0

        def reverse_inorder_traversal(node):
            if not node:
                return
            # Traverse the right subtree first
            reverse_inorder_traversal(node.right)
            # Update the current node's value
            self.running_sum += node.val
            node.val = self.running_sum
            # Traverse the left subtree
            reverse_inorder_traversal(node.left)

        reverse_inorder_traversal(root)
        return root

# Helper function to build a binary tree from a list (for testing purposes)
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

# Helper function to perform level-order traversal and return the tree as a list
def tree_to_list(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
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

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    root1 = build_tree([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
    result1 = solution.bstToGst(root1)
    print(tree_to_list(result1))  # Expected Output: [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]

    # Test Case 2
    root2 = build_tree([0, None, 1])
    result2 = solution.bstToGst(root2)
    print(tree_to_list(result2))  # Expected Output: [1, None, 1]

    # Test Case 3
    root3 = build_tree([2, 0, 3, None, 1])
    result3 = solution.bstToGst(root3)
    print(tree_to_list(result3))  # Expected Output: [5, 6, 3, None, 6]

"""
Time Complexity:
- The solution performs a reverse in-order traversal of the tree, visiting each node exactly once.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is O(h), where h is the height of the tree. This is due to the recursive call stack during the traversal.
- In the worst case (skewed tree), h = n, and in the best case (balanced tree), h = log(n).

Topic: Binary Tree
"""