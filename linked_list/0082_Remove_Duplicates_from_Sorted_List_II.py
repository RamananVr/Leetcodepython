"""
LeetCode Problem #82: Remove Duplicates from Sorted List II

Problem Statement:
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:
- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    """
    Removes all nodes with duplicate values from a sorted linked list.
    """
    # Create a dummy node to handle edge cases (e.g., head being part of duplicates)
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy  # Pointer to the node before the current sequence of duplicates

    while head:
        # Check if the current node is the start of a sequence of duplicates
        if head.next and head.val == head.next.val:
            # Skip all nodes with the same value
            while head.next and head.val == head.next.val:
                head = head.next
            # Connect prev to the node after the duplicates
            prev.next = head.next
        else:
            # Move prev forward if no duplicates are found
            prev = prev.next
        # Move head forward
        head = head.next

    return dummy.next

# Example Test Cases
def print_list(head: ListNode):
    """Helper function to print linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
print("Test Case 1 Output:", print_list(deleteDuplicates(head1)))  # Expected Output: [1, 2, 5]

# Test Case 2
head2 = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
print("Test Case 2 Output:", print_list(deleteDuplicates(head2)))  # Expected Output: [2, 3]

# Test Case 3
head3 = ListNode(1, ListNode(1))
print("Test Case 3 Output:", print_list(deleteDuplicates(head3)))  # Expected Output: []

# Test Case 4
head4 = ListNode(1, ListNode(2, ListNode(3)))
print("Test Case 4 Output:", print_list(deleteDuplicates(head4)))  # Expected Output: [1, 2, 3]

# Test Case 5
head5 = None
print("Test Case 5 Output:", print_list(deleteDuplicates(head5)))  # Expected Output: []

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm traverses the linked list once, performing O(1) operations for each node.
- Therefore, the time complexity is O(n), where n is the number of nodes in the linked list.

Space Complexity:
- The algorithm uses a constant amount of extra space (dummy node and pointers).
- Therefore, the space complexity is O(1).

Topic: Linked List
"""