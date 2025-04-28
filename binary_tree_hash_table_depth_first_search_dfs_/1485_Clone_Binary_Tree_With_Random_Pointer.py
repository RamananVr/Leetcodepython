"""
LeetCode Problem #1485: Clone Binary Tree With Random Pointer

Problem Statement:
A binary tree is given such that each node contains an additional random pointer which could point to any node in the tree or null.

You need to return a deep copy of the tree.

The tree is represented in the same input/output way as normal binary trees where each node is represented as a tuple of (val, left, right, random). 
The random pointer is described by the index of the node (in level order traversal) the random pointer is pointing to, or null if it is not pointing to any node.

Constraints:
- The number of nodes in the tree is in the range [0, 1000].
- -10^6 <= Node.val <= 10^6
"""

# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'Node':
        """
        Creates a deep copy of a binary tree with random pointers.
        """
        if not root:
            return None

        # A dictionary to map original nodes to their clones
        node_map = {}

        # Step 1: Clone all nodes (without setting left, right, or random pointers yet)
        def clone_nodes(node):
            if not node:
                return None
            if node in node_map:
                return node_map[node]
            clone = Node(node.val)
            node_map[node] = clone
            return clone

        # Step 2: Set up left, right, and random pointers for the cloned nodes
        def clone_tree(node):
            if not node:
                return None
            clone = clone_nodes(node)
            clone.left = clone_tree(node.left)
            clone.right = clone_tree(node.right)
            clone.random = clone_nodes(node.random)
            return clone

        return clone_tree(root)

# Example Test Cases
def test():
    # Helper function to build a tree from a list of tuples
    def build_tree(nodes):
        if not nodes:
            return None
        node_list = [Node(val) if val is not None else None for val, _, _, _ in nodes]
        for i, (val, left, right, random) in enumerate(nodes):
            if node_list[i]:
                node_list[i].left = node_list[left] if left is not None else None
                node_list[i].right = node_list[right] if right is not None else None
                node_list[i].random = node_list[random] if random is not None else None
        return node_list[0]

    # Helper function to serialize a tree for comparison
    def serialize_tree(node):
        if not node:
            return None
        node_map = {}
        result = []

        def serialize(node):
            if not node:
                return None
            if node in node_map:
                return node_map[node]
            idx = len(result)
            node_map[node] = idx
            result.append((node.val, serialize(node.left), serialize(node.right), serialize(node.random)))
            return idx

        serialize(node)
        return result

    # Test Case 1
    nodes = [
        (1, 1, 2, None),  # Node 0: val=1, left=1, right=2, random=None
        (2, None, None, 0),  # Node 1: val=2, left=None, right=None, random=0
        (3, None, None, 1)   # Node 2: val=3, left=None, right=None, random=1
    ]
    root = build_tree(nodes)
    solution = Solution()
    cloned_root = solution.copyRandomBinaryTree(root)
    assert serialize_tree(cloned_root) == serialize_tree(root)

    # Test Case 2: Empty tree
    root = None
    cloned_root = solution.copyRandomBinaryTree(root)
    assert serialize_tree(cloned_root) == serialize_tree(root)

    # Test Case 3: Single node with no random pointer
    nodes = [
        (1, None, None, None)  # Node 0: val=1, left=None, right=None, random=None
    ]
    root = build_tree(nodes)
    cloned_root = solution.copyRandomBinaryTree(root)
    assert serialize_tree(cloned_root) == serialize_tree(root)

    print("All test cases passed!")

# Time and Space Complexity Analysis
"""
Time Complexity:
- O(n): We traverse each node of the tree once to clone it and set up its pointers.

Space Complexity:
- O(n): We use a dictionary to store the mapping of original nodes to their clones, which requires O(n) space.

Where n is the number of nodes in the tree.
"""

# Topic: Binary Tree, Hash Table, Depth-First Search (DFS)

if __name__ == "__main__":
    test()