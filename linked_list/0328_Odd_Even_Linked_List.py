"""
LeetCode Problem #328: Odd Even Linked List

Problem Statement:
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, 
and return the reordered list.

The first node is considered odd, and the second node is even, and so on. Note that the relative order inside both the odd 
and even groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Constraints:
- The number of nodes in the linked list is in the range [0, 10^4].
- -10^6 <= Node.val <= 10^6
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head: ListNode) -> ListNode:
    """
    Reorders the linked list such that all odd-indexed nodes come before even-indexed nodes.
    """
    if not head or not head.next:
        return head

    # Initialize pointers for odd and even lists
    odd = head
    even = head.next
    even_head = even  # Save the head of the even list to connect later

    # Traverse the list and separate odd and even nodes
    while even and even.next:
        odd.next = even.next  # Connect odd nodes
        odd = odd.next       # Move odd pointer forward
        even.next = odd.next # Connect even nodes
        even = even.next     # Move even pointer forward

    # Connect the end of the odd list to the head of the even list
    odd.next = even_head

    return head

# Example Test Cases
def print_linked_list(head: ListNode):
    """Helper function to print linked list values."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Test Case 1:", print_linked_list(oddEvenList(head1)))  # Output: [1, 3, 5, 2, 4]

# Test Case 2
head2 = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
print("Test Case 2:", print_linked_list(oddEvenList(head2)))  # Output: [2, 3, 6, 7, 1, 5, 4]

# Test Case 3 (Edge Case: Empty List)
head3 = None
print("Test Case 3:", print_linked_list(oddEvenList(head3)))  # Output: []

# Test Case 4 (Edge Case: Single Node)
head4 = ListNode(1)
print("Test Case 4:", print_linked_list(oddEvenList(head4)))  # Output: [1]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm traverses the linked list once, performing O(1) operations for each node.
- Therefore, the time complexity is O(n), where n is the number of nodes in the linked list.

Space Complexity:
- The algorithm uses a constant amount of extra space (pointers for odd, even, and even_head).
- Therefore, the space complexity is O(1).
"""

# Topic: Linked List