"""
LeetCode Problem #369: Plus One Linked List

Problem Statement:
Given a non-negative integer represented as a singly linked list of digits, add 1 to the integer. 
The digits are stored such that the most significant digit is at the head of the list.

Example:
Input: head = [1,2,3]
Output: [1,2,4]

Constraints:
- The number of nodes in the linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- The number represented by the linked list does not contain leading zeros except for the number 0 itself.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        """
        Adds one to the number represented by the linked list.
        """
        # Helper function to reverse the linked list
        def reverse_list(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev

        # Step 1: Reverse the linked list
        head = reverse_list(head)

        # Step 2: Add one to the reversed list
        current = head
        carry = 1
        while current:
            current.val += carry
            if current.val < 10:
                carry = 0
                break
            current.val = 0
            if not current.next:
                current.next = ListNode(0)
            current = current.next

        # Step 3: Reverse the list back to its original order
        return reverse_list(head)

# Example Test Cases
def print_linked_list(head):
    """Helper function to print a linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

if __name__ == "__main__":
    # Test Case 1
    head = ListNode(1, ListNode(2, ListNode(3)))
    solution = Solution()
    result = solution.plusOne(head)
    print(print_linked_list(result))  # Output: [1, 2, 4]

    # Test Case 2
    head = ListNode(9, ListNode(9, ListNode(9)))
    result = solution.plusOne(head)
    print(print_linked_list(result))  # Output: [1, 0, 0, 0]

    # Test Case 3
    head = ListNode(0)
    result = solution.plusOne(head)
    print(print_linked_list(result))  # Output: [1]

"""
Time Complexity Analysis:
- Reversing the linked list takes O(n), where n is the number of nodes in the list.
- Adding one to the reversed list also takes O(n) in the worst case (if we need to propagate the carry through all nodes).
- Reversing the list back to its original order takes another O(n).
- Overall time complexity: O(n).

Space Complexity Analysis:
- The algorithm uses O(1) additional space since we are modifying the linked list in place.
- Overall space complexity: O(1).

Topic: Linked List
"""