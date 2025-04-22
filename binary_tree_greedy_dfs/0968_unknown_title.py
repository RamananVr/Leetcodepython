"""
LeetCode Problem #968: Binary Tree Cameras

Problem Statement:
You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- Node values are 0.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        """
        This function calculates the minimum number of cameras needed to monitor all nodes in the binary tree.
        """
        # State definitions:
        # 0 -> Node is not covered
        # 1 -> Node has a camera
        # 2 -> Node is covered but does not have a camera

        self.cameras = 0

        def dfs(node):
            if not node:
                return 2  # Null nodes are considered covered

            left = dfs(node.left)
            right = dfs(node.right)

            # If any child is not covered, place a camera at this node
            if left == 0 or right == 0:
                self.cameras += 1
                return 1

            # If any child has a camera, this node is covered
            if left == 1 or right == 1:
                return 2

            # If both children are covered but do not have cameras, this node is not covered
            return 0

        # If the root is not covered, place a camera at the root
        if dfs(root) == 0:
            self.cameras += 1

        return self.cameras

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
    root1 = build_tree([0, 0, None, 0, 0])
    print(Solution().minCameraCover(root1))  # Output: 1

    # Test Case 2
    root2 = build_tree([0, 0, None, 0, None, 0, None, None, 0])
    print(Solution().minCameraCover(root2))  # Output: 2

    # Test Case 3
    root3 = build_tree([0])
    print(Solution().minCameraCover(root3))  # Output: 1

"""
Time Complexity Analysis:
- Each node in the binary tree is visited exactly once during the DFS traversal.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity Analysis:
- The space complexity is determined by the recursion stack, which depends on the height of the tree.
- In the worst case (skewed tree), the height of the tree is O(n), so the space complexity is O(n).
- In the best case (balanced tree), the height of the tree is O(log n), so the space complexity is O(log n).

Topic: Binary Tree, Greedy, DFS
"""