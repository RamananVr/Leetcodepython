"""
LeetCode Problem #971: Flip Binary Tree To Match Preorder Traversal

Problem Statement:
You are given the root of a binary tree with `n` nodes, where each node is uniquely assigned a value from `1` to `n`. 
You are also given an integer array `voyage` representing the desired preorder traversal of the binary tree.

Any node in the binary tree can be flipped by swapping its left and right subtrees. For example, flipping the node with value `1` will have the following effect:
    - The left child of node `1` becomes the right child.
    - The right child of node `1` becomes the left child.

Return a list of the values of all nodes that need to be flipped in order to match the preorder traversal given by `voyage`. 
If it is impossible to match the preorder traversal, return the list `[-1]`.

Example 1:
Input: root = [1,2], voyage = [2,1]
Output: [-1]

Example 2:
Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]

Example 3:
Input: root = [1,2,3], voyage = [1,2,3]
Output: []

Constraints:
- The number of nodes in the tree is `n`.
- `n == voyage.length`
- `1 <= n <= 100`
- `1 <= Node.val, voyage[i] <= n`
- All the values in the tree are unique.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flipMatchVoyage(root: TreeNode, voyage: list[int]) -> list[int]:
    """
    Function to determine the nodes to flip to match the given preorder traversal.
    """
    flips = []
    index = 0

    def dfs(node):
        nonlocal index
        if not node:
            return True
        if node.val != voyage[index]:
            return False
        index += 1
        if node.left and node.left.val != voyage[index]:
            flips.append(node.val)
            return dfs(node.right) and dfs(node.left)
        return dfs(node.left) and dfs(node.right)

    return flips if dfs(root) else [-1]

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
    root1 = build_tree([1, 2])
    voyage1 = [2, 1]
    print(flipMatchVoyage(root1, voyage1))  # Output: [-1]

    # Test Case 2
    root2 = build_tree([1, 2, 3])
    voyage2 = [1, 3, 2]
    print(flipMatchVoyage(root2, voyage2))  # Output: [1]

    # Test Case 3
    root3 = build_tree([1, 2, 3])
    voyage3 = [1, 2, 3]
    print(flipMatchVoyage(root3, voyage3))  # Output: []

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function performs a depth-first traversal of the binary tree, visiting each node exactly once.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack used during the DFS traversal.
- In the worst case, the recursion stack can grow to O(n) if the tree is skewed (all nodes have only one child).
- Additionally, the `flips` list stores the nodes to be flipped, which can contain up to O(n) elements in the worst case.
- Overall space complexity: O(n).

Topic: Binary Tree
"""