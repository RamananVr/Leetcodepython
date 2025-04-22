"""
LeetCode Problem #590: N-ary Tree Postorder Traversal

Problem Statement:
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- 0 <= Node.val <= 10^4
- The height of the n-ary tree is less than or equal to 1000.

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

# Solution
def postorder(root: 'Node') -> list[int]:
    """
    Perform postorder traversal on an n-ary tree.

    :param root: Root node of the n-ary tree.
    :return: List of node values in postorder traversal.
    """
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)
        stack.extend(node.children)  # Add children to the stack

    return result[::-1]  # Reverse the result to get postorder

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = Node(1, [
        Node(3, [Node(5), Node(6)]),
        Node(2),
        Node(4)
    ])
    print(postorder(root1))  # Output: [5, 6, 3, 2, 4, 1]

    # Example 2
    root2 = Node(1, [
        Node(2),
        Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]),
        Node(4, [Node(8, [Node(12)])]),
        Node(5, [Node(9, [Node(13)]), Node(10)])
    ])
    print(postorder(root2))  # Output: [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Each node is visited exactly once, and for each node, we process its children.
- Therefore, the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The space complexity is determined by the stack used for traversal.
- In the worst case, the stack can hold all the nodes in the tree (e.g., when the tree is a single chain of nodes).
- Therefore, the space complexity is O(n).
"""

# Topic: Tree Traversal