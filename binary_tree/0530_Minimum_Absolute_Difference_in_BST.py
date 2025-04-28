"""
LeetCode Problem #530: Minimum Absolute Difference in BST

Problem Statement:
Given the root of a Binary Search Tree (BST), return the minimum absolute difference 
between the values of any two nodes in the tree.

Constraints:
- The number of nodes in the tree is in the range [2, 10^4].
- 0 <= Node.val <= 10^5

Note:
A BST is a binary tree in which for each node, all the values in its left subtree are 
less than the node's value, and all the values in its right subtree are greater than 
the node's value.

Example:
Input: root = [4,2,6,1,3]
Output: 1
Explanation: The minimum absolute difference is between nodes 2 and 3.

Input: root = [1,0,48,null,null,12,49]
Output: 1
Explanation: The minimum absolute difference is between nodes 48 and 49.
"""

# Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getMinimumDifference(root: TreeNode) -> int:
    """
    This function computes the minimum absolute difference between values of any two nodes in a BST.
    """
    # In-order traversal of BST gives sorted values
    def in_order_traversal(node):
        if not node:
            return []
        return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
    
    # Perform in-order traversal to get sorted values
    sorted_values = in_order_traversal(root)
    
    # Compute the minimum absolute difference between consecutive values
    min_diff = float('inf')
    for i in range(1, len(sorted_values)):
        min_diff = min(min_diff, sorted_values[i] - sorted_values[i - 1])
    
    return min_diff

# Example Test Cases
if __name__ == "__main__":
    # Helper function to build a tree from a list
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
    root1 = build_tree([4, 2, 6, 1, 3])
    print(getMinimumDifference(root1))  # Output: 1

    # Test Case 2
    root2 = build_tree([1, 0, 48, None, None, 12, 49])
    print(getMinimumDifference(root2))  # Output: 1

    # Test Case 3
    root3 = build_tree([10, 5, 15, None, None, None, 20])
    print(getMinimumDifference(root3))  # Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- The in-order traversal visits each node exactly once, so the traversal takes O(n) time, 
  where n is the number of nodes in the BST.
- Computing the minimum absolute difference from the sorted values takes O(n) time.
- Overall time complexity: O(n).

Space Complexity:
- The in-order traversal uses O(n) space to store the sorted values.
- The recursion stack for in-order traversal has a maximum depth of O(h), where h is the 
  height of the tree. In the worst case (skewed tree), h = O(n).
- Overall space complexity: O(n).

Topic: Binary Tree
"""