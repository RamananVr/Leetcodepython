"""
LeetCode Question #987: Vertical Order Traversal of a Binary Tree

Problem Statement:
Given the `root` of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position `(row, col)`, its left and right children will be at positions `(row + 1, col - 1)` and `(row + 1, col + 1)` respectively. The root of the tree is at `(0, 0)`.

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending at the rightmost column. If two nodes are in the same row and column, the order should be from smallest to largest value.

Return the vertical order traversal of the binary tree.

Constraints:
- The number of nodes in the tree is in the range `[1, 1000]`.
- `-1000 <= Node.val <= 1000`

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Explanation:
- Column -1: [9]
- Column  0: [3, 15]
- Column  1: [20]
- Column  2: [7]
"""

from collections import defaultdict, deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalTraversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Perform vertical order traversal of a binary tree.
    """
    if not root:
        return []

    # Dictionary to store nodes grouped by column index
    column_table = defaultdict(list)

    # Queue for BFS traversal: stores (node, row, column)
    queue = deque([(root, 0, 0)])

    while queue:
        node, row, col = queue.popleft()
        if node:
            # Append the node's value along with its row and column
            column_table[col].append((row, node.val))
            # Add left and right children to the queue
            queue.append((node.left, row + 1, col - 1))
            queue.append((node.right, row + 1, col + 1))

    # Sort the columns based on their index
    sorted_columns = sorted(column_table.keys())

    result = []
    for col in sorted_columns:
        # Sort the nodes in each column by (row, value)
        column_table[col].sort(key=lambda x: (x[0], x[1]))
        # Extract the values and append to the result
        result.append([val for _, val in column_table[col]])

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
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print(verticalTraversal(root1))  # Output: [[9], [3, 15], [20], [7]]

    # Test Case 2
    root2 = build_tree([1, 2, 3, 4, 5, 6, 7])
    print(verticalTraversal(root2))  # Output: [[4], [2], [1, 5, 6], [3], [7]]

    # Test Case 3
    root3 = build_tree([1, 2, 3, 4, 6, 5, 7])
    print(verticalTraversal(root3))  # Output: [[4], [2], [1, 5, 6], [3], [7]]

"""
Time Complexity:
- The BFS traversal visits each node once, so it takes O(N), where N is the number of nodes in the tree.
- Sorting the nodes within each column takes O(N log N) in the worst case.
- Sorting the column indices takes O(K log K), where K is the number of unique columns (K <= N).
- Overall time complexity: O(N log N).

Space Complexity:
- The space required for the column_table dictionary is O(N).
- The queue for BFS traversal can hold up to O(N) nodes in the worst case.
- Overall space complexity: O(N).

Topic: Binary Tree
"""