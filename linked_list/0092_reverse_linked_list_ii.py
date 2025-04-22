"""
LeetCode Question #92: Reverse Linked List II

Problem Statement:
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.

Constraints:
- The number of nodes in the list is n.
- 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n

Follow-up:
Could you do it in one pass?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    """
    Reverse the nodes of the linked list from position `left` to `right`.
    """
    # Edge case: If the list is empty or left == right, no need to reverse
    if not head or left == right:
        return head

    # Create a dummy node to simplify edge cases
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Step 1: Move `prev` to the node before `left`
    for _ in range(left - 1):
        prev = prev.next

    # Step 2: Reverse the sublist from `left` to `right`
    current = prev.next
    next_node = None
    for _ in range(right - left + 1):
        temp = current.next
        current.next = next_node
        next_node = current
        current = temp

    # Step 3: Connect the reversed sublist back to the original list
    prev.next.next = current
    prev.next = next_node

    return dummy.next

# Example Test Cases
def print_list(head: ListNode):
    """Helper function to print the linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
left1, right1 = 2, 4
result1 = reverseBetween(head1, left1, right1)
print(print_list(result1))  # Output: [1, 4, 3, 2, 5]

# Test Case 2
head2 = ListNode(1)
left2, right2 = 1, 1
result2 = reverseBetween(head2, left2, right2)
print(print_list(result2))  # Output: [1]

# Test Case 3
head3 = ListNode(1)
head3.next = ListNode(2)
left3, right3 = 1, 2
result3 = reverseBetween(head3, left3, right3)
print(print_list(result3))  # Output: [2, 1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm traverses the list once to reach the `left` position (O(left)).
- Then, it reverses the sublist from `left` to `right` (O(right - left)).
- Overall, the time complexity is O(n), where n is the number of nodes in the list.

Space Complexity:
- The algorithm uses a constant amount of extra space (O(1)).
- No additional data structures are used.

Topic: Linked List
"""