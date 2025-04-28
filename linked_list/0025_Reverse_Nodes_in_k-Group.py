"""
LeetCode Problem #25: Reverse Nodes in k-Group

Problem Statement:
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes
is not a multiple of k then left-out nodes, in the end, should remain as they are.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
- The number of nodes in the list is n.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000

Follow-up:
Can you solve the problem in O(1) extra memory space?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    def reverse_linked_list(start, end):
        """Reverse the linked list from start to end."""
        prev, curr = None, start
        while curr != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy

    while True:
        # Find the kth node from the current position
        kth_node = prev_group_end
        for _ in range(k):
            kth_node = kth_node.next
            if not kth_node:
                return dummy.next

        # Reverse the k nodes
        group_start = prev_group_end.next
        group_end = kth_node.next
        kth_node.next = None  # Temporarily break the chain
        reversed_group = reverse_linked_list(group_start, group_end)

        # Connect the reversed group back to the list
        prev_group_end.next = reversed_group
        group_start.next = group_end

        # Move prev_group_end to the end of the reversed group
        prev_group_end = group_start

# Example Test Cases
def print_linked_list(head):
    """Helper function to print linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k1 = 2
result1 = reverseKGroup(head1, k1)
print(print_linked_list(result1))  # Output: [2, 1, 4, 3, 5]

# Test Case 2
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k2 = 3
result2 = reverseKGroup(head2, k2)
print(print_linked_list(result2))  # Output: [3, 2, 1, 4, 5]

# Test Case 3
head3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k3 = 1
result3 = reverseKGroup(head3, k3)
print(print_linked_list(result3))  # Output: [1, 2, 3, 4, 5]

# Test Case 4
head4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k4 = 5
result4 = reverseKGroup(head4, k4)
print(print_linked_list(result4))  # Output: [5, 4, 3, 2, 1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm traverses the entire linked list once, and for each group of k nodes, it reverses the group.
- Reversing a group of k nodes takes O(k) time.
- Therefore, the overall time complexity is O(n), where n is the number of nodes in the linked list.

Space Complexity:
- The algorithm uses O(1) extra space for reversing the nodes in-place.
- Therefore, the space complexity is O(1).

Topic: Linked List
"""