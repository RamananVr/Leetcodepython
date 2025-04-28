"""
LeetCode Problem #1669: Merge In Between Linked Lists

Problem Statement:
You are given two linked lists: list1 and list2. 
You are also given two integers a and b where 0 <= a <= b < len(list1). 
The task is to merge the two linked lists in the following way:
- Remove list1's nodes from index a to index b, inclusive.
- Insert list2 into list1 at the position a.

The resulting linked list should be returned.

Constraints:
- The number of nodes in list1 is in the range [1, 10^4].
- The number of nodes in list2 is in the range [1, 10^4].
- 0 <= a <= b < len(list1).
- list1 and list2 are non-empty.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeInBetween(list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    """
    Merges list2 into list1 between indices a and b.
    """
    # Step 1: Find the node before index `a` in list1
    prev_a = list1
    for _ in range(a - 1):
        prev_a = prev_a.next

    # Step 2: Find the node at index `b` in list1
    after_b = prev_a
    for _ in range(b - a + 2):
        after_b = after_b.next

    # Step 3: Connect prev_a to the head of list2
    prev_a.next = list2

    # Step 4: Traverse list2 to its tail
    tail_list2 = list2
    while tail_list2.next:
        tail_list2 = tail_list2.next

    # Step 5: Connect the tail of list2 to after_b
    tail_list2.next = after_b

    return list1

# Example Test Cases
def print_linked_list(head: ListNode):
    """Helper function to print a linked list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1
list1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
list2 = ListNode(100, ListNode(101, ListNode(102)))
a, b = 3, 4
result = mergeInBetween(list1, a, b, list2)
print(print_linked_list(result))  # Output: [0, 1, 2, 100, 101, 102, 5]

# Test Case 2
list1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
list2 = ListNode(100, ListNode(101))
a, b = 2, 5
result = mergeInBetween(list1, a, b, list2)
print(print_linked_list(result))  # Output: [0, 1, 100, 101, 6]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Finding the node before index `a` takes O(a).
- Finding the node after index `b` takes O(b - a).
- Traversing list2 to its tail takes O(len(list2)).
- Overall, the time complexity is O(a + (b - a) + len(list2)) = O(a + b + len(list2)).

Space Complexity:
- The algorithm uses O(1) extra space since it modifies the linked list in place.
"""

# Topic: Linked List