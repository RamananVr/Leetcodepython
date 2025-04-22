"""
LeetCode Question #431: Encode N-ary Tree to Binary Tree

Problem Statement:
Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree back to the N-ary tree. 
An N-ary tree is a tree in which each node has no more than N children. A binary tree is a tree in which each node 
has at most two children.

Your task is to write two functions:
1. `encode(root: Node) -> TreeNode`: Encodes an N-ary tree to a binary tree.
2. `decode(root: TreeNode) -> Node`: Decodes the binary tree back to the N-ary tree.

Constraints:
- The N-ary tree node is defined as:
    class Node:
        def __init__(self, val=None, children=None):
            self.val = val
            self.children = children if children is not None else []
- The binary tree node is defined as:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
- You may assume that the input N-ary tree is well-formed and does not contain cycles.
"""

# Definition for an N-ary tree node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def encode(self, root: Node) -> TreeNode:
        """
        Encodes an N-ary tree to a binary tree.
        """
        if not root:
            return None
        
        binary_root = TreeNode(root.val)
        if root.children:
            binary_root.left = self.encode(root.children[0])
        
        current = binary_root.left
        for child in root.children[1:]:
            current.right = self.encode(child)
            current = current.right
        
        return binary_root

    def decode(self, root: TreeNode) -> Node:
        """
        Decodes a binary tree to an N-ary tree.
        """
        if not root:
            return None
        
        nary_root = Node(root.val)
        current = root.left
        while current:
            nary_root.children.append(self.decode(current))
            current = current.right
        
        return nary_root

# Example Test Cases
def example_test_cases():
    codec = Codec()

    # Example N-ary tree:
    #         1
    #       / | \
    #      2  3  4
    #         |
    #         5
    nary_root = Node(1, [
        Node(2),
        Node(3, [Node(5)]),
        Node(4)
    ])

    # Encode N-ary tree to binary tree
    binary_root = codec.encode(nary_root)
    print("Encoded Binary Tree Root:", binary_root.val)

    # Decode binary tree back to N-ary tree
    decoded_nary_root = codec.decode(binary_root)
    print("Decoded N-ary Tree Root:", decoded_nary_root.val)
    print("Decoded N-ary Tree Children:", [child.val for child in decoded_nary_root.children])

example_test_cases()

"""
Time and Space Complexity Analysis:

1. Encoding:
   - Time Complexity: O(N), where N is the total number of nodes in the N-ary tree. We traverse each node once.
   - Space Complexity: O(H), where H is the height of the N-ary tree. This is the space used by the recursion stack.

2. Decoding:
   - Time Complexity: O(N), where N is the total number of nodes in the binary tree. We traverse each node once.
   - Space Complexity: O(H), where H is the height of the binary tree. This is the space used by the recursion stack.

Topic: Tree Transformation (N-ary Tree, Binary Tree)
"""