"""
LeetCode Problem #897: Increasing Order Search Tree

Problem Statement:
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

Example 1:
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Example 2:
Input: root = [5,1,7]
Output: [1,null,5,null,7]

Constraints:
- The number of nodes in the given tree will be in the range [1, 100].
- 0 <= Node.val <= 1000
"""

# Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.current.right = TreeNode(node.val)
            self.current = self.current.right
            inorder(node.right)
        
        dummy = TreeNode(-1)
        self.current = dummy
        inorder(root)
        return dummy.right

# Example Test Cases
def build_tree(values):
    """Helper function to build a binary tree from a list of values."""
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    for i, node in enumerate(nodes):
        if node:
            if 2 * i + 1 < len(nodes):
                node.left = nodes[2 * i + 1]
            if 2 * i + 2 < len(nodes):
                node.right = nodes[2 * i + 2]
    return nodes[0]

def print_tree(root):
    """Helper function to print the tree in list format."""
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

# Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    root1 = build_tree([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9])
    result1 = solution.increasingBST(root1)
    print(print_tree(result1))  # Expected Output: [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]

    # Test Case 2
    root2 = build_tree([5, 1, 7])
    result2 = solution.increasingBST(root2)
    print(print_tree(result2))  # Expected Output: [1, None, 5, None, 7]

# Time and Space Complexity Analysis
# Time Complexity:
# The function performs an in-order traversal of the tree, which visits each node exactly once. 
# Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

# Space Complexity:
# The space complexity is O(h), where h is the height of the tree, due to the recursive call stack during the in-order traversal. 
# In the worst case (skewed tree), h = n, and in the best case (balanced tree), h = log(n).
# Additionally, we use O(n) space for the new tree structure.

# Topic: Binary Tree