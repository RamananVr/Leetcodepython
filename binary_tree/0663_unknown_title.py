"""
LeetCode Problem #663: Equal Tree Partition

Problem Statement:
Given the root of a binary tree, return true if you can partition the tree into two trees with equal sum of values after removing exactly one edge on the original tree.

Example 1:
Input: root = [1, 2, 10, null, null, null, 20]
Output: true
Explanation: Remove the edge between 10 and 20 to get two trees with sums 33 and 33.

Example 2:
Input: root = [1, 2, 10, null, null, null, 15]
Output: false
Explanation: No edge can be removed to partition the tree into two trees with equal sum.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkEqualTree(root: TreeNode) -> bool:
    """
    Function to determine if the binary tree can be partitioned into two trees with equal sum.
    """
    def tree_sum(node):
        if not node:
            return 0
        total = node.val + tree_sum(node.left) + tree_sum(node.right)
        subtree_sums.append(total)
        return total

    subtree_sums = []
    total_sum = tree_sum(root)
    
    # If the total sum is odd, it cannot be split into two equal parts
    if total_sum % 2 != 0:
        return False
    
    # Check if half of the total sum exists in the subtree sums
    target = total_sum // 2
    # Exclude the total sum itself (last element in subtree_sums) since removing the root is not valid
    return target in subtree_sums[:-1]

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(10)
    root1.right.right = TreeNode(20)
    print(checkEqualTree(root1))  # Output: True

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(10)
    root2.right.right = TreeNode(15)
    print(checkEqualTree(root2))  # Output: False

    # Additional Test Case
    root3 = TreeNode(0)
    root3.left = TreeNode(-1)
    root3.right = TreeNode(1)
    print(checkEqualTree(root3))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function `tree_sum` traverses the entire tree once to calculate the sum of all nodes and stores the sum of each subtree.
- This traversal takes O(n), where n is the number of nodes in the tree.

Space Complexity:
- The `subtree_sums` list stores the sum of all subtrees, which can have at most n elements.
- The recursion stack for `tree_sum` can go as deep as the height of the tree, which is O(h), where h is the height of the tree.
- In the worst case (skewed tree), h = n. Therefore, the space complexity is O(n).

Topic: Binary Tree
"""