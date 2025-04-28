"""
LeetCode Problem #99: Recover Binary Search Tree

Problem Statement:
You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. 
Recover the tree without changing its structure.

Example 1:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 and 1 are swapped.

Example 2:
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 and 3 are swapped.

Constraints:
- The number of nodes in the tree is in the range [2, 1000].
- -2^31 <= Node.val <= 2^31 - 1

Follow up: A solution using O(n) space is pretty straightforward. Could you devise a constant O(1) space solution?
"""

# Clean, Correct Python Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Initialize variables to track the swapped nodes
        self.first = self.second = self.prev = None

        # Helper function to perform in-order traversal
        def inorder(node):
            if not node:
                return
            
            # Traverse the left subtree
            inorder(node.left)
            
            # Detect swapped nodes
            if self.prev and self.prev.val > node.val:
                # If this is the first violation, mark the first and second nodes
                if not self.first:
                    self.first = self.prev
                # If this is the second violation, mark the second node
                self.second = node
            
            # Update the previous node
            self.prev = node
            
            # Traverse the right subtree
            inorder(node.right)
        
        # Perform in-order traversal to find the swapped nodes
        inorder(root)
        
        # Swap the values of the two nodes to recover the BST
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val

# Example Test Cases
def test_recover_tree():
    # Helper function to build a tree from a list
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

    # Helper function to perform in-order traversal and collect values
    def inorder_traversal(root):
        result = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)
        return result

    # Test Case 1
    root1 = build_tree([1, 3, None, None, 2])
    Solution().recoverTree(root1)
    assert inorder_traversal(root1) == [1, 2, 3], "Test Case 1 Failed"

    # Test Case 2
    root2 = build_tree([3, 1, 4, None, None, 2])
    Solution().recoverTree(root2)
    assert inorder_traversal(root2) == [1, 2, 3, 4], "Test Case 2 Failed"

    # Test Case 3
    root3 = build_tree([2, 3, 1])
    Solution().recoverTree(root3)
    assert inorder_traversal(root3) == [1, 2, 3], "Test Case 3 Failed"

    print("All test cases passed!")

# Run the test cases
if __name__ == "__main__":
    test_recover_tree()

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution performs an in-order traversal of the tree, which takes O(n) time, where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is O(h), where h is the height of the tree, due to the recursive call stack. 
  In the worst case (skewed tree), h = n, and in the best case (balanced tree), h = log(n).

Follow-up:
- The solution provided uses O(h) space. To achieve O(1) space, Morris Traversal can be used.
"""

# Topic: Binary Tree