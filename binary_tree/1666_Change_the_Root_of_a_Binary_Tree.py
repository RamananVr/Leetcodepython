"""
LeetCode Problem #1666: Change the Root of a Binary Tree

Problem Statement:
You are given the root of a binary tree and a node `p` in the tree. You need to change the root of the tree to `p`. 
The result should still be a valid binary tree with the same nodes and edges, but the parent-child relationships 
of the nodes may need to be changed.

Specifically, the following changes are made:
1. The original parent of `p` becomes its child.
2. If `p` has a left child, it becomes the right child of its original parent.
3. The left child of `p` becomes `None`.

Return the new root of the tree.

Constraints:
- The number of nodes in the tree is in the range [2, 100].
- `-10^9 <= Node.val <= 10^9`
- All Node.val are unique.
- `p` is a node in the tree.

"""

# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def flipBinaryTree(self, root: Node, p: Node) -> Node:
        """
        Flips the binary tree so that the node `p` becomes the new root.

        Args:
        root (Node): The root of the binary tree.
        p (Node): The node to become the new root.

        Returns:
        Node: The new root of the binary tree.
        """
        current = p
        prev = None
        prev_right = None

        while current:
            parent = current.parent  # Save the parent node
            current.parent = prev  # Update the parent pointer to the previous node

            # Rearrange the left and right children
            current_right = current.right
            current.right = prev_right
            prev_right = current.left
            current.left = prev

            # Move to the next node in the path
            prev = current
            current = parent

        return prev

# Example Test Cases
def test_flipBinaryTree():
    # Create a sample binary tree
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    root.left = node2
    root.right = node3
    node2.parent = root
    node3.parent = root

    node2.left = node4
    node2.right = node5
    node4.parent = node2
    node5.parent = node2

    node3.right = node6
    node6.parent = node3

    # Test case 1: Change root to node 5
    solution = Solution()
    new_root = solution.flipBinaryTree(root, node5)
    assert new_root == node5
    assert new_root.left is None
    assert new_root.right == node2
    assert node2.left == root
    assert node2.right is None
    assert root.left is None
    assert root.right is None

    # Test case 2: Change root to node 4
    new_root = solution.flipBinaryTree(root, node4)
    assert new_root == node4
    assert new_root.left is None
    assert new_root.right == node2
    assert node2.left == root
    assert node2.right == node5
    assert root.left is None
    assert root.right is None

    print("All test cases passed!")

if __name__ == "__main__":
    test_flipBinaryTree()

"""
Time Complexity:
- The algorithm traverses the path from the node `p` to the root of the tree. In the worst case, this path has a length of O(h), 
  where h is the height of the tree. Therefore, the time complexity is O(h).

Space Complexity:
- The algorithm uses a constant amount of extra space for variables like `current`, `prev`, `prev_right`, and `parent`. 
  Thus, the space complexity is O(1).

Topic: Binary Tree
"""