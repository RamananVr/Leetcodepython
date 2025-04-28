"""
LeetCode Problem #965: Univalued Binary Tree

Problem Statement:
A binary tree is univalued if every node in the tree has the same value.

Given the root of a binary tree, return true if the binary tree is univalued, or false otherwise.

Constraints:
- The number of nodes in the tree is in the range [1, 100].
- 0 <= Node.val < 100

Example 1:
Input: root = [1,1,1,1,1,null,1]
Output: true

Example 2:
Input: root = [2,2,2,5,2]
Output: false
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isUnivalTree(root: TreeNode) -> bool:
    """
    Determines if a binary tree is univalued.
    
    Args:
    root (TreeNode): The root of the binary tree.
    
    Returns:
    bool: True if the binary tree is univalued, False otherwise.
    """
    def dfs(node):
        if not node:
            return True
        if node.val != root.val:
            return False
        return dfs(node.left) and dfs(node.right)
    
    return dfs(root)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Univalued tree
    root1 = TreeNode(1)
    root1.left = TreeNode(1)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(1)
    root1.right.right = TreeNode(1)
    print(isUnivalTree(root1))  # Output: True

    # Test Case 2: Not univalued tree
    root2 = TreeNode(2)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(5)
    root2.left.right = TreeNode(2)
    print(isUnivalTree(root2))  # Output: False

    # Test Case 3: Single node tree
    root3 = TreeNode(3)
    print(isUnivalTree(root3))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function performs a depth-first search (DFS) traversal of the binary tree.
- In the worst case, we visit every node in the tree exactly once.
- Let n be the number of nodes in the tree. The time complexity is O(n).

Space Complexity:
- The space complexity is determined by the recursion stack used during DFS.
- In the worst case (for a skewed tree), the recursion stack can go up to n levels deep.
- In the best case (for a balanced tree), the recursion stack depth is O(log n).
- Therefore, the space complexity is O(n) in the worst case and O(log n) in the best case.

Topic: Binary Tree
"""