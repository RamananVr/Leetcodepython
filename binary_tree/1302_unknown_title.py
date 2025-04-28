"""
LeetCode Problem #1302: Deepest Leaves Sum

Problem Statement:
Given the root of a binary tree, return the sum of values of its deepest leaves.

Example 1:
          1
         / \
        2   3
       / \   \
      4   5   6
     /         \
    7           8

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Explanation: The deepest leaves are 7 and 8, and their sum is 7 + 8 = 15.

Example 2:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 1 <= Node.val <= 100
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deepestLeavesSum(root: TreeNode) -> int:
    """
    Function to calculate the sum of the values of the deepest leaves in a binary tree.
    """
    if not root:
        return 0

    # Perform a level-order traversal (BFS)
    queue = deque([root])
    while queue:
        level_sum = 0  # Sum of the current level
        level_size = len(queue)  # Number of nodes at the current level

        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val  # Add the value of the current node

            # Add child nodes to the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # The last computed level_sum corresponds to the deepest level
    return level_sum

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(6)
    root1.left.left.left = TreeNode(7)
    root1.right.right.right = TreeNode(8)
    print(deepestLeavesSum(root1))  # Output: 15

    # Example 2
    root2 = TreeNode(6)
    root2.left = TreeNode(7)
    root2.right = TreeNode(8)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(7)
    root2.right.left = TreeNode(1)
    root2.right.right = TreeNode(3)
    root2.left.left.left = TreeNode(9)
    root2.left.right.left = TreeNode(1)
    root2.left.right.right = TreeNode(4)
    root2.right.right.right = TreeNode(5)
    print(deepestLeavesSum(root2))  # Output: 19

"""
Time Complexity:
- The function performs a level-order traversal (BFS) of the binary tree.
- Each node is visited exactly once, so the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the size of the queue used for BFS.
- In the worst case, the queue can hold up to the maximum number of nodes at any level, which is O(w), where w is the maximum width of the tree.
- In the worst case, w can be proportional to n (e.g., in a complete binary tree), so the space complexity is O(n).

Topic: Binary Tree
"""