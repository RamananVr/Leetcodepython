"""
LeetCode Question #103: Binary Tree Zigzag Level Order Traversal

Problem Statement:
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -100 <= Node.val <= 100
"""

from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True  # Flag to determine the direction of traversal
    
    while queue:
        level_size = len(queue)
        level = deque()
        
        for _ in range(level_size):
            node = queue.popleft()
            
            # Add the node's value to the level based on the current direction
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            
            # Add child nodes to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Add the current level to the result and toggle the direction
        result.append(list(level))
        left_to_right = not left_to_right
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Helper function to build a binary tree from a list
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

    # Test Case 1
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print(zigzagLevelOrder(root1))  # Output: [[3], [20, 9], [15, 7]]

    # Test Case 2
    root2 = build_tree([1])
    print(zigzagLevelOrder(root2))  # Output: [[1]]

    # Test Case 3
    root3 = build_tree([])
    print(zigzagLevelOrder(root3))  # Output: []

"""
Time Complexity:
- Each node is visited exactly once, and operations on each node (adding to deque, appending to result) take O(1).
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the size of the queue, which can hold at most the number of nodes at the largest level of the tree.
- In the worst case (a balanced binary tree), the largest level has approximately n/2 nodes, so the space complexity is O(n).

Topic: Binary Tree
"""