"""
LeetCode Problem #2816: Double a Number Represented as a Linked List

Problem Statement:
You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes. 
The digits are stored in reverse order, meaning that the 1's digit is the head of the list. 
Your task is to double the number represented by the linked list and return the head of the new linked list.

Example:
Input: head = [2, 4, 3] (represents the number 342)
Output: [4, 8, 6] (represents the number 684)

Constraints:
- The number represented by the linked list will not exceed 10^100.
- The linked list is non-empty and contains only digits (0-9).
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def double_linked_list(head: ListNode) -> ListNode:
    """
    Doubles the number represented by a linked list and returns the new linked list.
    """
    # Convert linked list to integer
    num = 0
    multiplier = 1
    current = head
    while current:
        num += current.val * multiplier
        multiplier *= 10
        current = current.next

    # Double the number
    num *= 2

    # Convert the doubled number back to a linked list
    dummy = ListNode()
    current = dummy
    if num == 0:
        return ListNode(0)
    while num > 0:
        current.next = ListNode(num % 10)
        num //= 10
        current = current.next

    return dummy.next

# Example Test Cases
def print_linked_list(head: ListNode):
    """Helper function to print linked list as a list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1
head1 = ListNode(2, ListNode(4, ListNode(3)))  # Represents 342
result1 = double_linked_list(head1)
print(print_linked_list(result1))  # Expected Output: [4, 8, 6] (Represents 684)

# Test Case 2
head2 = ListNode(0)  # Represents 0
result2 = double_linked_list(head2)
print(print_linked_list(result2))  # Expected Output: [0] (Represents 0)

# Test Case 3
head3 = ListNode(5, ListNode(9, ListNode(9)))  # Represents 995
result3 = double_linked_list(head3)
print(print_linked_list(result3))  # Expected Output: [0, 9, 9, 1] (Represents 1990)

# Time and Space Complexity Analysis
"""
Time Complexity:
- Converting the linked list to an integer takes O(n), where n is the number of nodes in the linked list.
- Doubling the number is a constant-time operation.
- Converting the doubled number back to a linked list takes O(d), where d is the number of digits in the doubled number.
- In the worst case, d is proportional to n (e.g., doubling a number like 999...999).
- Overall, the time complexity is O(n).

Space Complexity:
- The space used for the new linked list is proportional to the number of digits in the doubled number, which is O(n) in the worst case.
- No additional space is used apart from the new linked list and a few variables.
- Overall, the space complexity is O(n).
"""

# Topic: Linked List