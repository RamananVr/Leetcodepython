"""
LeetCode Problem #1448: Count Good Nodes in Binary Tree

Problem Statement:
Given a binary tree root, a node X in the tree is named "good" if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Constraints:
- The number of nodes in the binary tree is in the range [1, 10^5].
- Each node's value is in the range [-10^4, 10^4].
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root: TreeNode) -> int:
    """
    Function to count the number of good nodes in a binary tree.
    """
    def dfs(node, max_val):
        if not node:
            return 0
        
        # Check if the current node is a "good" node
        is_good = node.val >= max_val
        count = 1 if is_good else 0
        
        # Update the maximum value seen so far
        max_val = max(max_val, node.val)
        
        # Recur for left and right subtrees
        count += dfs(node.left, max_val)
        count += dfs(node.right, max_val)
        
        return count
    
    # Start DFS with the root node and its value as the initial max_val
    return dfs(root, root.val)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.left = TreeNode(3)
    root1.right.left = TreeNode(1)
    root1.right.right = TreeNode(5)
    print(goodNodes(root1))  # Output: 4

    # Test Case 2
    root2 = TreeNode(3)
    print(goodNodes(root2))  # Output: 1

    # Test Case 3
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)
    print(goodNodes(root3))  # Output: 3

"""
Time Complexity:
- Each node in the binary tree is visited exactly once during the DFS traversal.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack in the DFS traversal.
- In the worst case (for a skewed tree), the recursion stack can go up to O(n).
- In the best case (for a balanced tree), the recursion stack will be O(log n).
- Therefore, the space complexity is O(h), where h is the height of the tree.

Topic: Binary Tree
"""