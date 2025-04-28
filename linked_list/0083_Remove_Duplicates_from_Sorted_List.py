"""
LeetCode Problem #83: Remove Duplicates from Sorted List

Problem Statement:
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:
- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is sorted in ascending order.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    """
    Removes duplicates from a sorted linked list.

    :param head: ListNode - The head of the sorted linked list.
    :return: ListNode - The head of the modified linked list with duplicates removed.
    """
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next  # Skip the duplicate node
        else:
            current = current.next  # Move to the next node
    return head

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
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    head1 = create_linked_list([1, 1, 2])
    result1 = deleteDuplicates(head1)
    print(linked_list_to_list(result1))  # Output: [1, 2]

    # Test Case 2
    head2 = create_linked_list([1, 1, 2, 3, 3])
    result2 = deleteDuplicates(head2)
    print(linked_list_to_list(result2))  # Output: [1, 2, 3]

    # Test Case 3
    head3 = create_linked_list([])
    result3 = deleteDuplicates(head3)
    print(linked_list_to_list(result3))  # Output: []

    # Test Case 4
    head4 = create_linked_list([1, 1, 1, 1, 1])
    result4 = deleteDuplicates(head4)
    print(linked_list_to_list(result4))  # Output: [1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm traverses the linked list once, performing O(1) operations for each node.
- Let n be the number of nodes in the linked list. The time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space (no additional data structures are used).
- The space complexity is O(1).

Topic: Linked List
"""