"""
LeetCode Problem #234: Palindrome Linked List

Problem Statement:
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

A linked list is a palindrome if the sequence of values is the same forward and backward.

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:
    """
    Determines if a singly linked list is a palindrome.

    Args:
    head (ListNode): The head of the singly linked list.

    Returns:
    bool: True if the linked list is a palindrome, False otherwise.
    """
    # Step 1: Find the middle of the linked list using the slow and fast pointer approach
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the linked list
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # Step 3: Compare the first half and the reversed second half
    left, right = head, prev
    while right:  # Only need to compare until the end of the reversed half
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True

# Example Test Cases
def build_linked_list(values):
    """Helper function to build a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

if __name__ == "__main__":
    # Test Case 1: Palindrome list
    head1 = build_linked_list([1, 2, 2, 1])
    print(isPalindrome(head1))  # Output: True

    # Test Case 2: Non-palindrome list
    head2 = build_linked_list([1, 2])
    print(isPalindrome(head2))  # Output: False

    # Test Case 3: Single element list
    head3 = build_linked_list([1])
    print(isPalindrome(head3))  # Output: True

    # Test Case 4: Empty list (edge case)
    head4 = build_linked_list([])
    print(isPalindrome(head4))  # Output: True

    # Test Case 5: Palindrome list with odd number of elements
    head5 = build_linked_list([1, 2, 3, 2, 1])
    print(isPalindrome(head5))  # Output: True

"""
Time Complexity Analysis:
- Finding the middle of the linked list takes O(n) time.
- Reversing the second half of the linked list takes O(n) time.
- Comparing the two halves takes O(n) time.
Overall, the time complexity is O(n), where n is the number of nodes in the linked list.

Space Complexity Analysis:
- The algorithm uses O(1) additional space since the reversal is done in-place.
Overall, the space complexity is O(1).

Topic: Linked List
"""