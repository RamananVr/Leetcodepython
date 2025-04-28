"""
LeetCode Problem #1171: Remove Zero Sum Consecutive Nodes from Linked List

Problem Statement:
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences. After doing so, return the head of the final linked list.

You may return any such solution. Note that the linked list is not guaranteed to be unique.

Example 1:
Input: head = [1,2,-3,3,1]
Output: [3,1]
Explanation: The consecutive nodes [1,2,-3] sum to 0. After removing them, the linked list becomes [3,1].

Example 2:
Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Explanation: The consecutive nodes [3,-3] sum to 0. After removing them, the linked list becomes [1,2,4].

Example 3:
Input: head = [1,2,3,-3,-2]
Output: [1]

Constraints:
- The given linked list will contain between 1 and 1000 nodes.
- Each node in the linked list has a value between -1000 and 1000.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head: ListNode) -> ListNode:
    """
    Removes consecutive nodes in the linked list that sum to zero.
    """
    # Create a dummy node to simplify edge cases
    dummy = ListNode(0)
    dummy.next = head
    
    # Use a prefix sum and a dictionary to track nodes
    prefix_sum = 0
    seen = {}
    seen[prefix_sum] = dummy
    
    # First pass: calculate prefix sums and store the last occurrence of each sum
    current = head
    while current:
        prefix_sum += current.val
        seen[prefix_sum] = current
        current = current.next
    
    # Second pass: remove zero-sum sublists
    prefix_sum = 0
    current = dummy
    while current:
        prefix_sum += current.val
        current.next = seen[prefix_sum].next
        current = current.next
    
    return dummy.next

# Example Test Cases
def print_linked_list(head: ListNode):
    """Helper function to print linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1
head1 = ListNode(1, ListNode(2, ListNode(-3, ListNode(3, ListNode(1)))))
print(print_linked_list(removeZeroSumSublists(head1)))  # Output: [3, 1]

# Test Case 2
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(-3, ListNode(4)))))
print(print_linked_list(removeZeroSumSublists(head2)))  # Output: [1, 2, 4]

# Test Case 3
head3 = ListNode(1, ListNode(2, ListNode(3, ListNode(-3, ListNode(-2)))))
print(print_linked_list(removeZeroSumSublists(head3)))  # Output: [1]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm performs two passes over the linked list.
- In the first pass, we calculate prefix sums and store them in a dictionary. This takes O(n) time, where n is the number of nodes in the linked list.
- In the second pass, we use the dictionary to adjust the pointers in the linked list, which also takes O(n) time.
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(n) due to the dictionary used to store prefix sums and their corresponding nodes.
- The dictionary can grow up to the size of the linked list in the worst case.
"""

# Topic: Linked List