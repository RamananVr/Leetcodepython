"""
LeetCode Question #655: Print Binary Tree

Problem Statement:
You are given the root of a binary tree. You need to construct a 2D list where each row represents a level of the tree, 
and each column represents a position in a full binary tree. The goal is to print the binary tree in a 2D format.

The rules for constructing the 2D list are as follows:
1. The height of the tree is `h`. The number of rows in the output list should be `h`, and the number of columns should be `2^h - 1`.
2. The root node (if it exists) should be at the center of the top row.
3. For each node, its left child should be placed in the row below, at the center of the left half of the current node's position.
   Similarly, its right child should be placed in the row below, at the center of the right half of the current node's position.
4. If a node does not exist, it should be represented as an empty string "" in the 2D list.

Return the constructed 2D list.

Constraints:
- The number of nodes in the tree is in the range [1, 2^10].
- -99 <= Node.val <= 99
- The depth of the tree will not exceed 10.

Example:
Input: root = [1, 2]
Output:
[["", "1", ""],
 ["2", "", ""]]

Input: root = [1, 2, 3, None, 4]
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: TreeNode) -> list[list[str]]:
        # Helper function to calculate the height of the tree
        def getHeight(node):
            if not node:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        # Helper function to fill the 2D list
        def fill(res, node, row, col, width):
            if not node:
                return
            res[row][col] = str(node.val)
            if node.left:
                fill(res, node.left, row + 1, col - width // 2, width // 2)
            if node.right:
                fill(res, node.right, row + 1, col + width // 2, width // 2)
        
        # Calculate the height of the tree
        height = getHeight(root)
        # Calculate the width of the 2D list
        width = (1 << height) - 1  # 2^height - 1
        # Initialize the 2D list with empty strings
        res = [["" for _ in range(width)] for _ in range(height)]
        # Fill the 2D list
        fill(res, root, 0, (width - 1) // 2, (width - 1) // 2)
        return res

# Example Test Cases
if __name__ == "__main__":
    # Helper function to build a binary tree from a list
    def buildTree(values):
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
    root1 = buildTree([1, 2])
    print(Solution().printTree(root1))
    # Expected Output:
    # [["", "1", ""],
    #  ["2", "", ""]]

    # Test Case 2
    root2 = buildTree([1, 2, 3, None, 4])
    print(Solution().printTree(root2))
    # Expected Output:
    # [["", "", "", "1", "", "", ""],
    #  ["", "2", "", "", "", "3", ""],
    #  ["", "", "4", "", "", "", ""]]

    # Test Case 3
    root3 = buildTree([1])
    print(Solution().printTree(root3))
    # Expected Output:
    # [["1"]]

"""
Time Complexity:
- Calculating the height of the tree: O(n), where n is the number of nodes in the tree.
- Filling the 2D list: O(n), as we visit each node once.
- Overall: O(n).

Space Complexity:
- The 2D list requires O(h * (2^h - 1)) space, where h is the height of the tree.
- The recursion stack requires O(h) space for the depth of the tree.
- Overall: O(h * (2^h - 1)).

Topic: Binary Tree
"""