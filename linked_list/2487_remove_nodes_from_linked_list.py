"""
LeetCode Question #2487: Remove Nodes From Linked List

Problem Statement:
You are given the head of a linked list.

Remove every node which has a node with a strictly greater value anywhere to the right side of it.

Return the head of the modified linked list.

Example 1:
Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes 5, 2, and 3 are removed because there is a node with a greater value to the right of them.

Example 2:
Input: head = [1,10,5,7,9]
Output: [10,9]
Explanation: The nodes 1, 5, and 7 are removed because there is a node with a greater value to the right of them.

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 1 <= Node.val <= 10^5
"""

# Solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNodes(head: ListNode) -> ListNode:
    """
    Removes nodes from the linked list that have a strictly greater value to their right.
    """
    # Reverse the linked list
    def reverse(head):
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

    # Reverse the linked list
    reversed_head = reverse(head)

    # Traverse the reversed list and keep track of the maximum value seen so far
    max_val = float('-inf')
    dummy = ListNode(0)
    current = dummy

    while reversed_head:
        if reversed_head.val >= max_val:
            max_val = reversed_head.val
            current.next = reversed_head
            current = current.next
        reversed_head = reversed_head.next

    # Terminate the new list
    current.next = None

    # Reverse the list again to restore the original order
    return reverse(dummy.next)

# Example Test Cases
def print_linked_list(head):
    """Helper function to print linked list values."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1
head1 = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
result1 = removeNodes(head1)
print(print_linked_list(result1))  # Output: [13, 8]

# Test Case 2
head2 = ListNode(1, ListNode(10, ListNode(5, ListNode(7, ListNode(9)))))
result2 = removeNodes(head2)
print(print_linked_list(result2))  # Output: [10, 9]

# Test Case 3
head3 = ListNode(3, ListNode(2, ListNode(1)))
result3 = removeNodes(head3)
print(print_linked_list(result3))  # Output: [3]

# Test Case 4
head4 = ListNode(1, ListNode(2, ListNode(3)))
result4 = removeNodes(head4)
print(print_linked_list(result4))  # Output: [3]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Reversing the linked list takes O(n), where n is the number of nodes in the list.
- Traversing the reversed list and constructing the new list takes O(n).
- Reversing the list again takes O(n).
- Overall, the time complexity is O(n).

Space Complexity:
- The algorithm uses O(1) extra space since it modifies the linked list in place and does not use any additional data structures.
- Overall, the space complexity is O(1).

Topic: Linked List
"""