"""
LeetCode Problem #1028: Recover a Tree From Preorder Traversal

Problem Statement:
We run a preorder depth-first search (DFS) on the root of a binary tree. At each node, we record the node's value, 
and if it has children, we record the depth of the children with dashes ('-').

For example, if the input is "1-2--3--4-5--6--7", the preorder traversal of the tree is as follows:
    - The root node is 1.
    - The depth of 2 is 1 (one dash before 2).
    - The depth of 3 is 2 (two dashes before 3).
    - The depth of 4 is 2 (two dashes before 4).
    - The depth of 5 is 1 (one dash before 5).
    - The depth of 6 is 2 (two dashes before 6).
    - The depth of 7 is 2 (two dashes before 7).

Given the string `traversal`, recover the tree and return its root.

Constraints:
- The number of nodes in the original tree is in the range [1, 1000].
- 1 <= Node.val <= 10^9.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recoverFromPreorder(traversal: str) -> TreeNode:
    """
    Recovers a binary tree from its preorder traversal string representation.
    """
    stack = []
    i = 0
    n = len(traversal)

    while i < n:
        level = 0
        # Count the number of dashes to determine the depth
        while i < n and traversal[i] == '-':
            level += 1
            i += 1

        # Read the node value
        value = 0
        while i < n and traversal[i].isdigit():
            value = value * 10 + int(traversal[i])
            i += 1

        # Create the new node
        node = TreeNode(value)

        # Adjust the stack to match the current depth
        while len(stack) > level:
            stack.pop()

        # Attach the new node to its parent
        if stack:
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node

        # Push the current node onto the stack
        stack.append(node)

    return stack[0]

# Example Test Cases
def print_tree_preorder(node):
    """Helper function to print the tree in preorder for verification."""
    if not node:
        return
    print(node.val, end=" ")
    print_tree_preorder(node.left)
    print_tree_preorder(node.right)

if __name__ == "__main__":
    # Test Case 1
    traversal1 = "1-2--3--4-5--6--7"
    root1 = recoverFromPreorder(traversal1)
    print("Preorder of recovered tree (Test Case 1):")
    print_tree_preorder(root1)  # Expected Output: 1 2 3 4 5 6 7

    # Test Case 2
    traversal2 = "1-2--3---4-5--6---7"
    root2 = recoverFromPreorder(traversal2)
    print("\nPreorder of recovered tree (Test Case 2):")
    print_tree_preorder(root2)  # Expected Output: 1 2 3 4 5 6 7

    # Test Case 3
    traversal3 = "1-401--349---90--88"
    root3 = recoverFromPreorder(traversal3)
    print("\nPreorder of recovered tree (Test Case 3):")
    print_tree_preorder(root3)  # Expected Output: 1 401 349 90 88

"""
Time Complexity:
- Parsing the input string takes O(n), where n is the length of the string.
- Each node is processed once, and stack operations (push/pop) are O(1).
- Overall time complexity: O(n).

Space Complexity:
- The stack stores at most O(h) nodes, where h is the height of the tree.
- In the worst case (skewed tree), h = O(n).
- Overall space complexity: O(n).

Topic: Binary Tree, String Parsing
"""