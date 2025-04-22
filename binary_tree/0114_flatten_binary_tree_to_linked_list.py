"""
LeetCode Question #114: Flatten Binary Tree to Linked List

Problem Statement:
Given the `root` of a binary tree, flatten the tree into a "linked list":
- The "linked list" should use the same `TreeNode` class where the `right` child pointer points to the next node in the list and the `left` child pointer is always `None`.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -100 <= Node.val <= 100

Example:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Input: root = []
Output: []

Input: root = [0]
Output: [0]

Follow-up:
Can you flatten the tree in-place (with O(1) extra space)?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Flattens the binary tree into a linked list in-place.
        """
        if not root:
            return
        
        # Start from the root and traverse the tree
        current = root
        while current:
            if current.left:
                # Find the rightmost node in the left subtree
                rightmost = current.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                # Connect the right subtree to the rightmost node
                rightmost.right = current.right
                
                # Move the left subtree to the right and set left to None
                current.right = current.left
                current.left = None
            
            # Move to the next node in the "linked list"
            current = current.right

# Example Test Cases
def build_tree(values):
    """
    Helper function to build a binary tree from a list of values.
    """
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    for i in range(len(values)):
        if nodes[i]:
            if 2 * i + 1 < len(values):
                nodes[i].left = nodes[2 * i + 1]
            if 2 * i + 2 < len(values):
                nodes[i].right = nodes[2 * i + 2]
    return nodes[0]

def tree_to_list(root):
    """
    Helper function to convert a flattened binary tree to a list.
    """
    result = []
    while root:
        result.append(root.val)
        root = root.right
    return result

if __name__ == "__main__":
    # Test Case 1
    root1 = build_tree([1, 2, 5, 3, 4, None, 6])
    Solution().flatten(root1)
    print(tree_to_list(root1))  # Output: [1, 2, 3, 4, 5, 6]

    # Test Case 2
    root2 = build_tree([])
    Solution().flatten(root2)
    print(tree_to_list(root2))  # Output: []

    # Test Case 3
    root3 = build_tree([0])
    Solution().flatten(root3)
    print(tree_to_list(root3))  # Output: [0]

"""
Time Complexity:
- Each node is visited once, and for each node, we may traverse its left subtree to find the rightmost node.
- In the worst case, this results in O(n) work for each node, but since the rightmost traversal is limited to the total number of nodes, the overall complexity is O(n).

Space Complexity:
- The algorithm modifies the tree in-place, so it uses O(1) extra space.
- However, the recursion stack (if implemented recursively) would use O(h) space, where h is the height of the tree. In this iterative implementation, the space complexity is O(1).

Topic: Binary Tree
"""