"""
LeetCode Problem #1602: Find Nearest Right Node in Binary Tree

Problem Statement:
Given the `root` of a binary tree and a node `u` in the tree, return the nearest node on the same level that is to the right of `u`, or return `None` if `u` is the rightmost node in its level.

Example 1:
Input: root = [1,2,3,null,4,5,6], u = 4
Output: 5
Explanation: The nearest node to the right of 4 is 5.

Example 2:
Input: root = [1,2,3,null,4,5,6], u = 6
Output: None
Explanation: 6 is the rightmost node in its level.

Example 3:
Input: root = [1,2,3,null,4,5,6], u = 3
Output: None
Explanation: 3 is the rightmost node in its level.

Constraints:
1. The number of nodes in the tree is in the range [1, 10^5].
2. The values of the nodes are unique.
3. `u` is a node in the binary tree rooted at `root`.
4. `root` is not `None`.

"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findNearestRightNode(root: TreeNode, u: TreeNode) -> TreeNode:
    """
    Finds the nearest right node to the given node `u` in the same level of the binary tree.
    """
    if not root:
        return None

    # Perform a level-order traversal (BFS)
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # If the current node is `u`, return the next node in the level (if it exists)
            if node == u:
                return queue[0] if i < level_size - 1 else None

            # Add child nodes to the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return None

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
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root

    # Test Case 1
    root = build_tree([1, 2, 3, None, 4, 5, 6])
    u = root.left.right  # Node with value 4
    print(findNearestRightNode(root, u).val if findNearestRightNode(root, u) else None)  # Output: 5

    # Test Case 2
    root = build_tree([1, 2, 3, None, 4, 5, 6])
    u = root.right.right  # Node with value 6
    print(findNearestRightNode(root, u))  # Output: None

    # Test Case 3
    root = build_tree([1, 2, 3, None, 4, 5, 6])
    u = root.right  # Node with value 3
    print(findNearestRightNode(root, u))  # Output: None

"""
Time Complexity:
- The algorithm performs a level-order traversal of the binary tree.
- In the worst case, we visit all nodes once, so the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the size of the queue used for BFS.
- In the worst case, the queue can hold up to O(w) nodes, where w is the maximum width of the tree.
- For a balanced binary tree, w is approximately n/2, so the space complexity is O(n) in the worst case.

Topic: Binary Tree, Breadth-First Search (BFS)
"""