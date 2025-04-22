"""
LeetCode Question #536: Construct Binary Tree from String

Problem Statement:
You need to construct a binary tree from a string consisting of parenthesis and integers. 
The whole input represents a binary tree. It contains an integer followed by zero, one, or two pairs of parenthesis. 
The integer represents the root's value, and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example 1:
Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]

Example 2:
Input: s = "4(2(3)(1))"
Output: [4,2,None,3,1]

Constraints:
- 0 <= Node.val <= 10^9
- The input string is guaranteed to be valid.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def str2tree(s: str) -> TreeNode:
    """
    Constructs a binary tree from a string representation.
    """
    if not s:
        return None

    def parse_subtree(index):
        # Parse the root value
        start = index
        while index < len(s) and (s[index].isdigit() or s[index] == '-'):
            index += 1
        root_val = int(s[start:index])
        root = TreeNode(root_val)

        # Parse left subtree if it exists
        if index < len(s) and s[index] == '(':
            index += 1  # Skip '('
            root.left, index = parse_subtree(index)
            index += 1  # Skip ')'

        # Parse right subtree if it exists
        if index < len(s) and s[index] == '(':
            index += 1  # Skip '('
            root.right, index = parse_subtree(index)
            index += 1  # Skip ')'

        return root, index

    tree, _ = parse_subtree(0)
    return tree

# Helper function to serialize the tree into a list for testing
def serialize_tree(root):
    """Converts a binary tree to a list representation (level-order traversal)."""
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

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "4(2(3)(1))(6(5))"
    root1 = str2tree(s1)
    print(serialize_tree(root1))  # Output: [4, 2, 6, 3, 1, 5]

    # Test Case 2
    s2 = "4(2(3)(1))"
    root2 = str2tree(s2)
    print(serialize_tree(root2))  # Output: [4, 2, None, 3, 1]

    # Test Case 3
    s3 = "1"
    root3 = str2tree(s3)
    print(serialize_tree(root3))  # Output: [1]

    # Test Case 4
    s4 = "1(2)"
    root4 = str2tree(s4)
    print(serialize_tree(root4))  # Output: [1, 2]

    # Test Case 5
    s5 = "1(2(3))"
    root5 = str2tree(s5)
    print(serialize_tree(root5))  # Output: [1, 2, None, 3]

"""
Time Complexity:
- Parsing the string involves traversing each character exactly once, so the time complexity is O(n), 
  where n is the length of the input string.

Space Complexity:
- The space complexity is O(h), where h is the height of the tree. This is due to the recursion stack 
  used during the tree construction. In the worst case (skewed tree), h can be O(n).

Topic: Binary Tree
"""