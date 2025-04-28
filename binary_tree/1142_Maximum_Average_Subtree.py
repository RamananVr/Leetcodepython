"""
LeetCode Problem #1142: Maximum Average Subtree

Problem Statement:
Given the root of a binary tree, find the maximum average value of any subtree of that tree. 
(A subtree of a tree is any node of that tree plus all its descendants. The average value of a 
tree is the sum of its values, divided by the number of nodes.)

You are guaranteed that the tree has at least one node.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 0 <= Node.val <= 10^5
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        """
        This function calculates the maximum average value of any subtree in the binary tree.
        """
        self.max_average = 0  # To store the maximum average found

        def dfs(node):
            """
            Perform a post-order traversal to calculate the sum and count of nodes for each subtree.
            """
            if not node:
                return (0, 0)  # (sum, count)

            # Recursively calculate for left and right subtrees
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            # Calculate the sum and count for the current subtree
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1

            # Calculate the average for the current subtree
            current_average = current_sum / current_count

            # Update the maximum average if the current one is greater
            self.max_average = max(self.max_average, current_average)

            return (current_sum, current_count)

        dfs(root)  # Start DFS traversal from the root
        return self.max_average


# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(5)
    root1.left = TreeNode(6)
    root1.right = TreeNode(1)
    print(Solution().maximumAverageSubtree(root1))  # Output: 6.0

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.right = TreeNode(6)
    print(Solution().maximumAverageSubtree(root2))  # Output: 4.666666666666667

    # Example 3
    root3 = TreeNode(10)
    print(Solution().maximumAverageSubtree(root3))  # Output: 10.0


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm performs a single DFS traversal of the binary tree.
- Each node is visited exactly once, and the operations at each node (sum, count, average) take O(1) time.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack used during the DFS traversal.
- In the worst case (for a skewed tree), the recursion stack can go up to O(n).
- In the best case (for a balanced tree), the recursion stack depth is O(log n).
- Therefore, the space complexity is O(n) in the worst case and O(log n) in the best case.

Topic: Binary Tree
"""