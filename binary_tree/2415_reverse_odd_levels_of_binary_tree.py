"""
LeetCode Question #2415: Reverse Odd Levels of Binary Tree

Problem Statement:
Given the root of a perfect binary tree, reverse the values of the nodes at each odd level of the tree 
(i.e., level 1, level 3, level 5, etc.). The level of a node is the number of edges along the path 
between it and the root node.

- The tree is perfect, meaning all levels are completely filled.
- The root is at level 0, its children are at level 1, and so on.

Return the root of the reversed tree.

Example:
Input: root = [2,3,5,8,13,21,34]
Output: [2,5,3,8,13,21,34]
Explanation:
The tree looks like this:
        2
      /   \
     3     5
    / \   / \
   8  13 21 34
After reversing odd levels:
        2
      /   \
     5     3
    / \   / \
   8  13 21 34

Constraints:
- The number of nodes in the tree is in the range [1, 2^14 - 1].
- -2^15 <= Node.val <= 2^15
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def reverseOddLevels(root: TreeNode) -> TreeNode:
    """
    Reverses the values of nodes at odd levels of a perfect binary tree.
    """
    if not root:
        return None

    # Perform a level-order traversal using a queue
    queue = deque([root])
    level = 0

    while queue:
        level_size = len(queue)
        current_level = []

        # Collect nodes at the current level
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Reverse the values of nodes at odd levels
        if level % 2 == 1:
            left, right = 0, len(current_level) - 1
            while left < right:
                current_level[left].val, current_level[right].val = current_level[right].val, current_level[left].val
                left += 1
                right -= 1

        level += 1

    return root

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

# Helper function to perform level-order traversal and return the result as a list
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

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    root = build_tree([2, 3, 5, 8, 13, 21, 34])
    reversed_root = reverseOddLevels(root)
    print(tree_to_list(reversed_root))  # Output: [2, 5, 3, 8, 13, 21, 34]

    # Test Case 2
    root = build_tree([7, 13, 11])
    reversed_root = reverseOddLevels(root)
    print(tree_to_list(reversed_root))  # Output: [7, 11, 13]

    # Test Case 3
    root = build_tree([1])
    reversed_root = reverseOddLevels(root)
    print(tree_to_list(reversed_root))  # Output: [1]

"""
Time Complexity:
- The algorithm performs a level-order traversal of the tree, visiting each node exactly once.
- Let n be the number of nodes in the tree. The time complexity is O(n).

Space Complexity:
- The space complexity is determined by the queue used for level-order traversal.
- In the worst case, the queue can hold up to half the nodes in the tree (at the last level), which is O(n/2) = O(n).

Topic: Binary Tree
"""