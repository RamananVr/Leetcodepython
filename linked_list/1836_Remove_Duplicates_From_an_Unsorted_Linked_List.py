"""
LeetCode Problem #1836: Remove Duplicates From an Unsorted Linked List

Problem Statement:
Given the head of a linked list, find all the elements that appear only once in the list and delete the rest. 
Return the linked list sorted as it was in the input.

Example 1:
Input: head = [3, 2, 2, 1, 3, 4, 5]
Output: [1, 4, 5]

Example 2:
Input: head = [1, 2, 3, 2]
Output: [1, 3]

Constraints:
- The number of nodes in the linked list is in the range [1, 10^5].
- -10^5 <= Node.val <= 10^5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicatesUnsorted(head: ListNode) -> ListNode:
    """
    Removes all nodes from the linked list that have duplicate values.
    """
    from collections import Counter

    # Step 1: Count the frequency of each value in the linked list
    current = head
    freq = Counter()
    while current:
        freq[current.val] += 1
        current = current.next

    # Step 2: Create a dummy node and filter out duplicates
    dummy = ListNode(0)
    dummy.next = head
    prev, current = dummy, head

    while current:
        if freq[current.val] > 1:  # If the value is a duplicate, skip it
            prev.next = current.next
        else:  # Otherwise, keep the node
            prev = current
        current = current.next

    return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    head = create_linked_list([3, 2, 2, 1, 3, 4, 5])
    result = deleteDuplicatesUnsorted(head)
    print(linked_list_to_list(result))  # Output: [1, 4, 5]

    # Test Case 2
    head = create_linked_list([1, 2, 3, 2])
    result = deleteDuplicatesUnsorted(head)
    print(linked_list_to_list(result))  # Output: [1, 3]

    # Test Case 3
    head = create_linked_list([1, 1, 1, 1])
    result = deleteDuplicatesUnsorted(head)
    print(linked_list_to_list(result))  # Output: []

    # Test Case 4
    head = create_linked_list([10, 20, 30, 40])
    result = deleteDuplicatesUnsorted(head)
    print(linked_list_to_list(result))  # Output: [10, 20, 30, 40]

"""
Time Complexity:
- Counting the frequency of each value takes O(n), where n is the number of nodes in the linked list.
- Traversing the linked list again to filter out duplicates also takes O(n).
- Overall time complexity: O(n).

Space Complexity:
- The Counter object stores the frequency of each value, which requires O(u) space, where u is the number of unique values in the linked list.
- Overall space complexity: O(u).

Topic: Linked List
"""