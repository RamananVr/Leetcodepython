"""
LeetCode Problem #2265: Count Nodes Equal to Average of Subtree

Problem Statement:
Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

- The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
- A subtree of root is a tree consisting of root and all its descendants.

Constraints:
1. The number of nodes in the tree is in the range [1, 1000].
2. 0 <= Node.val <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodesEqualToAverage(root: TreeNode) -> int:
    """
    Function to count the number of nodes where the value of the node is equal to the average of its subtree.
    """
    def dfs(node):
        """
        Perform a post-order traversal to calculate the sum and count of nodes in the subtree.
        """
        if not node:
            return (0, 0, 0)  # (sum, count, matching_nodes)

        left_sum, left_count, left_matches = dfs(node.left)
        right_sum, right_count, right_matches = dfs(node.right)

        # Calculate the sum and count for the current subtree
        subtree_sum = left_sum + right_sum + node.val
        subtree_count = left_count + right_count + 1

        # Check if the current node's value matches the average of its subtree
        if node.val == subtree_sum // subtree_count:
            matches = 1
        else:
            matches = 0

        # Return the updated values
        return (subtree_sum, subtree_count, left_matches + right_matches + matches)

    # Start DFS from the root
    _, _, total_matches = dfs(root)
    return total_matches

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(4)
    root1.left = TreeNode(8)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(1)
    root1.right.right = TreeNode(6)
    print(countNodesEqualToAverage(root1))  # Output: 5

    # Example 2
    root2 = TreeNode(1)
    print(countNodesEqualToAverage(root2))  # Output: 1

    # Example 3
    root3 = TreeNode(0)
    root3.left = TreeNode(0)
    root3.right = TreeNode(0)
    print(countNodesEqualToAverage(root3))  # Output: 3

"""
Time Complexity:
- Each node in the tree is visited exactly once during the DFS traversal.
- For each node, we perform constant-time operations to calculate the sum, count, and check the condition.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack during the DFS traversal.
- In the worst case (for a skewed tree), the recursion stack can go up to O(n).
- In the best case (for a balanced tree), the recursion stack is O(log n).
- Therefore, the space complexity is O(n) in the worst case.

Topic: Binary Tree
"""