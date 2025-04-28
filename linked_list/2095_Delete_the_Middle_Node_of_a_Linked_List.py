"""
LeetCode Problem #2095: Delete the Middle Node of a Linked List

Problem Statement:
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

- For example, if n = 5, the middle node is the 2nd node (0-based index), as ⌊5 / 2⌋ = 2.
- If n = 6, the middle node is the 3rd node (0-based index), as ⌊6 / 2⌋ = 3.

You cannot return the same linked list without modifying it. Instead, you should delete the middle node and return the modified linked list.

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 1 <= Node.val <= 10^5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(head: ListNode) -> ListNode:
    """
    Deletes the middle node of a linked list and returns the modified list.
    """
    # Edge case: If the list has only one node, return None
    if not head or not head.next:
        return None

    # Use two pointers: slow and fast
    slow, fast = head, head
    prev = None  # To keep track of the node before the middle node

    # Move fast pointer twice as fast as the slow pointer
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Delete the middle node
    prev.next = slow.next

    return head

# Example Test Cases
def print_linked_list(head: ListNode):
    """Helper function to print a linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1: Odd number of nodes
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Test Case 1:", print_linked_list(deleteMiddle(head1)))  # Output: [1, 2, 4, 5]

# Test Case 2: Even number of nodes
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print("Test Case 2:", print_linked_list(deleteMiddle(head2)))  # Output: [1, 2, 4]

# Test Case 3: Single node
head3 = ListNode(1)
print("Test Case 3:", print_linked_list(deleteMiddle(head3)))  # Output: []

# Test Case 4: Two nodes
head4 = ListNode(1, ListNode(2))
print("Test Case 4:", print_linked_list(deleteMiddle(head4)))  # Output: [1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm traverses the linked list once using the two-pointer technique.
- Therefore, the time complexity is O(n), where n is the number of nodes in the linked list.

Space Complexity:
- The algorithm uses a constant amount of extra space (pointers: slow, fast, and prev).
- Therefore, the space complexity is O(1).

Topic: Linked List
"""