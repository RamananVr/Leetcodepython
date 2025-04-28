"""
LeetCode Problem #2971: Serialize and Deserialize N-ary Tree

Problem Statement:
Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a tree in which each node has no more than N children. Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

You need to design a codec class with two methods:
1. `serialize(root)`: Encodes an N-ary tree to a single string.
2. `deserialize(data)`: Decodes the encoded string to reconstruct the N-ary tree.

The encoded string should be as compact as possible.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- 0 <= Node.val <= 10^4
- The height of the n-ary tree is less than or equal to 1000.
- Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.

Example:
Input: An N-ary tree with root node and its children.
Output: The serialized string and the reconstructed tree.

Topic: N-ary Tree
"""

from typing import List, Optional

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Codec:
    def serialize(self, root: Optional[Node]) -> str:
        """Encodes an N-ary tree to a single string."""
        if not root:
            return ""
        
        serialized = []
        
        def dfs(node):
            if not node:
                return
            # Add the current node's value
            serialized.append(str(node.val))
            # Add the number of children
            serialized.append(str(len(node.children)))
            # Recursively serialize each child
            for child in node.children:
                dfs(child)
        
        dfs(root)
        return " ".join(serialized)

    def deserialize(self, data: str) -> Optional[Node]:
        """Decodes your encoded data to tree."""
        if not data:
            return None
        
        tokens = iter(data.split())
        
        def dfs():
            # Read the current node's value
            val = int(next(tokens))
            # Read the number of children
            num_children = int(next(tokens))
            # Create the current node
            node = Node(val)
            # Recursively deserialize each child
            for _ in range(num_children):
                node.children.append(dfs())
            return node
        
        return dfs()

# Example Test Cases
def example_test_cases():
    codec = Codec()
    
    # Example 1: Serialize and Deserialize a simple N-ary tree
    root = Node(1, [
        Node(2),
        Node(3, [Node(6), Node(7)]),
        Node(4),
        Node(5)
    ])
    
    serialized = codec.serialize(root)
    print("Serialized:", serialized)
    
    deserialized = codec.deserialize(serialized)
    print("Deserialized Root Value:", deserialized.val)
    print("Deserialized Children Count:", len(deserialized.children))
    print("Deserialized First Child Value:", deserialized.children[0].val)

    # Example 2: Empty tree
    root = None
    serialized = codec.serialize(root)
    print("Serialized (Empty Tree):", serialized)
    
    deserialized = codec.deserialize(serialized)
    print("Deserialized (Empty Tree):", deserialized)

# Time and Space Complexity Analysis
"""
Time Complexity:
- Serialization: O(n), where n is the number of nodes in the tree. Each node is visited once during the DFS traversal.
- Deserialization: O(n), where n is the number of nodes in the tree. Each node is reconstructed once during the DFS traversal.

Space Complexity:
- Serialization: O(h), where h is the height of the tree. This is the space used by the recursion stack during DFS.
- Deserialization: O(h), where h is the height of the tree. This is the space used by the recursion stack during DFS.
"""

# Topic: N-ary Tree

if __name__ == "__main__":
    example_test_cases()