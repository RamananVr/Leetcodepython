"""
LeetCode Question #449: Serialize and Deserialize BST

Problem Statement:
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree (BST). There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a BST can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification:
The encoded string should be as compact as possible.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- The value of each node is unique.
- `-10^4 <= Node.val <= 10^4`
- The input tree is guaranteed to be a binary search tree.

"""

# Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if not node:
                return []
            return [str(node.val)] + preorder(node.left) + preorder(node.right)
        
        return ','.join(preorder(root))

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        values = list(map(int, data.split(',')))
        
        def build_bst(low, high):
            if not values or values[0] < low or values[0] > high:
                return None
            
            val = values.pop(0)
            node = TreeNode(val)
            node.left = build_bst(low, val)
            node.right = build_bst(val, high)
            return node
        
        return build_bst(float('-inf'), float('inf'))

# Example Test Cases

def test_codec():
    codec = Codec()
    
    # Test Case 1: Empty Tree
    root = None
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert serialized == ""
    assert deserialized == None
    
    # Test Case 2: Single Node Tree
    root = TreeNode(1)
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert serialized == "1"
    assert deserialized.val == 1
    assert deserialized.left == None
    assert deserialized.right == None
    
    # Test Case 3: Larger Tree
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert serialized == "2,1,3"
    assert deserialized.val == 2
    assert deserialized.left.val == 1
    assert deserialized.right.val == 3

    print("All test cases passed!")

test_codec()

# Time and Space Complexity Analysis

"""
Time Complexity:
- Serialization: O(n), where n is the number of nodes in the BST. We perform a preorder traversal of the tree.
- Deserialization: O(n), where n is the number of nodes in the BST. We construct the tree using the preorder traversal list.

Space Complexity:
- Serialization: O(n), for storing the preorder traversal list.
- Deserialization: O(n), for storing the preorder traversal list and the recursive stack during tree construction.

Overall, both serialization and deserialization have a time and space complexity of O(n).

"""

# Topic: Binary Tree