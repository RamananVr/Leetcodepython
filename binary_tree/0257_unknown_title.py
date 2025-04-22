"""
LeetCode Problem #257: Binary Tree Paths

Problem Statement:
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]

Constraints:
- The number of nodes in the tree is in the range [1, 100].
- -100 <= Node.val <= 100
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        def dfs(node, path, result):
            if not node:
                return
            # Append current node's value to the path
            path.append(str(node.val))
            # If it's a leaf node, add the path to the result
            if not node.left and not node.right:
                result.append("->".join(path))
            else:
                # Continue DFS on left and right children
                dfs(node.left, path, result)
                dfs(node.right, path, result)
            # Backtrack to explore other paths
            path.pop()

        result = []
        dfs(root, [], result)
        return result

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
    root1 = build_tree([1, 2, 3, None, 5])
    print(Solution().binaryTreePaths(root1))  # Output: ["1->2->5", "1->3"]

    # Test Case 2
    root2 = build_tree([1])
    print(Solution().binaryTreePaths(root2))  # Output: ["1"]

    # Test Case 3
    root3 = build_tree([1, 2, None, 3, None, None, None, 4])
    print(Solution().binaryTreePaths(root3))  # Output: ["1->2->3->4"]

"""
Time Complexity:
- Each node is visited exactly once, and for each node, we perform a constant amount of work (appending to the path, checking if it's a leaf, etc.).
- Therefore, the time complexity is O(N), where N is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack and the space used to store the paths.
- The recursion stack can go as deep as the height of the tree, which is O(H), where H is the height of the tree.
- In the worst case, the height of the tree is O(N) (e.g., a skewed tree).
- Additionally, the result list stores all the paths, which can take up to O(N) space in the worst case.
- Therefore, the overall space complexity is O(N).

Topic: Binary Tree
"""