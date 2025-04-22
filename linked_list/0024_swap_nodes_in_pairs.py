"""
LeetCode Question #24: Swap Nodes in Pairs

Problem Statement:
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed).

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Constraints:
- The number of nodes in the list is in the range [0, 100].
- 0 <= Node.val <= 100
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    """
    Swap every two adjacent nodes in the linked list.
    """
    # Base case: if the list is empty or has only one node, return the head
    if not head or not head.next:
        return head

    # Initialize pointers
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        # Identify the two nodes to be swapped
        first = prev.next
        second = prev.next.next

        # Perform the swap
        prev.next = second
        first.next = second.next
        second.next = first

        # Move the prev pointer forward
        prev = first

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
    head = create_linked_list([1, 2, 3, 4])
    swapped = swapPairs(head)
    print(linked_list_to_list(swapped))  # Output: [2, 1, 4, 3]

    # Test Case 2
    head = create_linked_list([])
    swapped = swapPairs(head)
    print(linked_list_to_list(swapped))  # Output: []

    # Test Case 3
    head = create_linked_list([1])
    swapped = swapPairs(head)
    print(linked_list_to_list(swapped))  # Output: [1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm traverses the linked list once, performing constant-time operations for each pair of nodes.
- Let n be the number of nodes in the linked list. The time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space (dummy node and pointers).
- The space complexity is O(1).

Topic: Linked List
"""