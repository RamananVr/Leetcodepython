"""
LeetCode Problem #116: Populating Next Right Pointers in Each Node

Problem Statement:
You are given a perfect binary tree where all leaves are at the same level, and every parent has two children. The binary tree is defined as follows:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, where '#' signifies the end of each level.

Constraints:
- The number of nodes in the tree is in the range [0, 2^12 - 1].
- -1000 <= Node.val <= 1000

Follow-up:
- You may only use constant extra space.
- The recursive approach is fine, but can you solve it iteratively?
"""

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root: 'Node') -> 'Node':
    """
    Connects the next pointers of all nodes in a perfect binary tree.
    """
    if not root:
        return None

    # Start with the root node
    leftmost = root

    # Traverse level by level
    while leftmost.left:
        # Iterate through the current level
        head = leftmost
        while head:
            # Connect left child to right child
            head.left.next = head.right

            # Connect right child to the next node's left child (if exists)
            if head.next:
                head.right.next = head.next.left

            # Move to the next node in the current level
            head = head.next

        # Move to the next level
        leftmost = leftmost.left

    return root

# Example Test Cases
def print_tree_by_levels(root: 'Node'):
    """
    Helper function to print the tree level by level using the next pointers.
    """
    levels = []
    while root:
        level = []
        current = root
        while current:
            level.append(current.val)
            current = current.next
        levels.append(level)
        root = root.left
    return levels

if __name__ == "__main__":
    # Example 1
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    connected_root = connect(root)
    print(print_tree_by_levels(connected_root))  # Output: [[1], [2, 3], [4, 5, 6, 7]]

# Time and Space Complexity Analysis
# Time Complexity: O(N)
# - Each node is visited once, and the connections are made in constant time per node.
# - Therefore, the time complexity is linear in terms of the number of nodes, O(N).

# Space Complexity: O(1)
# - The solution uses constant extra space since no additional data structures are used.
# - The traversal is done in-place using the `next` pointers.

# Topic: Binary Tree