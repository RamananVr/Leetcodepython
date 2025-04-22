"""
LeetCode Question #112: Path Sum

Problem Statement:
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the sum 22 is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are no root-to-leaf paths with sum = 5.

Example 3:
Input: root = [1,2], targetSum = 0
Output: false
Explanation: There are no root-to-leaf paths with sum = 0.

Constraints:
- The number of nodes in the tree is in the range [0, 5000].
- -1000 <= Node.val <= 1000
- -1000 <= targetSum <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    """
    Determines if the binary tree has a root-to-leaf path with the given target sum.

    :param root: TreeNode, the root of the binary tree
    :param targetSum: int, the target sum to check
    :return: bool, True if such a path exists, False otherwise
    """
    if not root:
        return False

    # If we are at a leaf node, check if the remaining targetSum equals the node's value
    if not root.left and not root.right:
        return targetSum == root.val

    # Recursively check the left and right subtrees with the updated targetSum
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)

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
    root1 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    targetSum1 = 22
    print(hasPathSum(root1, targetSum1))  # Output: True

    # Test Case 2
    root2 = build_tree([1, 2, 3])
    targetSum2 = 5
    print(hasPathSum(root2, targetSum2))  # Output: False

    # Test Case 3
    root3 = build_tree([1, 2])
    targetSum3 = 0
    print(hasPathSum(root3, targetSum3))  # Output: False

    # Test Case 4
    root4 = build_tree([])
    targetSum4 = 0
    print(hasPathSum(root4, targetSum4))  # Output: False

    # Test Case 5
    root5 = build_tree([1])
    targetSum5 = 1
    print(hasPathSum(root5, targetSum5))  # Output: True

"""
Time Complexity:
- Each node in the binary tree is visited once, so the time complexity is O(N), where N is the number of nodes in the tree.

Space Complexity:
- The space complexity is O(H), where H is the height of the tree. This is due to the recursive call stack. In the worst case (skewed tree), H = N, and in the best case (balanced tree), H = log(N).

Topic: Binary Tree
"""