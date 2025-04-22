"""
LeetCode Question #428: Serialize and Deserialize N-ary Tree

Problem Statement:
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following N-ary tree:

            1
          / | \
         3  2  4
        / \
       5   6

as [1 [3 [5 6] 2 4]].

Note that this is just an example; you do not necessarily need to follow this format.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- 0 <= Node.val <= 10^4
- The height of the n-ary tree is less than or equal to 1000.
- Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Codec:
    def serialize(self, root: 'Node') -> str:
        """
        Encodes an N-ary tree to a single string.
        """
        if not root:
            return ""
        
        def dfs(node):
            if not node:
                return ""
            serialized = str(node.val)
            if node.children:
                serialized += " [" + " ".join(dfs(child) for child in node.children) + "]"
            return serialized
        
        return dfs(root)

    def deserialize(self, data: str) -> 'Node':
        """
        Decodes your encoded data to tree.
        """
        if not data:
            return None
        
        tokens = iter(data.split())
        
        def parse():
            val = int(next(tokens))
            node = Node(val)
            if next(tokens, None) == "[":
                while True:
                    child = parse()
                    if child:
                        node.children.append(child)
                    if next(tokens, None) == "]":
                        break
            return node
        
        return parse()

# Example Test Cases
if __name__ == "__main__":
    codec = Codec()
    
    # Example 1
    root = Node(1, [
        Node(3, [Node(5), Node(6)]),
        Node(2),
        Node(4)
    ])
    serialized = codec.serialize(root)
    print("Serialized:", serialized)  # Output: "1 [3 [5 6] 2 4]"
    deserialized = codec.deserialize(serialized)
    print("Deserialized:", codec.serialize(deserialized))  # Output: "1 [3 [5 6] 2 4]"
    
    # Example 2: Empty tree
    root = None
    serialized = codec.serialize(root)
    print("Serialized:", serialized)  # Output: ""
    deserialized = codec.deserialize(serialized)
    print("Deserialized:", deserialized)  # Output: None

"""
Time Complexity:
- Serialization: O(n), where n is the number of nodes in the tree. Each node is visited once during the DFS traversal.
- Deserialization: O(n), where n is the number of nodes in the tree. Each node is reconstructed once during the parsing process.

Space Complexity:
- Serialization: O(h), where h is the height of the tree. This is the space used by the recursion stack during DFS.
- Deserialization: O(h), where h is the height of the tree. This is the space used by the recursion stack during parsing.

Topic: Tree, DFS
"""