"""
LeetCode Problem #958: Check Completeness of a Binary Tree

Problem Statement:
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, 
and all nodes in the last level are as far left as possible. It can have between 1 and 2^h nodes 
inclusive at the last level h.

Example 1:
    Input: root = [1,2,3,4,5,6]
    Output: true
    Explanation: Every level before the last is full (i.e., levels 0 and 1), and all nodes in the last level 
    (level 2) are as far left as possible.

Example 2:
    Input: root = [1,2,3,4,5,null,7]
    Output: false
    Explanation: The node with value 7 is not as far left as possible.

Constraints:
    - The number of nodes in the tree is in the range [1, 100].
    - 1 <= Node.val <= 1000
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isCompleteTree(root: TreeNode) -> bool:
    """
    Function to check if a binary tree is a complete binary tree.
    """
    if not root:
        return True

    # Perform a level-order traversal using a queue
    queue = deque([root])
    encountered_null = False

    while queue:
        node = queue.popleft()

        if node is None:
            # If we encounter a null node, set the flag
            encountered_null = True
        else:
            # If we encounter a non-null node after a null node, the tree is not complete
            if encountered_null:
                return False
            # Add the left and right children to the queue
            queue.append(node.left)
            queue.append(node.right)

    return True

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    print(isCompleteTree(root1))  # Output: True

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.right = TreeNode(7)
    print(isCompleteTree(root2))  # Output: False

    # Additional Test Case
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    print(isCompleteTree(root3))  # Output: True

"""
Time Complexity Analysis:
- The function performs a level-order traversal of the binary tree, visiting each node exactly once.
- Let n be the number of nodes in the tree. The time complexity is O(n).

Space Complexity Analysis:
- The space complexity is determined by the size of the queue used for the level-order traversal.
- In the worst case, the queue can hold up to the maximum number of nodes at any level, which is O(n) in the case of a complete binary tree.
- Therefore, the space complexity is O(n).

Topic: Binary Tree
"""