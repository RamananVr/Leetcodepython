"""
LeetCode Problem #206: Reverse Linked List

Problem Statement:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Clean, Correct Python Solution (Iterative Approach)
def reverseList(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next  # Save the next node
        current.next = prev       # Reverse the current node's pointer
        prev = current            # Move prev to the current node
        current = next_node       # Move to the next node
    return prev

# Example Test Cases
def print_linked_list(head: ListNode):
    """Helper function to print a linked list as a Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def create_linked_list(values):
    """Helper function to create a linked list from a Python list."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

if __name__ == "__main__":
    # Test Case 1
    head = create_linked_list([1, 2, 3, 4, 5])
    reversed_head = reverseList(head)
    print(print_linked_list(reversed_head))  # Output: [5, 4, 3, 2, 1]

    # Test Case 2
    head = create_linked_list([1, 2])
    reversed_head = reverseList(head)
    print(print_linked_list(reversed_head))  # Output: [2, 1]

    # Test Case 3
    head = create_linked_list([])
    reversed_head = reverseList(head)
    print(print_linked_list(reversed_head))  # Output: []

"""
Time Complexity Analysis:
- The function iterates through the linked list once, performing O(1) operations for each node.
- Let n be the number of nodes in the linked list.
- Time Complexity: O(n)

Space Complexity Analysis:
- The function uses a constant amount of extra space (pointers `prev`, `current`, and `next_node`).
- Space Complexity: O(1)

Topic: Linked List
"""