"""
LeetCode Question #2046: Sort Linked List Already Sorted by Absolute Values

Problem Statement:
Given the head of a singly linked list that is sorted based on absolute values, 
rearrange the list to be sorted based on actual values. Return the head of the modified linked list.

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- -10^5 <= Node.val <= 10^5
- The linked list is sorted based on absolute values.

Example:
Input: head = [-5, -3, 2, 3, 5]
Output: [-5, -3, 2, 3, 5]
Explanation: The list is already sorted based on absolute values. Rearranging it based on actual values results in [-5, -3, 2, 3, 5].

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortLinkedList(head: ListNode) -> ListNode:
    """
    Rearranges a linked list sorted by absolute values to be sorted by actual values.
    """
    # Create two dummy nodes for negative and non-negative values
    negative_dummy = ListNode(0)
    non_negative_dummy = ListNode(0)
    
    # Pointers to build the two lists
    negative = negative_dummy
    non_negative = non_negative_dummy
    
    # Traverse the original list
    current = head
    while current:
        if current.val < 0:
            negative.next = current
            negative = negative.next
        else:
            non_negative.next = current
            non_negative = non_negative.next
        current = current.next
    
    # Terminate the two lists
    negative.next = None
    non_negative.next = None
    
    # Reverse the negative list
    prev = None
    current = negative_dummy.next
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    # Connect the reversed negative list to the non-negative list
    if prev:
        negative_dummy.next = prev
        negative.next = non_negative_dummy.next
    else:
        negative_dummy.next = non_negative_dummy.next
    
    return negative_dummy.next

# Example Test Cases
def print_linked_list(head):
    """Helper function to print linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1
head = ListNode(-5, ListNode(-3, ListNode(2, ListNode(3, ListNode(5)))))
sorted_head = sortLinkedList(head)
print(print_linked_list(sorted_head))  # Output: [-5, -3, 2, 3, 5]

# Test Case 2
head = ListNode(-10, ListNode(-7, ListNode(-3, ListNode(1, ListNode(4, ListNode(8))))))
sorted_head = sortLinkedList(head)
print(print_linked_list(sorted_head))  # Output: [-10, -7, -3, 1, 4, 8]

# Test Case 3
head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
sorted_head = sortLinkedList(head)
print(print_linked_list(sorted_head))  # Output: [0, 1, 2, 3, 4]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Traversing the linked list to separate negative and non-negative values: O(n)
- Reversing the negative list: O(n)
- Connecting the two lists: O(1)
Overall: O(n)

Space Complexity:
- No additional data structures are used apart from a few pointers.
Overall: O(1)
"""

# Topic: Linked List