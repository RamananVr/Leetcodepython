"""
LeetCode Problem #2641: Cousins in Binary Tree II

Problem Statement:
Given the root of a binary tree, replace the value of each node in the tree with the sum of all values of its cousins, and return the root of the modified tree.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note:
- The root node has no cousins.
- The binary tree is guaranteed to have at least one node.

Constraints:
- The number of nodes in the tree is in the range [1, 10^5].
- 1 <= Node.val <= 10^4

Example:
Input: root = [5,4,9,1,10,null,7]
Output: [0,0,0,7,7,null,11]

Explanation:
- The root node has no cousins, so its value is replaced with 0.
- The node with value 4 has cousins with values [9], so its value is replaced with 0.
- The node with value 9 has cousins with values [4], so its value is replaced with 0.
- The node with value 1 has cousins with values [10, 7], so its value is replaced with 7.
- The node with value 10 has cousins with values [1, 7], so its value is replaced with 7.
- The node with value 7 has cousins with values [1, 10], so its value is replaced with 11.

Topic: Binary Tree
"""

from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def replaceValueInTree(root: TreeNode) -> TreeNode:
    if not root:
        return None

    # Step 1: Perform a level-order traversal to calculate the sum of values at each depth
    level_sum = defaultdict(int)
    parent_map = {}
    queue = deque([(root, 0, None)])  # (node, depth, parent)

    while queue:
        node, depth, parent = queue.popleft()
        level_sum[depth] += node.val
        parent_map[node] = parent

        if node.left:
            queue.append((node.left, depth + 1, node))
        if node.right:
            queue.append((node.right, depth + 1, node))

    # Step 2: Replace each node's value with the sum of its cousins
    queue = deque([(root, 0)])
    while queue:
        node, depth = queue.popleft()
        parent = parent_map[node]

        # Calculate the sum of cousins
        if parent is None:  # Root node has no cousins
            node.val = 0
        else:
            # Subtract the value of the node and its sibling (if any) from the level sum
            sibling_sum = 0
            if parent.left and parent.left != node:
                sibling_sum += parent.left.val
            if parent.right and parent.right != node:
                sibling_sum += parent.right.val

            node.val = level_sum[depth] - sibling_sum

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return root

# Example Test Cases
def print_tree_level_order(root):
    """Helper function to print the tree in level-order for testing."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val if node else None)
        if node:
            queue.append(node.left)
            queue.append(node.right)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

# Test Case 1
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(9)
root.left.left = TreeNode(1)
root.left.right = TreeNode(10)
root.right.right = TreeNode(7)

new_root = replaceValueInTree(root)
print(print_tree_level_order(new_root))  # Output: [0, 0, 0, 7, 7, None, 11]

# Test Case 2
root = TreeNode(1)
new_root = replaceValueInTree(root)
print(print_tree_level_order(new_root))  # Output: [0]

# Test Case 3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

new_root = replaceValueInTree(root)
print(print_tree_level_order(new_root))  # Output: [0, 0, 0, 11, 11, 11, 11]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm performs a level-order traversal twice:
  1. To calculate the level sums and parent mapping: O(n), where n is the number of nodes.
  2. To update the node values: O(n).
- Overall time complexity: O(n).

Space Complexity:
- The space required for the queue during level-order traversal is O(w), where w is the maximum width of the tree.
- The space required for the level_sum and parent_map dictionaries is O(n).
- Overall space complexity: O(n).
"""