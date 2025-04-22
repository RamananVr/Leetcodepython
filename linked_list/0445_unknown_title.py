"""
LeetCode Problem #445: Add Two Numbers II

Problem Statement:
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]

Constraints:
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.

Follow up: Could you solve it without reversing the input lists?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Adds two numbers represented by linked lists in reverse order.
    """
    # Helper function to convert a linked list to a stack
    def to_stack(node):
        stack = []
        while node:
            stack.append(node.val)
            node = node.next
        return stack

    # Convert both linked lists to stacks
    stack1 = to_stack(l1)
    stack2 = to_stack(l2)

    carry = 0
    result = None

    # Process the stacks and carry
    while stack1 or stack2 or carry:
        val1 = stack1.pop() if stack1 else 0
        val2 = stack2.pop() if stack2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        new_node = ListNode(total % 10)
        new_node.next = result
        result = new_node

    return result

# Example Test Cases
def print_linked_list(node):
    """Helper function to print a linked list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

if __name__ == "__main__":
    # Test Case 1
    l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = addTwoNumbers(l1, l2)
    print_linked_list(result)  # Output: [7, 8, 0, 7]

    # Test Case 2
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = addTwoNumbers(l1, l2)
    print_linked_list(result)  # Output: [8, 0, 7]

    # Test Case 3
    l1 = ListNode(0)
    l2 = ListNode(0)
    result = addTwoNumbers(l1, l2)
    print_linked_list(result)  # Output: [0]

"""
Time Complexity:
- Let n and m be the lengths of the two linked lists.
- Converting the linked lists to stacks takes O(n + m).
- Processing the stacks takes O(max(n, m)).
- Overall time complexity: O(n + m).

Space Complexity:
- The space used by the stacks is O(n + m).
- The space used by the result linked list is O(max(n, m)).
- Overall space complexity: O(n + m).

Topic: Linked List
"""