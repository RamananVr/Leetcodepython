"""
LeetCode Problem #117: Populating Next Right Pointers in Each Node II

Problem Statement:
Given a binary tree:

    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A),
    1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \     \
4-> 5 -> 7 -> NULL

Example 2:
Input: root = []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 6000].
- -100 <= Node.val <= 100

Follow-up:
- You may only use constant extra space.
- The recursive approach is fine, but you should attempt to solve it iteratively.

"""

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        # Start with the root node
        current = root
        # Dummy node to track the start of the next level
        dummy = Node(0)
        while current:
            # Use a pointer to build the next level
            tail = dummy
            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                if current.right:
                    tail.next = current.right
                    tail = tail.next
                # Move to the next node in the current level
                current = current.next
            # Move to the next level
            current = dummy.next
            dummy.next = None  # Reset the dummy node for the next level
        
        return root

# Example Test Cases
def print_tree_with_next_pointers(root):
    """Helper function to print the tree level by level with next pointers."""
    levels = []
    while root:
        level = []
        current = root
        while current:
            level.append(current.val)
            current = current.next
        levels.append(level)
        # Move to the next level
        root = root.left if root.left else root.right
    return levels

# Test Case 1
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)

solution = Solution()
solution.connect(root)
print(print_tree_with_next_pointers(root))  # Expected Output: [[1], [2, 3], [4, 5, 7]]

# Test Case 2
root = None
solution = Solution()
print(solution.connect(root))  # Expected Output: None

# Test Case 3
root = Node(1)
solution = Solution()
solution.connect(root)
print(print_tree_with_next_pointers(root))  # Expected Output: [[1]]

"""
Time Complexity:
- O(n): Each node is visited exactly once to establish the next pointers.

Space Complexity:
- O(1): The solution uses constant extra space (excluding the recursion stack or input tree).

Topic: Binary Tree, Level Order Traversal
"""