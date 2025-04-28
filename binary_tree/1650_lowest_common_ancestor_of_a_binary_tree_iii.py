"""
LeetCode Question #1650: Lowest Common Ancestor of a Binary Tree III

Problem Statement:
Given two nodes of a binary tree `p` and `q`, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for a Node is as follows:
class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

The lowest common ancestor of two nodes `p` and `q` is defined as the lowest node in the tree that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).

Constraints:
- The number of nodes in the tree is in the range [2, 10^4].
- -10^5 <= Node.val <= 10^5
- All Node.val are unique.
- `p` and `q` exist in the tree.

"""

# Solution
class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def lowestCommonAncestor(p: Node, q: Node) -> Node:
    """
    Finds the lowest common ancestor of two nodes in a binary tree with parent pointers.

    Args:
    p (Node): First node.
    q (Node): Second node.

    Returns:
    Node: The lowest common ancestor of p and q.
    """
    # Use two pointers to traverse the tree
    a, b = p, q
    while a != b:
        # Move to the parent node, or switch to the other node if reaching None
        a = a.parent if a else q
        b = b.parent if b else p
    return a

# Example Test Cases
if __name__ == "__main__":
    # Create a sample binary tree with parent pointers
    root = Node(3)
    node5 = Node(5, parent=root)
    node1 = Node(1, parent=root)
    root.left = node5
    root.right = node1

    node6 = Node(6, parent=node5)
    node2 = Node(2, parent=node5)
    node5.left = node6
    node5.right = node2

    node0 = Node(0, parent=node1)
    node8 = Node(8, parent=node1)
    node1.left = node0
    node1.right = node8

    node7 = Node(7, parent=node2)
    node4 = Node(4, parent=node2)
    node2.left = node7
    node2.right = node4

    # Test Case 1
    p = node5
    q = node1
    print(lowestCommonAncestor(p, q).val)  # Output: 3

    # Test Case 2
    p = node6
    q = node4
    print(lowestCommonAncestor(p, q).val)  # Output: 5

    # Test Case 3
    p = node7
    q = node8
    print(lowestCommonAncestor(p, q).val)  # Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm traverses the tree using parent pointers. In the worst case, each pointer traverses the height of the tree.
- Since the height of the tree is O(h), where h is the height of the tree, the time complexity is O(h).
- In a balanced binary tree, h = O(log n), and in the worst case (skewed tree), h = O(n).

Space Complexity:
- The algorithm uses constant space, as it only uses two pointers (a and b).
- Space complexity is O(1).
"""

# Topic: Binary Tree