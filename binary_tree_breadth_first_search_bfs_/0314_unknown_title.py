"""
LeetCode Problem #314: Binary Tree Vertical Order Traversal

Problem Statement:
Given the `root` of a binary tree, return the vertical order traversal of its nodes' values. 
(i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Example 2:
Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]

Example 3:
Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- `-100 <= Node.val <= 100`
"""

from collections import defaultdict, deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Dictionary to store nodes grouped by their column index
        column_table = defaultdict(list)
        # Queue for BFS traversal, storing pairs of (node, column_index)
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()
            if node:
                # Append the node's value to the corresponding column index
                column_table[column].append(node.val)
                # Add left and right children to the queue with updated column indices
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        # Sort the columns and return the values in sorted order
        return [column_table[col] for col in sorted(column_table.keys())]

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
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print(Solution().verticalOrder(root1))  # Output: [[9], [3, 15], [20], [7]]

    # Test Case 2
    root2 = build_tree([3, 9, 8, 4, 0, 1, 7])
    print(Solution().verticalOrder(root2))  # Output: [[4], [9], [3, 0, 1], [8], [7]]

    # Test Case 3
    root3 = build_tree([3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5])
    print(Solution().verticalOrder(root3))  # Output: [[4], [9, 5], [3, 0, 1], [8, 2], [7]]

"""
Time Complexity:
- The BFS traversal visits each node exactly once, so the time complexity is O(N), 
  where N is the number of nodes in the tree.
- Sorting the column indices takes O(K log K), where K is the number of unique columns.
- Overall time complexity: O(N + K log K).

Space Complexity:
- The space required for the queue is O(N) in the worst case (when all nodes are in the queue).
- The space required for the column_table is O(N) to store all node values.
- Overall space complexity: O(N).

Topic: Binary Tree, Breadth-First Search (BFS)
"""