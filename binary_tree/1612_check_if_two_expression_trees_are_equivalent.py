"""
LeetCode Question #1612: Check If Two Expression Trees are Equivalent

Problem Statement:
A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (variables), and internal nodes (nodes with two children) correspond to the operators '+' and '*'.

Two binary expression trees are considered equivalent if they evaluate to the same value for any given set of variable values.

Given the roots of two binary expression trees, return true if the two trees are equivalent, otherwise return false.

Constraints:
- The number of nodes in both trees is in the range [1, 1000].
- Each node has either 0 or 2 children.
- Leaf nodes are represented by lowercase English letters.
- Non-leaf nodes are represented by the characters '+' or '*'.
- It is guaranteed that no two leaf nodes have the same variable name.

Example:
Input: root1 = [+, a, b], root2 = [+, b, a]
Output: true
Explanation: Both trees evaluate to "a + b".

Input: root1 = [+, *, a, b, c], root2 = [+, *, b, a, c]
Output: true
Explanation: Both trees evaluate to "a * b + c".
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkEquivalence(root1: TreeNode, root2: TreeNode) -> bool:
    """
    This function checks if two binary expression trees are equivalent.
    """
    from collections import Counter

    def collect_terms(node):
        """
        Collects terms from the tree into a Counter object.
        Leaf nodes are added as variables, and '+' nodes combine terms.
        """
        if not node:
            return Counter()
        if not node.left and not node.right:  # Leaf node
            return Counter({node.val: 1})
        if node.val == '+':  # Addition
            return collect_terms(node.left) + collect_terms(node.right)
        if node.val == '*':  # Multiplication
            # For multiplication, we use a tuple to represent the product of terms
            left_terms = collect_terms(node.left)
            right_terms = collect_terms(node.right)
            return Counter({tuple(sorted(left_terms.elements() + right_terms.elements())): 1})
        return Counter()

    # Collect terms from both trees and compare
    return collect_terms(root1) == collect_terms(root2)

# Example Test Cases
if __name__ == "__main__":
    # Helper function to build a tree from a list
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
    root1 = build_tree(['+', 'a', 'b'])
    root2 = build_tree(['+', 'b', 'a'])
    print(checkEquivalence(root1, root2))  # Output: True

    # Test Case 2
    root1 = build_tree(['+', '*', 'a', 'b', 'c'])
    root2 = build_tree(['+', '*', 'b', 'a', 'c'])
    print(checkEquivalence(root1, root2))  # Output: True

    # Test Case 3
    root1 = build_tree(['+', 'a', 'b'])
    root2 = build_tree(['+', 'a', 'c'])
    print(checkEquivalence(root1, root2))  # Output: False

"""
Time Complexity:
- Collecting terms from a tree takes O(n) time, where n is the number of nodes in the tree.
- Comparing two Counter objects also takes O(n) in the worst case.
- Thus, the overall time complexity is O(n), where n is the total number of nodes in both trees.

Space Complexity:
- The space complexity is O(n) due to the storage of terms in the Counter object.

Topic: Binary Tree
"""