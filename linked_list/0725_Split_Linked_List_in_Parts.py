"""
LeetCode Problem #725: Split Linked List in Parts

Problem Statement:
Given the head of a singly linked list and an integer k, split the linked list into k consecutive parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. 
This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size 
greater than or equal to parts occurring later.

Return an array of the k parts.

Constraints:
- The number of nodes in the list is in the range [0, 1000].
- 0 <= Node.val <= 1000
- 1 <= k <= 50
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def splitListToParts(head: ListNode, k: int):
    """
    Splits the linked list into k parts as evenly as possible.
    """
    # Step 1: Count the total number of nodes in the linked list
    total_length = 0
    current = head
    while current:
        total_length += 1
        current = current.next

    # Step 2: Determine the size of each part
    part_size = total_length // k  # Minimum size of each part
    extra_nodes = total_length % k  # Extra nodes to distribute

    # Step 3: Split the list into parts
    result = []
    current = head
    for i in range(k):
        part_head = current
        # Determine the size of the current part
        current_part_size = part_size + (1 if i < extra_nodes else 0)
        # Traverse the current part
        for j in range(current_part_size - 1):
            if current:
                current = current.next
        # Break the link to the next part
        if current:
            next_part = current.next
            current.next = None
            current = next_part
        # Add the current part to the result
        result.append(part_head)

    return result

# Example Test Cases
def print_linked_list(head):
    """Helper function to print a linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 3
result = splitListToParts(head, k)
print([print_linked_list(part) for part in result])  # Output: [[1, 2], [3, 4], [5]]

# Test Case 2
head = ListNode(1, ListNode(2, ListNode(3)))
k = 5
result = splitListToParts(head, k)
print([print_linked_list(part) for part in result])  # Output: [[1], [2], [3], [], []]

# Test Case 3
head = None
k = 3
result = splitListToParts(head, k)
print([print_linked_list(part) for part in result])  # Output: [[], [], []]

# Time and Space Complexity Analysis
# Time Complexity:
# - Counting the total number of nodes takes O(n), where n is the number of nodes in the linked list.
# - Splitting the list into k parts involves traversing the list again, which is also O(n).
# - Overall time complexity: O(n).

# Space Complexity:
# - The algorithm uses O(1) additional space since we are modifying the linked list in place.
# - The result list of size k is returned, but this is required by the problem and does not count as extra space.
# - Overall space complexity: O(1).

# Topic: Linked List