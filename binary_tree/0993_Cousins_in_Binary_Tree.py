"""
LeetCode Problem #993: Cousins in Binary Tree

Problem Statement:
Given the root of a binary tree with unique values and the values of two different nodes `x` and `y`, 
return `true` if the nodes corresponding to the values `x` and `y` in the tree are cousins, or `false` otherwise.

Two nodes of a binary tree are cousins if they have the same depth but different parents.

Note:
- The number of nodes in the tree is in the range [2, 100].
- 1 <= Node.val <= 100
- Each node has a unique value.

Example 1:
Input: root = [1, 2, 3, 4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1, 2, 3, null, 4, null, 5], x = 5, y = 4
Output: true

Example 3:
Input: root = [1, 2, 3, null, 4], x = 2, y = 3
Output: false

Constraints:
- The tree is a binary tree with unique values.
- x and y are different and exist in the tree.
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isCousins(root: TreeNode, x: int, y: int) -> bool:
    """
    Determines if two nodes in a binary tree are cousins.
    """
    if not root:
        return False

    # Use BFS to find the depth and parent of x and y
    queue = deque([(root, None, 0)])  # (node, parent, depth)
    x_info = y_info = None

    while queue:
        node, parent, depth = queue.popleft()

        # Check if the current node is x or y
        if node.val == x:
            x_info = (parent, depth)
        if node.val == y:
            y_info = (parent, depth)

        # If both x and y are found, break out of the loop
        if x_info and y_info:
            break

        # Add children to the queue
        if node.left:
            queue.append((node.left, node, depth + 1))
        if node.right:
            queue.append((node.right, node, depth + 1))

    # Check if x and y are cousins
    if x_info and y_info:
        x_parent, x_depth = x_info
        y_parent, y_depth = y_info
        return x_depth == y_depth and x_parent != y_parent

    return False

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
    root1 = build_tree([1, 2, 3, 4])
    x1, y1 = 4, 3
    print(isCousins(root1, x1, y1))  # Output: False

    # Test Case 2
    root2 = build_tree([1, 2, 3, None, 4, None, 5])
    x2, y2 = 5, 4
    print(isCousins(root2, x2, y2))  # Output: True

    # Test Case 3
    root3 = build_tree([1, 2, 3, None, 4])
    x3, y3 = 2, 3
    print(isCousins(root3, x3, y3))  # Output: False

"""
Time Complexity:
- The algorithm performs a level-order traversal (BFS) of the binary tree.
- In the worst case, we visit all nodes in the tree once.
- Let n be the number of nodes in the tree. The time complexity is O(n).

Space Complexity:
- The space complexity is determined by the size of the queue used for BFS.
- In the worst case, the queue can hold up to O(n) nodes (in a completely balanced binary tree).
- Thus, the space complexity is O(n).

Topic: Binary Tree
"""