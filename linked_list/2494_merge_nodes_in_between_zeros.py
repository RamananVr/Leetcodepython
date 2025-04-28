"""
LeetCode Question #2494: Merge Nodes in Between Zeros

Problem Statement:
You are given the head of a linked list, which contains a series of integers separated by 0's. Specifically, the linked list starts with a 0, and there are no consecutive 0's. The linked list ends with a 0.

For every sequence of integers separated by 0's, merge them into a single node whose value is the sum of all the integers in the sequence. After merging all the sequences, return the modified linked list.

Example:
Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation:
- The first sequence is [3,1], which sums to 4.
- The second sequence is [4,5,2], which sums to 11.

Constraints:
- The number of nodes in the list is between 3 and 2 * 10^5.
- 0 <= Node.val <= 1000
- There are no consecutive 0's in the list.
- The list starts and ends with 0.

"""

# Clean, Correct Python Solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeNodes(head: ListNode) -> ListNode:
    # Initialize pointers
    dummy = ListNode(0)  # Dummy node to simplify the result list construction
    current = dummy
    sum_val = 0
    
    # Traverse the linked list
    while head:
        if head.val == 0:
            if sum_val > 0:  # If we have accumulated a sum, create a new node
                current.next = ListNode(sum_val)
                current = current.next
                sum_val = 0  # Reset sum for the next sequence
        else:
            sum_val += head.val  # Accumulate the sum
        head = head.next
    
    return dummy.next

# Example Test Cases
def print_linked_list(head):
    """Helper function to print linked list values."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1
head1 = ListNode(0)
head1.next = ListNode(3)
head1.next.next = ListNode(1)
head1.next.next.next = ListNode(0)
head1.next.next.next.next = ListNode(4)
head1.next.next.next.next.next = ListNode(5)
head1.next.next.next.next.next.next = ListNode(2)
head1.next.next.next.next.next.next.next = ListNode(0)

result1 = mergeNodes(head1)
print(print_linked_list(result1))  # Output: [4, 11]

# Test Case 2
head2 = ListNode(0)
head2.next = ListNode(1)
head2.next.next = ListNode(0)
head2.next.next.next = ListNode(2)
head2.next.next.next.next = ListNode(3)
head2.next.next.next.next.next = ListNode(0)

result2 = mergeNodes(head2)
print(print_linked_list(result2))  # Output: [1, 5]

# Test Case 3
head3 = ListNode(0)
head3.next = ListNode(0)

result3 = mergeNodes(head3)
print(print_linked_list(result3))  # Output: []

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm traverses the linked list once, processing each node exactly once.
- Therefore, the time complexity is O(n), where n is the number of nodes in the linked list.

Space Complexity:
- The algorithm uses a dummy node and creates new nodes for the result list.
- The space complexity is O(k), where k is the number of non-zero sequences in the linked list.
- However, the input linked list itself is reused, so no additional space is required for processing.

Overall Space Complexity: O(k)
"""

# Topic: Linked List