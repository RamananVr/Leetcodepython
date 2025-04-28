"""
LeetCode Problem #1325: Delete Leaves With a Given Value

Problem Statement:
Given a binary tree root and an integer target, delete all the leaf nodes with the value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf and has the value target, it should also be deleted (you need to continue doing that until you cannot).

Example 1:
Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes with value 2 are removed. For the tree [1,2,3,2,null,2,4], 
             removing the leaf nodes with value 2 results in [1,null,3,null,4].

Example 2:
Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]

Example 3:
Input: root = [1,2,null,2,null,2], target = 2
Output: [1]

Constraints:
- The number of nodes in the tree is in the range [1, 3000].
- 1 <= Node.val, target <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        """
        Recursively remove all leaf nodes with the given target value.
        """
        if not root:
            return None
        
        # Recursively process the left and right subtrees
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        
        # If the current node becomes a leaf and matches the target, remove it
        if not root.left and not root.right and root.val == target:
            return None
        
        return root

# Helper function to build a binary tree from a list (for testing purposes)
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

# Helper function to serialize a binary tree to a list (for testing purposes)
def serialize_tree(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    root1 = build_tree([1, 2, 3, 2, None, 2, 4])
    target1 = 2
    result1 = solution.removeLeafNodes(root1, target1)
    print(serialize_tree(result1))  # Expected Output: [1, None, 3, None, 4]

    # Test Case 2
    root2 = build_tree([1, 3, 3, 3, 2])
    target2 = 3
    result2 = solution.removeLeafNodes(root2, target2)
    print(serialize_tree(result2))  # Expected Output: [1, 3, None, None, 2]

    # Test Case 3
    root3 = build_tree([1, 2, None, 2, None, 2])
    target3 = 2
    result3 = solution.removeLeafNodes(root3, target3)
    print(serialize_tree(result3))  # Expected Output: [1]

    # Test Case 4
    root4 = build_tree([1, 1, 1])
    target4 = 1
    result4 = solution.removeLeafNodes(root4, target4)
    print(serialize_tree(result4))  # Expected Output: []

"""
Time Complexity:
- Each node in the tree is visited once, so the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is O(h), where h is the height of the tree. This is due to the recursive call stack.

Topic: Binary Tree
"""