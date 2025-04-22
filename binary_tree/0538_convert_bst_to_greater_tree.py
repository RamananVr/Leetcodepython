"""
LeetCode Question #538: Convert BST to Greater Tree

Problem Statement:
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the sum of all keys greater than or equal to the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Example 2:
Input: root = [0,null,1]
Output: [1,null,1]

Constraints:
- The number of nodes in the tree is in the range [1, 100].
- 0 <= Node.val <= 10^4
- The tree is guaranteed to be a binary search tree.

Follow-up:
Can you do it without using extra space (i.e., O(1) space complexity)?
"""

# Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        Convert BST to Greater Tree using reverse in-order traversal.
        """
        self.sum = 0  # Initialize a variable to store the cumulative sum
        
        def reverse_inorder(node):
            if not node:
                return
            # Traverse the right subtree first
            reverse_inorder(node.right)
            # Update the current node's value
            self.sum += node.val
            node.val = self.sum
            # Traverse the left subtree
            reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root

# Example Test Cases
def print_tree(root):
    """Helper function to print the tree in level order."""
    if not root:
        return []
    from collections import deque
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()
    return result

if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(4)
    root1.left = TreeNode(1)
    root1.right = TreeNode(6)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(2)
    root1.left.right.right = TreeNode(3)
    root1.right.left = TreeNode(5)
    root1.right.right = TreeNode(7)
    root1.right.right.right = TreeNode(8)
    
    solution = Solution()
    new_root1 = solution.convertBST(root1)
    print(print_tree(new_root1))  # Output: [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]

    # Example 2
    root2 = TreeNode(0)
    root2.right = TreeNode(1)
    
    new_root2 = solution.convertBST(root2)
    print(print_tree(new_root2))  # Output: [1, None, 1]

# Time and Space Complexity Analysis
"""
Time Complexity:
The algorithm performs a reverse in-order traversal of the BST, visiting each node exactly once.
Thus, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
The algorithm uses O(h) space for the recursion stack, where h is the height of the tree.
In the worst case (for a skewed tree), h = n, so the space complexity is O(n).
In the best case (for a balanced tree), h = log(n), so the space complexity is O(log(n)).
No additional data structures are used, so the space complexity is dominated by the recursion stack.
"""

# Topic: Binary Tree