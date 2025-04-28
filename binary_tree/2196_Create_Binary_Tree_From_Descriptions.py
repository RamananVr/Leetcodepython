"""
LeetCode Problem #2196: Create Binary Tree From Descriptions

Problem Statement:
You are given a 2D integer array `descriptions` where each `descriptions[i] = [parent, child, isLeft]` indicates that:
- `parent` is the parent of `child`.
- If `isLeft == 1`, then `child` is the left child of `parent`.
- If `isLeft == 0`, then `child` is the right child of `parent`.

The binary tree described by `descriptions` may have multiple nodes with the same value, but no two nodes with the same value will have different parents. The binary tree will always have at least one node, and there will be no cycles in the binary tree.

Return the root of the binary tree after creating it.

Example 1:
Input: descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0]]
Output: [50, 20, 80, 15, 17]
Explanation: The root node is 50, and its left and right children are 20 and 80, respectively. Node 20's left and right children are 15 and 17, respectively.

Example 2:
Input: descriptions = [[1, 2, 1], [2, 3, 0], [3, 4, 1]]
Output: [1, 2, null, null, 3, 4]
Explanation: The root node is 1, and its left child is 2. Node 2's right child is 3, and Node 3's left child is 4.

Constraints:
- 1 <= descriptions.length <= 10^4
- descriptions[i].length == 3
- 1 <= parent, child <= 10^5
- 0 <= isLeft <= 1
- The binary tree described by `descriptions` is valid.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createBinaryTree(descriptions):
    """
    Function to create a binary tree from the given descriptions.
    """
    from collections import defaultdict

    # Dictionary to store nodes by their values
    nodes = {}
    # Set to track all child nodes
    children = set()

    # Create nodes and establish parent-child relationships
    for parent, child, isLeft in descriptions:
        # Create parent node if it doesn't exist
        if parent not in nodes:
            nodes[parent] = TreeNode(parent)
        # Create child node if it doesn't exist
        if child not in nodes:
            nodes[child] = TreeNode(child)
        # Establish the relationship
        if isLeft:
            nodes[parent].left = nodes[child]
        else:
            nodes[parent].right = nodes[child]
        # Add child to the set of children
        children.add(child)

    # The root is the node that is not a child of any other node
    for parent, _, _ in descriptions:
        if parent not in children:
            return nodes[parent]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    descriptions1 = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0]]
    root1 = createBinaryTree(descriptions1)
    # Expected Output: [50, 20, 80, 15, 17]
    print(root1.val)  # 50
    print(root1.left.val)  # 20
    print(root1.right.val)  # 80
    print(root1.left.left.val)  # 15
    print(root1.left.right.val)  # 17

    # Test Case 2
    descriptions2 = [[1, 2, 1], [2, 3, 0], [3, 4, 1]]
    root2 = createBinaryTree(descriptions2)
    # Expected Output: [1, 2, null, null, 3, 4]
    print(root2.val)  # 1
    print(root2.left.val)  # 2
    print(root2.left.right.val)  # 3
    print(root2.left.right.left.val)  # 4

"""
Time Complexity:
- Creating nodes and establishing relationships: O(n), where n is the number of descriptions.
- Finding the root: O(n).
- Overall: O(n).

Space Complexity:
- Dictionary to store nodes: O(n), where n is the number of unique nodes.
- Set to track child nodes: O(n).
- Overall: O(n).

Topic: Binary Tree
"""