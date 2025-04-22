"""
LeetCode Question #237: Delete Node in a Linked List

Problem Statement:
There is a singly linked list, and you are given access to a node `node` in the list. 
You are not given access to the head of the list. You are tasked with deleting the given `node` 
from the linked list. The input node will not be the tail and will always be a valid node of the linked list.

Note:
- The linked list will have at least two elements.
- All the values in the linked list are unique.
- You must solve the problem without modifying the structure of the linked list.

Example:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

Constraints:
- The number of nodes in the list is in the range [2, 1000].
- -1000 <= Node.val <= 1000
- The value of each node in the list is unique.
- The `node` to be deleted is not a tail node in the list.
"""

# Clean and Correct Python Solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node: ListNode) -> None:
    """
    Deletes the given node from the linked list by copying the value of the next node
    into the current node and bypassing the next node.
    """
    # Copy the value of the next node into the current node
    node.val = node.next.val
    # Bypass the next node
    node.next = node.next.next

# Example Test Cases
def print_linked_list(head: ListNode) -> None:
    """Helper function to print the linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Test Case 1
head1 = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
node_to_delete1 = head1.next  # Node with value 5
deleteNode(node_to_delete1)
print_linked_list(head1)  # Expected Output: [4, 1, 9]

# Test Case 2
head2 = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
node_to_delete2 = head2.next.next  # Node with value 1
deleteNode(node_to_delete2)
print_linked_list(head2)  # Expected Output: [4, 5, 9]

# Test Case 3
head3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
node_to_delete3 = head3.next.next  # Node with value 3
deleteNode(node_to_delete3)
print_linked_list(head3)  # Expected Output: [1, 2, 4]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The operation of copying the value of the next node and bypassing it is O(1).
- Therefore, the time complexity is O(1).

Space Complexity:
- No additional data structures are used, and the operation is performed in-place.
- Therefore, the space complexity is O(1).
"""

# Topic: Linked List