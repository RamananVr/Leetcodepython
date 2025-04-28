"""
LeetCode Problem #1290: Convert Binary Number in a Linked List to Integer

Problem Statement:
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101 in binary is 5 in decimal)

Example 2:
Input: head = [0]
Output: 0

Constraints:
- The Linked List is not empty.
- Number of nodes will not exceed 30.
- Each node's value is either 0 or 1.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution
def getDecimalValue(head: ListNode) -> int:
    """
    Convert the binary number represented by the linked list to an integer.
    """
    num = 0
    while head:
        # Shift the current number to the left and add the current node's value
        num = (num << 1) | head.val
        head = head.next
    return num

# Example Test Cases
def test_getDecimalValue():
    # Helper function to create a linked list from a list
    def create_linked_list(values):
        dummy = ListNode()
        current = dummy
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return dummy.next

    # Test Case 1
    head1 = create_linked_list([1, 0, 1])
    assert getDecimalValue(head1) == 5, "Test Case 1 Failed"

    # Test Case 2
    head2 = create_linked_list([0])
    assert getDecimalValue(head2) == 0, "Test Case 2 Failed"

    # Test Case 3
    head3 = create_linked_list([1])
    assert getDecimalValue(head3) == 1, "Test Case 3 Failed"

    # Test Case 4
    head4 = create_linked_list([1, 1, 1, 1])
    assert getDecimalValue(head4) == 15, "Test Case 4 Failed"

    # Test Case 5
    head5 = create_linked_list([1, 0, 0, 1, 0])
    assert getDecimalValue(head5) == 18, "Test Case 5 Failed"

    print("All test cases passed!")

# Run the test cases
if __name__ == "__main__":
    test_getDecimalValue()

"""
Time Complexity:
- O(n), where n is the number of nodes in the linked list. We traverse the linked list once.

Space Complexity:
- O(1), as we use a constant amount of extra space.

Topic: Linked List
"""