"""
LeetCode Question #156: Binary Tree Upside Down

Problem Statement:
Given the root of a binary tree, turn the tree upside down and return the new root. 
You can turn a binary tree upside down with the following rules:
1. The original left child becomes the new root.
2. The original root becomes the right child.
3. The original right child becomes the left child.

The transformation should be done in-place, meaning no new nodes should be created.

Example:
Input: root = [1, 2, 3, 4, 5]
Output: [4, 5, 2, null, null, 3, 1]

Constraints:
- The number of nodes in the tree will be in the range [0, 10^4].
- The tree is a binary tree with unique values.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def upsideDownBinaryTree(root: TreeNode) -> TreeNode:
    """
    Function to turn a binary tree upside down.
    """
    if not root or not root.left:
        return root
    
    # Recursively process the left subtree
    new_root = upsideDownBinaryTree(root.left)
    
    # Transform the current node
    root.left.left = root.right  # Original right child becomes new left child
    root.left.right = root       # Original root becomes new right child
    
    # Disconnect the current node from its children
    root.left = None
    root.right = None
    
    return new_root

# Example Test Cases
def test_upsideDownBinaryTree():
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

    # Helper function to serialize a binary tree to a list
    def serialize_tree(root):
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()
        return result

    # Test Case 1
    root = build_tree([1, 2, 3, 4, 5])
    new_root = upsideDownBinaryTree(root)
    assert serialize_tree(new_root) == [4, 5, 2, None, None, 3, 1], "Test Case 1 Failed"

    # Test Case 2
    root = build_tree([1, 2, 3])
    new_root = upsideDownBinaryTree(root)
    assert serialize_tree(new_root) == [2, 3, 1], "Test Case 2 Failed"

    # Test Case 3
    root = build_tree([])
    new_root = upsideDownBinaryTree(root)
    assert serialize_tree(new_root) == [], "Test Case 3 Failed"

    # Test Case 4
    root = build_tree([1])
    new_root = upsideDownBinaryTree(root)
    assert serialize_tree(new_root) == [1], "Test Case 4 Failed"

    print("All test cases passed!")

# Run the test cases
test_upsideDownBinaryTree()

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function processes each node exactly once, so the time complexity is O(n), 
  where n is the number of nodes in the binary tree.

Space Complexity:
- The space complexity is O(h), where h is the height of the tree, due to the 
  recursive call stack. In the worst case (skewed tree), h = n, so the space 
  complexity is O(n). In the best case (balanced tree), h = log(n), so the space 
  complexity is O(log(n)).

Topic: Binary Tree
"""