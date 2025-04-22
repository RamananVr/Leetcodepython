"""
LeetCode Question #143: Reorder List

Problem Statement:
You are given the head of a singly linked list. The list is represented as:
    L0 → L1 → … → Ln - 1 → Ln
Reorder the list to:
    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes, only the node structure.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
- The number of nodes in the list is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 1000
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: ListNode) -> None:
    """
    Reorders the given linked list in-place.
    """
    if not head or not head.next:
        return

    # Step 1: Find the middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    prev, curr = None, slow
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # Step 3: Merge the two halves
    first, second = head, prev
    while second.next:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2

# Example Test Cases
def print_list(head: ListNode):
    """Helper function to print the linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
reorderList(head1)
print(print_list(head1))  # Output: [1, 4, 2, 3]

# Test Case 2
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reorderList(head2)
print(print_list(head2))  # Output: [1, 5, 2, 4, 3]

# Test Case 3
head3 = ListNode(1)
reorderList(head3)
print(print_list(head3))  # Output: [1]

# Test Case 4
head4 = ListNode(1, ListNode(2))
reorderList(head4)
print(print_list(head4))  # Output: [1, 2]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Finding the middle of the list: O(n), where n is the number of nodes in the list.
- Reversing the second half of the list: O(n/2) = O(n).
- Merging the two halves: O(n).
Overall: O(n).

Space Complexity:
- The algorithm uses O(1) extra space since it modifies the list in-place.
Overall: O(1).

Topic: Linked List
"""