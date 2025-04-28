"""
LeetCode Problem #1019: Next Greater Node In Linked List

Problem Statement:
You are given the head of a linked list with `n` nodes. For each node in the list, find the next node that has a strictly greater value than the current node. Return an integer array `result` where `result[i]` is the value of the next greater node of the `i-th` node in the linked list. If there is no next greater node, set `result[i] = 0`.

Example:
Input: head = [2, 1, 5]
Output: [5, 5, 0]

Constraints:
- The number of nodes in the list is in the range [1, 10000].
- 1 <= Node.val <= 10^9
"""

# Solution
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nextLargerNodes(head: ListNode) -> List[int]:
    # Convert linked list to array
    values = []
    while head:
        values.append(head.val)
        head = head.next
    
    # Result array and monotonic stack
    result = [0] * len(values)
    stack = []
    
    # Traverse the array to find next greater elements
    for i, value in enumerate(values):
        while stack and values[stack[-1]] < value:
            index = stack.pop()
            result[index] = value
        stack.append(i)
    
    return result

# Example Test Cases
def build_linked_list(values: List[int]) -> ListNode:
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
    # Test Case 1
    head = build_linked_list([2, 1, 5])
    print(nextLargerNodes(head))  # Output: [5, 5, 0]

    # Test Case 2
    head = build_linked_list([2, 7, 4, 3, 5])
    print(nextLargerNodes(head))  # Output: [7, 0, 5, 5, 0]

    # Test Case 3
    head = build_linked_list([1, 7, 5, 1, 9])
    print(nextLargerNodes(head))  # Output: [7, 9, 9, 9, 0]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Converting the linked list to an array takes O(n), where n is the number of nodes in the linked list.
- The traversal of the array to find the next greater elements using a monotonic stack takes O(n) in the worst case.
- Overall time complexity: O(n).

Space Complexity:
- The `values` array takes O(n) space to store the linked list values.
- The `result` array takes O(n) space to store the output.
- The stack can hold up to O(n) indices in the worst case.
- Overall space complexity: O(n).

Topic: Linked List, Monotonic Stack
"""