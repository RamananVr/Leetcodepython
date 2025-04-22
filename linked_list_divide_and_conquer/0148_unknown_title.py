"""
LeetCode Problem #148: Sort List

Problem Statement:
Given the head of a linked list, return the list after sorting it in ascending order.

Constraints:
1. The number of nodes in the list is in the range [0, 5 * 10^4].
2. -10^5 <= Node.val <= 10^5

Follow up: Can you sort the linked list in O(n log n) time and O(1) memory (i.e., constant space)?

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case: if the list is empty or has only one node, it's already sorted
        if not head or not head.next:
            return head

        # Step 1: Split the list into two halves using the slow and fast pointer approach
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves
        mid = slow.next
        slow.next = None

        # Step 2: Recursively sort each half
        left = self.sortList(head)
        right = self.sortList(mid)

        # Step 3: Merge the two sorted halves
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Dummy node to simplify the merge process
        dummy = ListNode()
        current = dummy

        # Merge the two lists
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # Append the remaining nodes from either list
        if l1:
            current.next = l1
        if l2:
            current.next = l2

        return dummy.next

# Example Test Cases
def print_list(head):
    """Helper function to print the linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1
head1 = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
solution = Solution()
sorted_head1 = solution.sortList(head1)
print("Test Case 1:", print_list(sorted_head1))  # Output: [1, 2, 3, 4]

# Test Case 2
head2 = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
sorted_head2 = solution.sortList(head2)
print("Test Case 2:", print_list(sorted_head2))  # Output: [-1, 0, 3, 4, 5]

# Test Case 3
head3 = None
sorted_head3 = solution.sortList(head3)
print("Test Case 3:", print_list(sorted_head3))  # Output: []

"""
Time Complexity:
- The algorithm uses merge sort, which has a time complexity of O(n log n).
  - Splitting the list into halves takes O(log n) recursive calls.
  - Merging two sorted lists takes O(n) time in total across all levels of recursion.
- Therefore, the overall time complexity is O(n log n).

Space Complexity:
- The algorithm uses O(log n) space for the recursion stack due to the divide-and-conquer approach.
- The merge process itself does not use additional space (it operates in-place).
- Therefore, the overall space complexity is O(log n).

Topic: Linked List, Divide and Conquer
"""