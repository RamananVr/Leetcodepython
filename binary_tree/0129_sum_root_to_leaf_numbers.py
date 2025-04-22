"""
LeetCode Question #129: Sum Root to Leaf Numbers

Problem Statement:
You are given the root of a binary tree containing digits from 0 to 9 only. Each root-to-leaf path in the tree represents a number.

- For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. A leaf node is a node with no children.

Example 1:
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- 0 <= Node.val <= 9
- The depth of the tree will not exceed 10.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root: TreeNode) -> int:
    """
    This function calculates the sum of all root-to-leaf numbers in a binary tree.
    """
    def dfs(node, current_sum):
        if not node:
            return 0
        current_sum = current_sum * 10 + node.val
        # If it's a leaf node, return the current sum
        if not node.left and not node.right:
            return current_sum
        # Otherwise, continue the DFS on left and right children
        return dfs(node.left, current_sum) + dfs(node.right, current_sum)
    
    return dfs(root, 0)

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    print(sumNumbers(root1))  # Output: 25

    # Example 2
    root2 = TreeNode(4)
    root2.left = TreeNode(9)
    root2.right = TreeNode(0)
    root2.left.left = TreeNode(5)
    root2.left.right = TreeNode(1)
    print(sumNumbers(root2))  # Output: 1026

    # Additional Test Case
    root3 = TreeNode(0)
    root3.left = TreeNode(1)
    print(sumNumbers(root3))  # Output: 1

"""
Time Complexity:
- Each node is visited exactly once, so the time complexity is O(N), where N is the number of nodes in the tree.

Space Complexity:
- The space complexity is O(H), where H is the height of the tree. This is due to the recursive call stack. In the worst case (a skewed tree), H can be equal to N.

Topic: Binary Tree
"""