"""
LeetCode Question #2: Add Two Numbers

Problem Statement:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Adds two numbers represented as linked lists and returns the sum as a linked list.
    """
    dummy_head = ListNode(0)  # Dummy node to simplify result list construction
    current = dummy_head
    carry = 0

    # Traverse both linked lists
    while l1 or l2 or carry:
        # Get the values from the current nodes of l1 and l2, or 0 if the node is None
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate the sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)

        # Move to the next nodes
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next

# Helper function to create a linked list from a list of integers
def create_linked_list(values):
    dummy_head = ListNode(0)
    current = dummy_head
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy_head.next

# Helper function to convert a linked list to a list of integers
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))  # Output: [7, 0, 8]

    # Test Case 2
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))  # Output: [0]

    # Test Case 3
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result = addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))  # Output: [8, 9, 9, 9, 0, 0, 0, 1]

"""
Time Complexity:
- O(max(m, n)): We traverse the longer of the two linked lists, where m and n are the lengths of l1 and l2, respectively.

Space Complexity:
- O(max(m, n)): The space required for the result linked list is proportional to the length of the longer input list.

Topic: Linked List
"""