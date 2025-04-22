"""
LeetCode Question #938: Range Sum of BST

Problem Statement:
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

A binary search tree (BST) is a tree in which all left descendants of a node are less than the node, and all right descendants are greater than the node.

Constraints:
- The number of nodes in the tree is in the range [1, 2 * 10^4].
- 1 <= Node.val <= 10^5
- 1 <= low <= high <= 10^5
- All Node.val are unique.

Example:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes with values 7, 10, and 15 are in the range [7, 15]. Sum = 7 + 10 + 15 = 32.

Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes with values 6 and 10 are in the range [6, 10]. Sum = 6 + 10 = 23.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
    """
    Function to calculate the sum of all nodes in the range [low, high] in a BST.
    """
    if not root:
        return 0
    
    # If the current node's value is less than the low range, skip the left subtree
    if root.val < low:
        return rangeSumBST(root.right, low, high)
    
    # If the current node's value is greater than the high range, skip the right subtree
    if root.val > high:
        return rangeSumBST(root.left, low, high)
    
    # If the current node's value is within the range, include it in the sum
    return root.val + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high)

# Example Test Cases
def test_rangeSumBST():
    # Helper function to build a binary tree from a list
    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        for i, node in enumerate(nodes):
            if node:
                if 2 * i + 1 < len(nodes):
                    node.left = nodes[2 * i + 1]
                if 2 * i + 2 < len(nodes):
                    node.right = nodes[2 * i + 2]
        return nodes[0]

    # Test Case 1
    root1 = build_tree([10, 5, 15, 3, 7, None, 18])
    low1, high1 = 7, 15
    assert rangeSumBST(root1, low1, high1) == 32

    # Test Case 2
    root2 = build_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
    low2, high2 = 6, 10
    assert rangeSumBST(root2, low2, high2) == 23

    # Test Case 3
    root3 = build_tree([5, 3, 8, 2, 4, None, 10])
    low3, high3 = 4, 10
    assert rangeSumBST(root3, low3, high3) == 22

    print("All test cases passed!")

# Run the test cases
test_rangeSumBST()

"""
Time and Space Complexity Analysis:

Time Complexity:
- In the worst case, we visit every node in the tree once. This happens when all nodes fall within the range [low, high].
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack. In the worst case, the height of the tree is O(n) (for a skewed tree).
- In the best case (balanced tree), the height of the tree is O(log n).
- Therefore, the space complexity is O(h), where h is the height of the tree.

Topic: Binary Tree
"""