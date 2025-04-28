"""
LeetCode Problem #366: Find Leaves of Binary Tree

Problem Statement:
Given the root of a binary tree, collect a tree's nodes as if you were doing this:
- Collect all the leaf nodes.
- Remove all the leaf nodes.
- Repeat until the tree is empty.

Return a list of lists where each list contains the values of the leaves removed in each step.

Example 1:
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
- Removing the leaves [4, 5, 3] would result in the tree [1, 2].
- Removing the leaves [2] would result in the tree [1].
- Removing the leaves [1] would result in the tree [].

Example 2:
Input: root = [1]
Output: [[1]]

Constraints:
- The number of nodes in the tree is in the range [1, 100].
- -100 <= Node.val <= 100
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findLeaves(root):
    """
    Function to find the leaves of a binary tree in a step-by-step manner.
    Args:
    root (TreeNode): The root of the binary tree.

    Returns:
    List[List[int]]: A list of lists where each list contains the values of the leaves removed in each step.
    """
    result = []

    def dfs(node):
        if not node:
            return -1
        # Recursively find the height of the left and right subtrees
        left_height = dfs(node.left)
        right_height = dfs(node.right)
        # The height of the current node is the max of left and right heights + 1
        current_height = max(left_height, right_height) + 1
        # If the current height is not in the result list, add a new list
        if current_height == len(result):
            result.append([])
        # Append the current node's value to the corresponding height list
        result[current_height].append(node.val)
        return current_height

    dfs(root)
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
    root1 = build_tree([1, 2, 3, 4, 5])
    print(findLeaves(root1))  # Output: [[4, 5, 3], [2], [1]]

    # Test Case 2
    root2 = build_tree([1])
    print(findLeaves(root2))  # Output: [[1]]

    # Test Case 3
    root3 = build_tree([1, 2, 3, None, None, 4, 5])
    print(findLeaves(root3))  # Output: [[4, 5], [2, 3], [1]]

"""
Time Complexity:
- Each node is visited exactly once during the DFS traversal, so the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is O(h), where h is the height of the tree, due to the recursive call stack.

Topic: Binary Tree
"""