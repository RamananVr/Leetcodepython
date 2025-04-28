"""
LeetCode Problem #2331: Evaluate Boolean Binary Tree

Problem Statement:
You are given the root of a binary tree where each node has the following properties:
- `val`: 0 if the node represents `False`, 1 if the node represents `True`, 2 if the node represents a logical OR, and 3 if the node represents a logical AND.
- `left` and `right`: Children of the node.

Return the boolean result of evaluating the binary tree. A null node evaluates to `False`.

The evaluation of a node is as follows:
- If the node is a leaf node, the evaluation is the value of the node (`True` for 1, `False` for 0).
- If the node is an internal node with value 2 (`OR`), the evaluation is the logical OR of its children.
- If the node is an internal node with value 3 (`AND`), the evaluation is the logical AND of its children.

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- 0 <= Node.val <= 3
- Each node has either 0 or 2 children.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def evaluateTree(root: TreeNode) -> bool:
    """
    Evaluates the boolean binary tree based on the given rules.
    """
    # Base case: If the node is a leaf, return its boolean value
    if not root.left and not root.right:
        return root.val == 1
    
    # Recursive case: Evaluate based on the node's value
    left_eval = evaluateTree(root.left)
    right_eval = evaluateTree(root.right)
    
    if root.val == 2:  # Logical OR
        return left_eval or right_eval
    elif root.val == 3:  # Logical AND
        return left_eval and right_eval
    
    # Should not reach here for valid inputs
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Simple OR operation
    root1 = TreeNode(2, TreeNode(1), TreeNode(0))  # OR(True, False)
    print(evaluateTree(root1))  # Expected: True

    # Test Case 2: Simple AND operation
    root2 = TreeNode(3, TreeNode(1), TreeNode(0))  # AND(True, False)
    print(evaluateTree(root2))  # Expected: False

    # Test Case 3: Nested operations
    root3 = TreeNode(3, TreeNode(2, TreeNode(1), TreeNode(0)), TreeNode(1))  # AND(OR(True, False), True)
    print(evaluateTree(root3))  # Expected: True

    # Test Case 4: Single leaf node (True)
    root4 = TreeNode(1)  # True
    print(evaluateTree(root4))  # Expected: True

    # Test Case 5: Single leaf node (False)
    root5 = TreeNode(0)  # False
    print(evaluateTree(root5))  # Expected: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each node in the binary tree is visited exactly once during the recursive traversal.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the recursion stack. In the worst case, the tree is completely unbalanced (e.g., a chain), and the recursion stack will have a depth of n.
- In the best case, the tree is balanced, and the recursion stack will have a depth of log(n).
- Therefore, the space complexity is O(h), where h is the height of the tree. In the worst case, h = n.

Topic: Binary Tree
"""