"""
LeetCode Question #2641: Cousins in Binary Tree II

Problem Statement:
Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

Two nodes of a binary tree are cousins if they have the same depth but have different parents.

Return the root of the modified tree.

Note: The depth of a node is the number of edges in the path from the root node to it.

Constraints:
- The number of nodes in the tree is in the range [1, 10^5].
- 1 <= Node.val <= 10^4
"""

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def replaceValueInTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Replace the value of each node with the sum of all its cousins' values.
    """
    if not root:
        return root
    
    # First pass: calculate level sums
    level_sums = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level_sum = 0
        
        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        level_sums.append(level_sum)
    
    # Second pass: replace values with cousin sums
    root.val = 0  # Root has no cousins
    queue = deque([root])
    level = 0
    
    while queue:
        level_size = len(queue)
        level += 1
        
        for _ in range(level_size):
            node = queue.popleft()
            
            # Calculate sibling sum for current node's children
            sibling_sum = 0
            if node.left:
                sibling_sum += node.left.val
            if node.right:
                sibling_sum += node.right.val
            
            # Update children values with cousin sum
            if level < len(level_sums):
                cousin_sum = level_sums[level] - sibling_sum
                
                if node.left:
                    node.left.val = cousin_sum
                    queue.append(node.left)
                if node.right:
                    node.right.val = cousin_sum
                    queue.append(node.right)
    
    return root

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
    
    # Helper function to convert tree to list for testing
    def tree_to_list(root):
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()
        return result

    # Test Case 1
    root1 = build_tree([5, 4, 9, 1, 10, None, 7])
    result1 = replaceValueInTree(root1)
    print(tree_to_list(result1))  # Expected: [0, 0, 0, 7, 7, None, 11]

    # Test Case 2
    root2 = build_tree([3, 1, 2])
    result2 = replaceValueInTree(root2)
    print(tree_to_list(result2))  # Expected: [0, 0, 0]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm performs two BFS traversals of the binary tree.
- Each node is visited exactly twice, so the time complexity is O(n), where n is the number of nodes.

Space Complexity:
- The space complexity is determined by the BFS queue and the level_sums array.
- In the worst case, the queue can hold up to O(w) nodes, where w is the maximum width of the tree.
- The level_sums array stores at most O(h) values, where h is the height of the tree.
- Overall space complexity is O(n) in the worst case.

Topic: Binary Tree
"""
