"""
LeetCode Question #637: Average of Levels in Binary Tree

Problem Statement:
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
Answers within 10^-5 of the actual answer will be accepted.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000, 14.50000, 11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

Example 2:
Input: root = [3,9,20,15,7]
Output: [3.00000, 14.50000, 11.00000]

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1
"""

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    """
    Function to calculate the average of each level in a binary tree.
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])  # Use a queue for level-order traversal
    
    while queue:
        level_sum = 0
        level_count = len(queue)
        
        for _ in range(level_count):
            node = queue.popleft()
            level_sum += node.val
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Calculate the average for the current level
        result.append(level_sum / level_count)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(averageOfLevels(root1))  # Output: [3.0, 14.5, 11.0]

    # Example 2
    root2 = TreeNode(3)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.left.left = TreeNode(15)
    root2.left.right = TreeNode(7)
    print(averageOfLevels(root2))  # Output: [3.0, 14.5, 11.0]

"""
Time Complexity:
- O(n): Each node is visited exactly once during the level-order traversal.

Space Complexity:
- O(m): At most, the queue will contain all the nodes at the largest level of the tree, where m is the maximum width of the tree.
"""

# Topic: Binary Tree