"""
LeetCode Problem #508: Most Frequent Subtree Sum

Problem Statement:
Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). The frequency of a subtree sum is the number of times the sum occurs in the tree.

Example 1:
Input: root = [5,2,-3]
Output: [2,-3,4]

Example 2:
Input: root = [5,2,-5]
Output: [2]

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5
"""

from collections import Counter
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return 0
            # Calculate the subtree sum recursively
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            subtree_sum = node.val + left_sum + right_sum
            # Record the subtree sum frequency
            count[subtree_sum] += 1
            return subtree_sum
        
        # Counter to store frequency of each subtree sum
        count = Counter()
        dfs(root)
        
        # Find the maximum frequency
        max_freq = max(count.values())
        
        # Return all subtree sums with the maximum frequency
        return [key for key, freq in count.items() if freq == max_freq]

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
    root1 = build_tree([5, 2, -3])
    print(Solution().findFrequentTreeSum(root1))  # Output: [2, -3, 4]

    # Test Case 2
    root2 = build_tree([5, 2, -5])
    print(Solution().findFrequentTreeSum(root2))  # Output: [2]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The `dfs` function visits each node exactly once, so the time complexity is O(n), where n is the number of nodes in the tree.
- Calculating the maximum frequency and filtering the results takes O(k), where k is the number of unique subtree sums. In the worst case, k = n.
- Overall time complexity: O(n).

Space Complexity:
- The `count` dictionary stores the frequency of subtree sums, which can have at most n unique entries. Thus, the space complexity for `count` is O(n).
- The recursion stack in the `dfs` function can go as deep as the height of the tree. In the worst case (skewed tree), the height is O(n). In the best case (balanced tree), the height is O(log n).
- Overall space complexity: O(n).

Topic: Binary Tree
"""