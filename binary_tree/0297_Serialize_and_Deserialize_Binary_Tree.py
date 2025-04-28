"""
LeetCode Problem #297: Serialize and Deserialize Binary Tree

Problem Statement:
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification:
The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:
    Input: root = [1,2,3,null,null,4,5]
    Output: [1,2,3,null,null,4,5]

Example 2:
    Input: root = []
    Output: []

Constraints:
    - The number of nodes in the tree is in the range [0, 10^4].
    - -1000 <= Node.val <= 1000
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return "null"
        
        result = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        
        # Remove trailing "null" values for a cleaner output
        while result and result[-1] == "null":
            result.pop()
        
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if data == "null":
            return None
        
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        i = 1
        
        while queue:
            node = queue.popleft()
            if i < len(nodes) and nodes[i] != "null":
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i += 1
            if i < len(nodes) and nodes[i] != "null":
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1
        
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Example Test Cases
def test():
    codec = Codec()
    
    # Test Case 1: Example tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert codec.serialize(deserialized) == "1,2,3,null,null,4,5"
    
    # Test Case 2: Empty tree
    root = None
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert codec.serialize(deserialized) == "null"
    
    # Test Case 3: Single node tree
    root = TreeNode(42)
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert codec.serialize(deserialized) == "42"
    
    # Test Case 4: Tree with only left children
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert codec.serialize(deserialized) == "1,2,null,3"
    
    # Test Case 5: Tree with only right children
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert codec.serialize(deserialized) == "1,null,2,null,3"
    
    print("All test cases passed!")

# Run the test cases
if __name__ == "__main__":
    test()

"""
Time Complexity:
- Serialization: O(n), where n is the number of nodes in the tree. Each node is visited once.
- Deserialization: O(n), where n is the number of nodes in the tree. Each node is processed once.

Space Complexity:
- Serialization: O(n), for the result list and the queue used for level-order traversal.
- Deserialization: O(n), for the queue used to reconstruct the tree.

Topic: Binary Tree
"""