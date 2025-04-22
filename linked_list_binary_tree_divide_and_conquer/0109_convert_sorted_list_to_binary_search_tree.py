"""
LeetCode Question #109: Convert Sorted List to Binary Search Tree

Problem Statement:
Given the head of a singly linked list where elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees 
of every node never differs by more than one.

Example 1:
Input: head = [-10, -3, 0, 5, 9]
Output: [0, -3, 9, -10, null, 5]
Explanation: One possible answer is [0, -3, 9, -10, null, 5], which represents the 
following height-balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5

Example 2:
Input: head = []
Output: []

Constraints:
- The number of nodes in head is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedListToBST(head: ListNode) -> TreeNode:
    """
    Converts a sorted singly linked list to a height-balanced binary search tree.
    """
    # Helper function to find the middle element of the linked list
    def find_middle(left, right):
        slow = left
        fast = left
        while fast != right and fast.next != right:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Recursive function to build the BST
    def build_tree(left, right):
        if left == right:
            return None

        mid = find_middle(left, right)
        root = TreeNode(mid.val)
        root.left = build_tree(left, mid)
        root.right = build_tree(mid.next, right)
        return root

    return build_tree(head, None)

# Example Test Cases
def print_tree_inorder(root):
    """Helper function to print the tree in-order for testing."""
    if not root:
        return []
    return print_tree_inorder(root.left) + [root.val] + print_tree_inorder(root.right)

# Test Case 1
head1 = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
tree1 = sortedListToBST(head1)
print("In-order traversal of Test Case 1:", print_tree_inorder(tree1))  # Expected: [-10, -3, 0, 5, 9]

# Test Case 2
head2 = None
tree2 = sortedListToBST(head2)
print("In-order traversal of Test Case 2:", print_tree_inorder(tree2))  # Expected: []

# Test Case 3
head3 = ListNode(1)
tree3 = sortedListToBST(head3)
print("In-order traversal of Test Case 3:", print_tree_inorder(tree3))  # Expected: [1]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Finding the middle element takes O(n) for each recursive call.
- Since the list is divided into two halves at each step, the total time complexity is O(n log n).

Space Complexity:
- The recursion stack depth is O(log n) due to the balanced nature of the tree.
- No additional space is used apart from the recursion stack, so the overall space complexity is O(log n).
"""

# Topic: Linked List, Binary Tree, Divide and Conquer