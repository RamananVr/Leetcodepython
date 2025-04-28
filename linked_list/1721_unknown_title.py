"""
LeetCode Problem #1721: Swapping Nodes in a Linked List

Problem Statement:
You are given the head of a linked list, and an integer k. Return the head of the linked list after swapping the values 
of the k-th node from the beginning and the k-th node from the end (the list is 1-indexed).

Note:
- The k-th node from the beginning is the k-th node in the list.
- The k-th node from the end is the (n-k+1)-th node in the list, where n is the length of the list.
- It is guaranteed that k is a valid integer for the given linked list.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [1,2,3,4,5], k = 1
Output: [5,2,3,4,1]

Constraints:
- The number of nodes in the list is n.
- 1 <= k <= n <= 10^5
- 0 <= Node.val <= 10^9
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapNodes(head: ListNode, k: int) -> ListNode:
    """
    Swaps the values of the k-th node from the beginning and the k-th node from the end in a linked list.
    """
    # Step 1: Find the length of the linked list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    # Step 2: Find the k-th node from the beginning and the k-th node from the end
    first_k_node = head
    for _ in range(k - 1):
        first_k_node = first_k_node.next

    second_k_node = head
    for _ in range(length - k):
        second_k_node = second_k_node.next

    # Step 3: Swap the values of the two nodes
    first_k_node.val, second_k_node.val = second_k_node.val, first_k_node.val

    return head

# Example Test Cases
def print_linked_list(head: ListNode):
    """Helper function to print a linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k1 = 2
result1 = swapNodes(head1, k1)
print(print_linked_list(result1))  # Output: [1, 4, 3, 2, 5]

# Test Case 2
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k2 = 1
result2 = swapNodes(head2, k2)
print(print_linked_list(result2))  # Output: [5, 2, 3, 4, 1]

# Test Case 3
head3 = ListNode(7, ListNode(9, ListNode(6, ListNode(6, ListNode(7, ListNode(8, ListNode(3, ListNode(0))))))))
k3 = 5
result3 = swapNodes(head3, k3)
print(print_linked_list(result3))  # Output: [7, 9, 6, 6, 8, 7, 3, 0]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Finding the length of the linked list takes O(n), where n is the number of nodes in the list.
- Traversing to the k-th node from the beginning and the k-th node from the end each take O(n).
- Swapping the values is O(1).
- Overall time complexity: O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space (no additional data structures are used).
- Overall space complexity: O(1).
"""

# Topic: Linked List