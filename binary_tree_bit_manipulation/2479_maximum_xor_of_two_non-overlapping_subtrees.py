"""
LeetCode Question #2479: Maximum XOR of Two Non-Overlapping Subtrees

Problem Statement:
You are given the root of a binary tree. Each node in the tree has a value. 
Find the maximum XOR value of two non-overlapping subtrees of the binary tree.

A subtree of a binary tree is a tree that consists of a node in the binary tree and all of its descendants. 
Two subtrees are non-overlapping if they do not share any node.

Return the maximum XOR value of two non-overlapping subtrees.

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- 1 <= Node.val <= 10^9
"""

# Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maximumXOR(self, root: TreeNode) -> int:
        # Helper function to calculate the XOR sum of a subtree
        def calculate_subtree_xor(node):
            if not node:
                return 0
            subtree_xor = node.val ^ calculate_subtree_xor(node.left) ^ calculate_subtree_xor(node.right)
            subtree_xors.append(subtree_xor)
            return subtree_xor

        subtree_xors = []
        calculate_subtree_xor(root)

        # Find the maximum XOR of two non-overlapping subtrees
        max_xor = 0
        for xor1 in subtree_xors:
            for xor2 in subtree_xors:
                if xor1 != xor2:  # Ensure non-overlapping
                    max_xor = max(max_xor, xor1 ^ xor2)

        return max_xor

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(7)
    solution = Solution()
    print(solution.maximumXOR(root1))  # Expected output: Maximum XOR value of two non-overlapping subtrees

    # Example 2
    root2 = TreeNode(8)
    root2.left = TreeNode(3)
    root2.right = TreeNode(10)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(6)
    root2.right.right = TreeNode(14)
    root2.right.right.left = TreeNode(13)
    print(solution.maximumXOR(root2))  # Expected output: Maximum XOR value of two non-overlapping subtrees

# Time and Space Complexity Analysis
"""
Time Complexity:
- The `calculate_subtree_xor` function traverses the entire tree once, which takes O(n), where n is the number of nodes in the tree.
- The nested loop to calculate the maximum XOR value has a complexity of O(m^2), where m is the number of unique subtree XOR values.
- In the worst case, m = n, so the overall complexity is O(n + n^2) = O(n^2).

Space Complexity:
- The `subtree_xors` list stores the XOR values of all subtrees, which takes O(n) space.
- The recursion stack for `calculate_subtree_xor` takes O(h) space, where h is the height of the tree. In the worst case, h = n (for a skewed tree).
- Overall space complexity is O(n).

Topic: Binary Tree, Bit Manipulation
"""