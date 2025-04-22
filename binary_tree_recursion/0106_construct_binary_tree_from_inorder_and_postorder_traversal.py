"""
LeetCode Question #106: Construct Binary Tree from Inorder and Postorder Traversal

Problem Statement:
Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]

Constraints:
- `1 <= inorder.length <= 3000`
- `postorder.length == inorder.length`
- `-3000 <= inorder[i], postorder[i] <= 3000`
- `inorder` and `postorder` consist of unique values.
- Each value of `postorder` also appears in `inorder`.
- `inorder` is guaranteed to be the inorder traversal of the tree.
- `postorder` is guaranteed to be the postorder traversal of the tree.
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Base case: if either list is empty, return None
        if not inorder or not postorder:
            return None
        
        # The last element of postorder is the root of the current subtree
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        # Find the index of the root in the inorder list
        root_index = inorder.index(root_val)
        
        # Recursively build the right subtree using the portion of inorder and postorder
        root.right = self.buildTree(inorder[root_index + 1:], postorder)
        
        # Recursively build the left subtree using the portion of inorder and postorder
        root.left = self.buildTree(inorder[:root_index], postorder)
        
        return root

# Helper function to print the tree in level-order for testing
def level_order_traversal(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
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
    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()
    return result

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    inorder1 = [9, 3, 15, 20, 7]
    postorder1 = [9, 15, 7, 20, 3]
    root1 = solution.buildTree(inorder1, postorder1)
    print(level_order_traversal(root1))  # Output: [3, 9, 20, None, None, 15, 7]
    
    # Test Case 2
    inorder2 = [-1]
    postorder2 = [-1]
    root2 = solution.buildTree(inorder2, postorder2)
    print(level_order_traversal(root2))  # Output: [-1]

"""
Time Complexity:
- The `index` operation on the `inorder` list takes O(n) in the worst case.
- Each recursive call processes a smaller portion of the `inorder` and `postorder` lists.
- In total, the time complexity is O(n^2) in the worst case due to the repeated `index` lookups.

Space Complexity:
- The recursion stack can go as deep as the height of the tree. In the worst case (skewed tree), this is O(n).
- Additionally, the `inorder` and `postorder` slices create new lists, which also take O(n) space in total.
- Overall space complexity: O(n).

Topic: Binary Tree, Recursion
"""