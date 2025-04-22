"""
LeetCode Problem #21: Merge Two Sorted Lists

Problem Statement:
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one sorted linked list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both `list1` and `list2` are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # Create a dummy node to simplify edge cases
    dummy = ListNode(-1)
    current = dummy

    # Traverse both lists and merge them in sorted order
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach the remaining nodes from either list1 or list2
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    # Return the merged list starting from the next node of dummy
    return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a Python list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))  # Output: [1, 1, 2, 3, 4, 4]

    # Test Case 2
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged = mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))  # Output: []

    # Test Case 3
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged = mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))  # Output: [0]

# Topic: Linked List