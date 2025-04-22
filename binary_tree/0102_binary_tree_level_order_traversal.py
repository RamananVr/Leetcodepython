"""
LeetCode Question #102: Binary Tree Level Order Traversal

Problem Statement:
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    """
    Perform level order traversal of a binary tree.

    :param root: TreeNode, the root of the binary tree
    :return: List[List[int]], the level order traversal of the tree
    """
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(levelOrder(root1))  # Output: [[3], [9, 20], [15, 7]]

    # Example 2
    root2 = TreeNode(1)
    print(levelOrder(root2))  # Output: [[1]]

    # Example 3
    root3 = None
    print(levelOrder(root3))  # Output: []

"""
Time Complexity:
- O(n): Each node is visited exactly once, where n is the number of nodes in the tree.

Space Complexity:
- O(n): The space complexity is determined by the size of the queue, which in the worst case can hold all the nodes at the deepest level of the tree.

Topic: Binary Tree
"""