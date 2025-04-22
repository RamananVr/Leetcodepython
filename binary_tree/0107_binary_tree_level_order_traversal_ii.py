"""
LeetCode Question #107: Binary Tree Level Order Traversal II

Problem Statement:
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. 
(i.e., from left to right, level by level from leaf to root).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000
"""

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderBottom(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Perform a bottom-up level order traversal of a binary tree.
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    
    return result[::-1]  # Reverse the result to get bottom-up order

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(levelOrderBottom(root1))  # Output: [[15,7],[9,20],[3]]

    # Example 2
    root2 = TreeNode(1)
    print(levelOrderBottom(root2))  # Output: [[1]]

    # Example 3
    root3 = None
    print(levelOrderBottom(root3))  # Output: []

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each node is visited exactly once, and for each node, we perform constant-time operations.
- Therefore, the time complexity is O(n), where n is the number of nodes in the binary tree.

Space Complexity:
- The space complexity is determined by the size of the queue and the result list.
- In the worst case (a full binary tree), the queue can hold up to O(n/2) nodes at the last level, and the result list will store all nodes.
- Therefore, the space complexity is O(n).

Topic: Binary Tree
"""