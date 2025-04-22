"""
LeetCode Problem #515: Find Largest Value in Each Tree Row

Problem Statement:
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Explanation:
          1
         / \
        3   2
       / \    \
      5   3    9
    - The largest value in the 0th row is 1.
    - The largest value in the 1st row is 3.
    - The largest value in the 2nd row is 9.

Example 2:
Input: root = [1,2,3]
Output: [1,3]
Explanation:
          1
         / \
        2   3
    - The largest value in the 0th row is 1.
    - The largest value in the 1st row is 3.

Constraints:
- The number of nodes in the tree will be in the range [0, 10^4].
- -2^31 <= Node.val <= 2^31 - 1
"""

from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestValues(root: Optional[TreeNode]) -> List[int]:
    """
    Finds the largest value in each row of a binary tree.

    Args:
    root (TreeNode): The root of the binary tree.

    Returns:
    List[int]: A list of the largest values in each row.
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        max_value = float('-inf')

        for _ in range(level_size):
            node = queue.popleft()
            max_value = max(max_value, node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(max_value)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)
    root1.left.right = TreeNode(3)
    root1.right.right = TreeNode(9)
    print(largestValues(root1))  # Output: [1, 3, 9]

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    print(largestValues(root2))  # Output: [1, 3]

    # Example 3: Empty tree
    root3 = None
    print(largestValues(root3))  # Output: []

    # Example 4: Single node tree
    root4 = TreeNode(42)
    print(largestValues(root4))  # Output: [42]

    # Example 5: Tree with negative values
    root5 = TreeNode(-1)
    root5.left = TreeNode(-2)
    root5.right = TreeNode(-3)
    root5.left.left = TreeNode(-4)
    root5.left.right = TreeNode(-5)
    print(largestValues(root5))  # Output: [-1, -2, -4]

"""
Time Complexity:
- The algorithm performs a level-order traversal of the binary tree.
- Each node is visited exactly once, so the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the size of the queue used for the level-order traversal.
- In the worst case, the queue can hold up to O(w) nodes, where w is the maximum width of the tree.
- Therefore, the space complexity is O(w).

Topic: Binary Tree
"""