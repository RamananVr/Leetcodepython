"""
LeetCode Problem #513: Find Bottom Left Tree Value

Problem Statement:
Given the root of a binary tree, return the leftmost value in the last row of the tree.

Example 1:
Input: root = [2,1,3]
Output: 1

Example 2:
Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findBottomLeftValue(root: TreeNode) -> int:
    """
    This function finds the leftmost value in the last row of the binary tree.
    """
    # Perform a level-order traversal (BFS)
    queue = deque([root])
    bottom_left_value = root.val  # Initialize with the root value

    while queue:
        # Get the size of the current level
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            # Update the bottom-left value at the start of each level
            if i == 0:
                bottom_left_value = node.val
            # Add child nodes to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return bottom_left_value

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    print(findBottomLeftValue(root1))  # Output: 1

    # Test Case 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.right.left = TreeNode(5)
    root2.right.right = TreeNode(6)
    root2.right.left.left = TreeNode(7)
    print(findBottomLeftValue(root2))  # Output: 7

    # Test Case 3
    root3 = TreeNode(1)
    print(findBottomLeftValue(root3))  # Output: 1

"""
Time Complexity:
- The function performs a level-order traversal of the binary tree, visiting each node exactly once.
- Let n be the number of nodes in the tree. The time complexity is O(n).

Space Complexity:
- The space complexity is determined by the size of the queue used for BFS.
- In the worst case (a completely unbalanced tree), the queue can hold up to O(n) nodes.
- In the best case (a balanced tree), the queue holds O(w) nodes, where w is the maximum width of the tree.
- Overall, the space complexity is O(n) in the worst case.

Topic: Binary Tree
"""