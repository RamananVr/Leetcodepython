"""
LeetCode Problem #589: N-ary Tree Preorder Traversal

Problem Statement:
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

N-ary Tree Input Format:
- Each node in the n-ary tree contains a value (`val`) and a list of its children (`children`).
- You are given the root of the tree.

Preorder Traversal:
- In a preorder traversal, you visit the root node first, then recursively do a preorder traversal of each child in order.

Constraints:
1. The number of nodes in the tree is in the range [0, 10^4].
2. 0 <= Node.val <= 10^4
3. The height of the n-ary tree is less than or equal to 1000.

Follow-up:
Recursive solutions are straightforward. Could you do it iteratively?
"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

# Solution: Recursive Approach
def preorder(root: 'Node') -> list[int]:
    """
    Perform a preorder traversal of an n-ary tree.

    :param root: Root node of the n-ary tree.
    :return: List of node values in preorder traversal order.
    """
    result = []

    def dfs(node):
        if not node:
            return
        result.append(node.val)  # Visit the root node
        for child in node.children:  # Visit all children
            dfs(child)

    dfs(root)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Example 1:
    # Input: root = [1,null,3,2,4,null,5,6]
    # Tree structure:
    #        1
    #      / | \
    #     3  2  4
    #    / \
    #   5   6
    root1 = Node(1, [
        Node(3, [Node(5), Node(6)]),
        Node(2),
        Node(4)
    ])
    print(preorder(root1))  # Output: [1, 3, 5, 6, 2, 4]

    # Example 2:
    # Input: root = []
    # Tree structure: Empty tree
    root2 = None
    print(preorder(root2))  # Output: []

    # Example 3:
    # Input: root = [1]
    # Tree structure:
    #        1
    root3 = Node(1)
    print(preorder(root3))  # Output: [1]

"""
Time Complexity:
- Let `n` be the number of nodes in the tree.
- In the recursive approach, we visit each node exactly once, performing O(1) work per node.
- Therefore, the time complexity is O(n).

Space Complexity:
- The space complexity is determined by the recursion stack.
- In the worst case (a skewed tree), the recursion stack can go as deep as the height of the tree, which is O(h), where `h` is the height of the tree.
- In the best case (a balanced tree), the height of the tree is O(log n).
- Therefore, the space complexity is O(h), where `h` is the height of the tree.

Topic: Tree Traversal
"""