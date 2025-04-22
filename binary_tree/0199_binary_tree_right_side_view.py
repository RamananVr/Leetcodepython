"""
LeetCode Question #199: Binary Tree Right Side View

Problem Statement:
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    """
    Returns the right side view of a binary tree.

    :param root: TreeNode, the root of the binary tree
    :return: List[int], the values of the nodes visible from the right side
    """
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            # Add the last node of each level to the result
            if i == level_size - 1:
                result.append(node.val)
            # Add child nodes to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(4)
    print(rightSideView(root1))  # Output: [1, 3, 4]

    # Example 2
    root2 = TreeNode(1)
    root2.right = TreeNode(3)
    print(rightSideView(root2))  # Output: [1, 3]

    # Example 3
    root3 = None
    print(rightSideView(root3))  # Output: []

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm traverses each node of the binary tree exactly once.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the size of the queue used for level-order traversal.
- In the worst case (a full binary tree), the queue can hold up to O(n/2) nodes, which simplifies to O(n).
- Thus, the space complexity is O(n).

Topic: Binary Tree
"""