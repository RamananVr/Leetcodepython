"""
LeetCode Question #203: Remove Linked List Elements

Problem Statement:
Given the head of a linked list and an integer `val`, remove all the nodes of the linked list that have `Node.val == val`, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []

Constraints:
- The number of nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- -10^5 <= val <= 10^5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: ListNode, val: int) -> ListNode:
    """
    Removes all nodes with the value `val` from the linked list.
    """
    # Create a dummy node to handle edge cases (e.g., removing the head node)
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    # Traverse the list and remove nodes with the target value
    while current.next:
        if current.next.val == val:
            current.next = current.next.next  # Skip the node with value `val`
        else:
            current = current.next  # Move to the next node

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
head1 = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
val1 = 6
print(print_linked_list(removeElements(head1, val1)))  # Output: [1, 2, 3, 4, 5]

# Test Case 2
head2 = None
val2 = 1
print(print_linked_list(removeElements(head2, val2)))  # Output: []

# Test Case 3
head3 = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
val3 = 7
print(print_linked_list(removeElements(head3, val3)))  # Output: []

# Test Case 4
head4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
val4 = 10
print(print_linked_list(removeElements(head4, val4)))  # Output: [1, 2, 3, 4, 5]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm traverses the entire linked list once, performing O(1) operations for each node.
- Therefore, the time complexity is O(n), where n is the number of nodes in the linked list.

Space Complexity:
- The algorithm uses a constant amount of extra space (dummy node and pointers).
- Therefore, the space complexity is O(1).
"""

# Topic: Linked List