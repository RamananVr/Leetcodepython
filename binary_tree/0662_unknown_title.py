"""
LeetCode Problem #662: Maximum Width of Binary Tree

Problem Statement:
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels. The width of one level is defined as the number of nodes between the leftmost and rightmost non-null nodes in the level, where the null nodes between the non-null nodes are also counted into the width.

It is guaranteed that the answer will be in the range of a 32-bit signed integer.

Constraints:
- The number of nodes in the tree is in the range [1, 3000].
- -100 <= Node.val <= 100
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def widthOfBinaryTree(root: TreeNode) -> int:
    """
    Function to calculate the maximum width of a binary tree.
    """
    if not root:
        return 0

    # Initialize a queue for level-order traversal
    # Each element in the queue is a tuple (node, index)
    # where index is the position of the node in the current level
    queue = deque([(root, 0)])
    max_width = 0

    while queue:
        level_length = len(queue)
        _, first_index = queue[0]  # Get the index of the first node in the level
        for _ in range(level_length):
            node, index = queue.popleft()
            # Add child nodes to the queue with their respective indices
            if node.left:
                queue.append((node.left, 2 * index))
            if node.right:
                queue.append((node.right, 2 * index + 1))
        # Calculate the width of the current level
        _, last_index = queue[-1] if queue else (None, index)
        max_width = max(max_width, last_index - first_index + 1)

    return max_width

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)
    root1.left.right = TreeNode(3)
    root1.right.right = TreeNode(9)
    print("Example 1 Output:", widthOfBinaryTree(root1))  # Expected Output: 4

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(5)
    print("Example 2 Output:", widthOfBinaryTree(root2))  # Expected Output: 2

    # Example 3
    root3 = TreeNode(1)
    root3.left = TreeNode(3)
    root3.left.left = TreeNode(5)
    root3.left.left.left = TreeNode(6)
    print("Example 3 Output:", widthOfBinaryTree(root3))  # Expected Output: 2

"""
Time Complexity:
- The function performs a level-order traversal of the binary tree, visiting each node exactly once.
- Let n be the number of nodes in the tree. The time complexity is O(n).

Space Complexity:
- The space complexity is determined by the size of the queue used for level-order traversal.
- In the worst case, the queue can hold all the nodes in the last level of the tree, which is O(n) in the case of a complete binary tree.
- Therefore, the space complexity is O(n).

Topic: Binary Tree
"""