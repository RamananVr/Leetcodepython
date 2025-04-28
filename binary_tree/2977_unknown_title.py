"""
LeetCode Problem #2977: Full Problem Statement

Problem:
You are given a binary tree where each node contains an integer value. Your task is to serialize and deserialize the binary tree. Serialization is the process of converting a binary tree into a string representation, and deserialization is the process of converting the string representation back into the original binary tree.

Implement the following methods:
1. `serialize(root: TreeNode) -> str`: Converts the binary tree rooted at `root` into a string representation.
2. `deserialize(data: str) -> TreeNode`: Converts the string representation `data` back into the original binary tree.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000
- The input tree is guaranteed to be a binary tree.

You may assume that the input/output format is consistent across calls to `serialize` and `deserialize`.

Example:
Input:
    root = [1,2,3,null,null,4,5]

Output:
    serialize(root) -> "1,2,3,null,null,4,5"
    deserialize("1,2,3,null,null,4,5") -> [1,2,3,null,null,4,5]

Follow-up:
Could you design a solution that is both space and time efficient?
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ""
        
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
        
        # Remove trailing "null" values for a cleaner representation
        while result and result[-1] == "null":
            result.pop()
        
        return ",".join(result)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        if not data:
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

# Example Test Cases
def test():
    codec = Codec()
    
    # Test Case 1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    serialized = codec.serialize(root)
    print("Serialized:", serialized)  # Expected: "1,2,3,null,null,4,5"
    deserialized = codec.deserialize(serialized)
    print("Deserialized:", codec.serialize(deserialized))  # Expected: "1,2,3,null,null,4,5"
    
    # Test Case 2
    root = None
    serialized = codec.serialize(root)
    print("Serialized:", serialized)  # Expected: ""
    deserialized = codec.deserialize(serialized)
    print("Deserialized:", codec.serialize(deserialized))  # Expected: ""
    
    # Test Case 3
    root = TreeNode(1)
    serialized = codec.serialize(root)
    print("Serialized:", serialized)  # Expected: "1"
    deserialized = codec.deserialize(serialized)
    print("Deserialized:", codec.serialize(deserialized))  # Expected: "1"

test()

"""
Time and Space Complexity Analysis:

1. Serialization:
   - Time Complexity: O(n), where n is the number of nodes in the tree. Each node is visited once.
   - Space Complexity: O(n), for the result list and the queue used in the level-order traversal.

2. Deserialization:
   - Time Complexity: O(n), where n is the number of nodes in the tree. Each node is processed once.
   - Space Complexity: O(n), for the queue used to reconstruct the tree.

Overall:
- Time Complexity: O(n)
- Space Complexity: O(n)

Topic: Binary Tree
"""