"""
LeetCode Problem #510: Inorder Successor in BST II

Problem Statement:
Given a `Node` in a Binary Search Tree (BST), find the in-order successor of that node in the BST.

The successor of a node `p` is the node with the smallest key greater than `p.val`. You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node.

A node is defined as follows:
class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

Constraints:
1. The number of nodes in the tree is in the range [1, 10^4].
2. -10^5 <= Node.val <= 10^5
3. All Node.val are unique.
4. The tree is a BST.
5. You are given the node for which the successor is to be found.

Follow-up:
Could you solve it without using extra space?
"""

# Solution
class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def inorderSuccessor(node: Node) -> Node:
    """
    Finds the in-order successor of the given node in a BST.
    """
    # Case 1: If the node has a right child, the successor is the leftmost node in the right subtree.
    if node.right:
        successor = node.right
        while successor.left:
            successor = successor.left
        return successor

    # Case 2: If the node does not have a right child, traverse up using the parent pointer
    # until we find a node that is the left child of its parent.
    while node.parent and node == node.parent.right:
        node = node.parent

    return node.parent

# Example Test Cases
def test_inorder_successor():
    # Constructing the BST
    root = Node(5)
    node3 = Node(3, parent=root)
    node6 = Node(6, parent=root)
    root.left = node3
    root.right = node6

    node2 = Node(2, parent=node3)
    node4 = Node(4, parent=node3)
    node3.left = node2
    node3.right = node4

    node1 = Node(1, parent=node2)
    node2.left = node1

    # Test Case 1: Successor of node 1 is node 2
    assert inorderSuccessor(node1) == node2

    # Test Case 2: Successor of node 2 is node 3
    assert inorderSuccessor(node2) == node3

    # Test Case 3: Successor of node 3 is node 4
    assert inorderSuccessor(node3) == node4

    # Test Case 4: Successor of node 4 is node 5
    assert inorderSuccessor(node4) == root

    # Test Case 5: Successor of node 5 is node 6
    assert inorderSuccessor(root) == node6

    # Test Case 6: Node 6 has no successor
    assert inorderSuccessor(node6) == None

    print("All test cases passed!")

# Run the test cases
if __name__ == "__main__":
    test_inorder_successor()

"""
Time Complexity:
- Case 1 (node has a right child): O(h), where h is the height of the tree, as we traverse down the right subtree to find the leftmost node.
- Case 2 (node does not have a right child): O(h), as we traverse up the tree using the parent pointer.
- Overall: O(h), where h is the height of the tree. In the worst case, h = O(log n) for a balanced BST and h = O(n) for a skewed BST.

Space Complexity:
- O(1), as we do not use any additional data structures and only use a constant amount of extra space.

Topic: Binary Search Tree (BST), Tree Traversal
"""