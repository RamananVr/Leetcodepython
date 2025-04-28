"""
LeetCode Problem #1315: Sum of Nodes with Even-Valued Grandparent

Problem Statement:
Given a binary tree, return the sum of values of nodes with an even-valued grandparent. 
A grandparent of a node is the parent of its parent if it exists. If there are no nodes 
with an even-valued grandparent, return 0.

The binary tree is represented using TreeNode class:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

Constraints:
- The number of nodes in the tree is between 1 and 10^4.
- The value of each node is between 1 and 100.
"""

# Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, parent, grandparent):
            if not node:
                return 0
            
            # Calculate the sum for the current node if its grandparent is even-valued
            current_sum = node.val if grandparent and grandparent.val % 2 == 0 else 0
            
            # Recursively calculate the sum for left and right children
            left_sum = dfs(node.left, node, parent)
            right_sum = dfs(node.right, node, parent)
            
            return current_sum + left_sum + right_sum
        
        # Start DFS traversal with root node, no parent, and no grandparent
        return dfs(root, None, None)

# Example Test Cases
def test():
    # Example 1
    root1 = TreeNode(6)
    root1.left = TreeNode(7)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(2)
    root1.left.right = TreeNode(7)
    root1.right.left = TreeNode(1)
    root1.right.right = TreeNode(3)
    root1.left.left.left = TreeNode(9)
    root1.left.right.left = TreeNode(1)
    root1.left.right.right = TreeNode(4)
    root1.right.right.right = TreeNode(5)
    assert Solution().sumEvenGrandparent(root1) == 18

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.left = TreeNode(6)
    root2.right.right = TreeNode(7)
    assert Solution().sumEvenGrandparent(root2) == 0

    # Example 3
    root3 = TreeNode(2)
    root3.left = TreeNode(4)
    root3.right = TreeNode(6)
    root3.left.left = TreeNode(8)
    root3.left.right = TreeNode(10)
    root3.right.left = TreeNode(12)
    root3.right.right = TreeNode(14)
    assert Solution().sumEvenGrandparent(root3) == 44

    print("All test cases passed!")

# Time and Space Complexity Analysis
"""
Time Complexity:
- Each node in the binary tree is visited exactly once during the DFS traversal.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the maximum depth of the recursion stack, which is equal to the height of the tree.
- In the worst case (skewed tree), the height of the tree is O(n).
- In the best case (balanced tree), the height of the tree is O(log n).
- Therefore, the space complexity is O(h), where h is the height of the tree.

Overall:
- Time Complexity: O(n)
- Space Complexity: O(h)
"""

# Topic: Binary Tree

# Run the test cases
if __name__ == "__main__":
    test()