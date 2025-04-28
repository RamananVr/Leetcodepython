"""
LeetCode Problem #2181: Merge Nodes in Between Zeros

Problem Statement:
You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will always have a value of 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.

Example:
Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation: 
- The nodes between the first two 0's are [3,1]. Their sum is 4.
- The nodes between the second two 0's are [4,5,2]. Their sum is 11.
- We return the list [4,11].

Constraints:
- The number of nodes in the list is between 3 and 10^5.
- 0 <= Node.val <= 1000
- There are no two consecutive nodes with the value 0.
- The beginning and end of the linked list have the value 0.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeNodes(head: ListNode) -> ListNode:
    """
    Merges nodes between zeros in a linked list and returns the modified list.
    """
    # Initialize pointers
    dummy = ListNode(0)  # Dummy node to simplify list construction
    current = dummy
    sum_between_zeros = 0

    # Traverse the linked list starting from the first node after the initial 0
    head = head.next
    while head:
        if head.val == 0:
            # When encountering a 0, finalize the current segment
            current.next = ListNode(sum_between_zeros)
            current = current.next
            sum_between_zeros = 0  # Reset the sum for the next segment
        else:
            # Accumulate the sum of values between zeros
            sum_between_zeros += head.val
        head = head.next

    return dummy.next

# Example Test Cases
def print_linked_list(head: ListNode):
    """Helper function to print a linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Test Case 1
head = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))
result = mergeNodes(head)
print_linked_list(result)  # Output: [4, 11]

# Test Case 2
head = ListNode(0, ListNode(1, ListNode(0, ListNode(0, ListNode(2, ListNode(3, ListNode(0)))))))
result = mergeNodes(head)
print_linked_list(result)  # Output: [1, 0, 5]

# Test Case 3
head = ListNode(0, ListNode(10, ListNode(20, ListNode(30, ListNode(0, ListNode(40, ListNode(0)))))))
result = mergeNodes(head)
print_linked_list(result)  # Output: [60, 40]

# Time and Space Complexity Analysis
"""
Time Complexity:
- O(n): We traverse the linked list once, where n is the number of nodes in the list.

Space Complexity:
- O(1): We use a constant amount of extra space for pointers and variables. The output list does not count as extra space.

Overall, the solution is efficient and works well for large inputs.
"""

# Topic: Linked List