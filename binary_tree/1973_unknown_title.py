"""
LeetCode Problem #1973: Count Nodes Equal to Sum of Descendants

Problem Statement:
You are given the root of a binary tree. A node is considered "good" if the value of the node is equal to the sum of the values of its descendants. A node's descendants are the nodes that are below it in the tree.

Return the number of "good" nodes in the tree.

Example:
Input: root = [10,3,4,2,1]
Output: 2
Explanation:
- The root node (10) is "good" because 3 + 4 + 2 + 1 = 10.
- The node with value 4 is "good" because it has no descendants, so the sum is 0, and 4 == 0 + 4.
- The node with value 3 is not "good" because 2 + 1 != 3.
- The node with value 2 is "good" because it has no descendants, so the sum is 0, and 2 == 0 + 2.
- The node with value 1 is "good" because it has no descendants, so the sum is 0, and 1 == 0 + 1.
Thus, there are 2 "good" nodes.

Constraints:
- The number of nodes in the tree is in the range [1, 10^5].
- 0 <= Node.val <= 10^5
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodesEqualToSumOfDescendants(self, root: TreeNode) -> int:
        """
        This function returns the number of "good" nodes in the binary tree.
        """
        self.good_nodes_count = 0

        def dfs(node):
            if not node:
                return 0  # Base case: if the node is None, its sum is 0

            # Recursively calculate the sum of descendants for left and right subtrees
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # Calculate the total sum of descendants for the current node
            total_sum = left_sum + right_sum

            # Check if the current node is "good"
            if node.val == total_sum:
                self.good_nodes_count += 1

            # Return the sum of the current node and its descendants
            return total_sum + node.val

        # Start DFS traversal from the root
        dfs(root)

        return self.good_nodes_count

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
    root1 = build_tree([10, 3, 4, 2, 1])
    solution = Solution()
    print(solution.countNodesEqualToSumOfDescendants(root1))  # Output: 2

    # Test Case 2
    root2 = build_tree([5, 3, 2, None, None, None, None])
    print(solution.countNodesEqualToSumOfDescendants(root2))  # Output: 0

    # Test Case 3
    root3 = build_tree([0])
    print(solution.countNodesEqualToSumOfDescendants(root3))  # Output: 1

"""
Time Complexity Analysis:
- Each node in the binary tree is visited exactly once during the DFS traversal.
- For each node, we perform constant-time operations (addition and comparison).
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity Analysis:
- The space complexity is determined by the recursion stack used in the DFS traversal.
- In the worst case (for a skewed tree), the recursion stack can go up to O(n).
- In the best case (for a balanced tree), the recursion stack is O(log n).
- Therefore, the space complexity is O(n) in the worst case and O(log n) in the best case.

Topic: Binary Tree
"""