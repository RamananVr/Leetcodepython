"""
LeetCode Question #19: Remove Nth Node From End of List

Problem Statement:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
- The number of nodes in the list is `sz`.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

Follow up:
Could you do this in one pass?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    """
    Removes the nth node from the end of the linked list.
    """
    # Create a dummy node to simplify edge cases (e.g., removing the head)
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    # Move the first pointer n + 1 steps ahead
    for _ in range(n + 1):
        first = first.next

    # Move both pointers until the first pointer reaches the end
    while first:
        first = first.next
        second = second.next

    # Remove the nth node
    second.next = second.next.next

    return dummy.next

# Example Test Cases
def print_linked_list(head):
    """Helper function to print linked list as a Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n1 = 2
result1 = removeNthFromEnd(head1, n1)
print(print_linked_list(result1))  # Output: [1, 2, 3, 5]

# Test Case 2
head2 = ListNode(1)
n2 = 1
result2 = removeNthFromEnd(head2, n2)
print(print_linked_list(result2))  # Output: []

# Test Case 3
head3 = ListNode(1, ListNode(2))
n3 = 1
result3 = removeNthFromEnd(head3, n3)
print(print_linked_list(result3))  # Output: [1]

# Time and Space Complexity Analysis
# Time Complexity: O(sz), where sz is the number of nodes in the linked list.
# - The algorithm traverses the list twice: once to move the first pointer n + 1 steps, and once to find the nth node.

# Space Complexity: O(1)
# - The algorithm uses a constant amount of extra space.

# Topic: Linked List