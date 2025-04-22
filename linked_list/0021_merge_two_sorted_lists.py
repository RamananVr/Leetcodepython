"""
LeetCode Question #21: Merge Two Sorted Lists

Problem Statement:
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one sorted linked list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:
1. The number of nodes in both lists is in the range [0, 50].
2. -100 <= Node.val <= 100
3. Both `list1` and `list2` are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    Merges two sorted linked lists into one sorted linked list.

    Args:
    list1 (ListNode): The head of the first sorted linked list.
    list2 (ListNode): The head of the second sorted linked list.

    Returns:
    ListNode: The head of the merged sorted linked list.
    """
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

    # Return the merged list starting from the next of dummy node
    return dummy.next

# Example Test Cases
def print_list(head: ListNode):
    """Helper function to print a linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
merged = mergeTwoLists(list1, list2)
print("Test Case 1:", print_list(merged))  # Output: [1, 1, 2, 3, 4, 4]

# Test Case 2
list1 = None
list2 = ListNode(0)
merged = mergeTwoLists(list1, list2)
print("Test Case 2:", print_list(merged))  # Output: [0]

# Test Case 3
list1 = None
list2 = None
merged = mergeTwoLists(list1, list2)
print("Test Case 3:", print_list(merged))  # Output: []

# Test Case 4
list1 = ListNode(5)
list2 = ListNode(1, ListNode(2, ListNode(3)))
merged = mergeTwoLists(list1, list2)
print("Test Case 4:", print_list(merged))  # Output: [1, 2, 3, 5]

"""
Time Complexity Analysis:
- The function iterates through both linked lists once, comparing and merging nodes.
- Let `n` be the number of nodes in `list1` and `m` be the number of nodes in `list2`.
- The time complexity is O(n + m), as we traverse each list once.

Space Complexity Analysis:
- The function uses a constant amount of extra space (dummy node and pointers).
- The space complexity is O(1).

Topic: Linked List
"""