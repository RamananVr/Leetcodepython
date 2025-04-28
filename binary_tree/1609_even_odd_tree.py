"""
LeetCode Question #1609: Even Odd Tree

Problem Statement:
A binary tree is named Even-Odd if it meets the following conditions:
1. The root of the tree is at level 0, its children are at level 1, their children are at level 2, and so on.
2. For every even-indexed level, all nodes at the level have odd integer values, and the values are strictly increasing from left to right.
3. For every odd-indexed level, all nodes at the level have even integer values, and the values are strictly decreasing from left to right.

Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

Constraints:
- The number of nodes in the tree is in the range [1, 10^5].
- 1 <= Node.val <= 10^6

Example 1:
Input: root = [1,10,4,3,null,7,9,12,8,null,null,6,null,null,2]
Output: true

Example 2:
Input: root = [5,4,2,3,3,7]
Output: false

Example 3:
Input: root = [5,9,1,3,5,7]
Output: false

"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isEvenOddTree(root: TreeNode) -> bool:
    if not root:
        return False
    
    # Use BFS to traverse the tree level by level
    queue = deque([root])
    level = 0  # Start at level 0
    
    while queue:
        level_size = len(queue)
        prev_value = None  # To track the previous value in the current level
        
        for _ in range(level_size):
            node = queue.popleft()
            
            # Check if the value satisfies the even-odd condition
            if level % 2 == 0:  # Even level
                if node.val % 2 == 0 or (prev_value is not None and node.val <= prev_value):
                    return False
            else:  # Odd level
                if node.val % 2 != 0 or (prev_value is not None and node.val >= prev_value):
                    return False
            
            prev_value = node.val
            
            # Add children to the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Move to the next level
        level += 1
    
    return True

# Example Test Cases
def test_isEvenOddTree():
    # Helper function to build a binary tree from a list
    def build_tree(values):
        if not values:
            return None
        root = TreeNode(values[0])
        queue = deque([root])
        i = 1
        while queue and i < len(values):
            node = queue.popleft()
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        return root

    # Test Case 1
    root1 = build_tree([1, 10, 4, 3, None, 7, 9, 12, 8, None, None, 6, None, None, 2])
    assert isEvenOddTree(root1) == True

    # Test Case 2
    root2 = build_tree([5, 4, 2, 3, 3, 7])
    assert isEvenOddTree(root2) == False

    # Test Case 3
    root3 = build_tree([5, 9, 1, 3, 5, 7])
    assert isEvenOddTree(root3) == False

    print("All test cases passed!")

# Run the test cases
test_isEvenOddTree()

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each node is visited exactly once during the BFS traversal.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the maximum number of nodes in the queue at any time.
- In the worst case (a complete binary tree), the queue can hold up to O(n/2) nodes at the last level.
- Therefore, the space complexity is O(n).

Topic: Binary Tree
"""