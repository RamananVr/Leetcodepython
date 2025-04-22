"""
LeetCode Problem #998: Maximum Binary Tree II

Problem Statement:
A maximum binary tree is a binary tree where every node has a value greater than any other value in its subtree.

You are given the root of a maximum binary tree and an integer `val`.

Just as in the [Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/) problem, the given tree was constructed from a list `nums` (a subset of the integers in the range `[1, 1000]`) recursively with the following algorithm:
1. Create a root node whose value is the maximum value in `nums`.
2. Recursively build the left subtree on the subarray prefix to the left of the maximum value.
3. Recursively build the right subtree on the subarray suffix to the right of the maximum value.

Given the root of a maximum binary tree and an integer `val`, insert the value `val` into the tree such that it remains a maximum binary tree.

Return the root of the modified tree.

Constraints:
- The number of nodes in the tree is in the range `[1, 100]`.
- `1 <= Node.val <= 100`.
- All the values of the tree are unique.
- `1 <= val <= 100`.

Example:
Input: root = [4,1,3,null,null,2], val = 5
Output: [5,4,null,1,3,null,null,2]
Explanation: A node with value 5 becomes the new root, and the entire tree is the left subtree of the new root.

Follow-up:
Can you solve the problem without reconstructing the tree?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoMaxTree(root: TreeNode, val: int) -> TreeNode:
    """
    Inserts a value into the maximum binary tree while maintaining its properties.
    """
    if not root or val > root.val:
        # If the tree is empty or the new value is greater than the root value,
        # the new value becomes the new root, and the current tree becomes its left subtree.
        return TreeNode(val, left=root)
    
    # Otherwise, recursively insert the value into the right subtree.
    root.right = insertIntoMaxTree(root.right, val)
    return root

# Helper function to print the tree in level-order for testing purposes.
def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    root = TreeNode(4, TreeNode(1), TreeNode(3, TreeNode(2)))
    val = 5
    new_root = insertIntoMaxTree(root, val)
    print(level_order_traversal(new_root))  # Output: [5, 4, None, 1, 3, None, None, 2]

    # Test Case 2
    root = TreeNode(5, TreeNode(2, None, TreeNode(1)), TreeNode(4))
    val = 3
    new_root = insertIntoMaxTree(root, val)
    print(level_order_traversal(new_root))  # Output: [5, 2, 4, None, 1, None, None, None, 3]

    # Test Case 3
    root = TreeNode(5)
    val = 6
    new_root = insertIntoMaxTree(root, val)
    print(level_order_traversal(new_root))  # Output: [6, 5]

"""
Time Complexity:
- In the worst case, we traverse the entire rightmost path of the tree, which has a depth of O(n), where n is the number of nodes in the tree.
- Thus, the time complexity is O(n).

Space Complexity:
- The space complexity is O(h), where h is the height of the tree, due to the recursive call stack.
- In the worst case, the height of the tree is O(n) (if the tree is skewed), so the space complexity is O(n).

Topic: Binary Tree
"""