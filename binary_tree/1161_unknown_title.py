"""
LeetCode Problem #1161: Maximum Level Sum of a Binary Tree

Problem Statement:
Given the `root` of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level `x` such that the sum of all the values of nodes at level `x` is maximal.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5
"""

from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxLevelSum(root: TreeNode) -> int:
    """
    Function to find the smallest level x such that the sum of all the values of nodes at level x is maximal.
    """
    if not root:
        return 0

    # Use a queue for level-order traversal
    queue = deque([root])
    level = 1
    max_sum = float('-inf')
    result_level = 1

    while queue:
        level_sum = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Update the maximum sum and the corresponding level
        if level_sum > max_sum:
            max_sum = level_sum
            result_level = level

        level += 1

    return result_level

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(7)
    root1.right = TreeNode(0)
    root1.left.left = TreeNode(7)
    root1.left.right = TreeNode(-8)
    print(maxLevelSum(root1))  # Output: 2

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.right = TreeNode(8)
    root2.right.right.left = TreeNode(6)
    root2.right.right.right = TreeNode(7)
    print(maxLevelSum(root2))  # Output: 3

    # Example 3
    root3 = TreeNode(1)
    print(maxLevelSum(root3))  # Output: 1

"""
Time Complexity Analysis:
- The function performs a level-order traversal of the binary tree, visiting each node exactly once.
- Let n be the number of nodes in the tree.
- Time complexity: O(n)

Space Complexity Analysis:
- The space complexity is determined by the maximum number of nodes at any level of the tree (the width of the tree).
- In the worst case, the space complexity is O(n) for a completely balanced binary tree or a completely skewed tree.
- Space complexity: O(n)

Topic: Binary Tree
"""