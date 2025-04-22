"""
LeetCode Problem #61: Rotate List

Problem Statement:
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:
1. The number of nodes in the list is in the range [0, 500].
2. -100 <= Node.val <= 100
3. 0 <= k <= 2 * 10^9
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head or not head.next or k == 0:
        return head

    # Step 1: Compute the length of the list
    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1

    # Step 2: Make the list circular
    current.next = head

    # Step 3: Find the new head
    k = k % length  # Handle cases where k > length
    steps_to_new_head = length - k
    new_tail = head
    for _ in range(steps_to_new_head - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None  # Break the circular link

    return new_head

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
    head = create_linked_list([1, 2, 3, 4, 5])
    k = 2
    rotated = rotateRight(head, k)
    print(linked_list_to_list(rotated))  # Output: [4, 5, 1, 2, 3]

    # Test Case 2
    head = create_linked_list([0, 1, 2])
    k = 4
    rotated = rotateRight(head, k)
    print(linked_list_to_list(rotated))  # Output: [2, 0, 1]

    # Test Case 3
    head = create_linked_list([1, 2])
    k = 3
    rotated = rotateRight(head, k)
    print(linked_list_to_list(rotated))  # Output: [2, 1]

    # Test Case 4
    head = create_linked_list([])
    k = 1
    rotated = rotateRight(head, k)
    print(linked_list_to_list(rotated))  # Output: []

"""
Time Complexity Analysis:
1. Calculating the length of the list takes O(n), where n is the number of nodes in the list.
2. Making the list circular and finding the new head also takes O(n).
3. Overall, the time complexity is O(n).

Space Complexity Analysis:
1. The algorithm uses O(1) additional space since no extra data structures are used.

Topic: Linked List
"""