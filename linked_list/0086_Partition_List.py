"""
LeetCode Problem #86: Partition List

Problem Statement:
Given the `head` of a linked list and a value `x`, partition it such that all nodes less than `x` come before nodes greater than or equal to `x`.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]

Constraints:
- The number of nodes in the list is in the range `[0, 200]`.
- `-100 <= Node.val <= 100`
- `-200 <= x <= 200`
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head: ListNode, x: int) -> ListNode:
    """
    Partition the linked list such that all nodes less than x come before nodes greater than or equal to x.
    """
    # Create two dummy nodes for two partitions
    less_head = ListNode(0)
    greater_head = ListNode(0)
    
    # Pointers to build the two partitions
    less = less_head
    greater = greater_head
    
    # Traverse the original list
    current = head
    while current:
        if current.val < x:
            less.next = current
            less = less.next
        else:
            greater.next = current
            greater = greater.next
        current = current.next
    
    # Connect the two partitions
    greater.next = None  # End the greater list
    less.next = greater_head.next  # Connect less list to greater list
    
    return less_head.next

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    head = create_linked_list([1, 4, 3, 2, 5, 2])
    x = 3
    result = partition(head, x)
    print(linked_list_to_list(result))  # Output: [1, 2, 2, 4, 3, 5]

    # Test Case 2
    head = create_linked_list([2, 1])
    x = 2
    result = partition(head, x)
    print(linked_list_to_list(result))  # Output: [1, 2]

    # Test Case 3
    head = create_linked_list([1, 2, 3, 4, 5])
    x = 3
    result = partition(head, x)
    print(linked_list_to_list(result))  # Output: [1, 2, 3, 4, 5]

    # Test Case 4
    head = create_linked_list([])
    x = 0
    result = partition(head, x)
    print(linked_list_to_list(result))  # Output: []

"""
Time Complexity Analysis:
- The algorithm traverses the linked list once, performing O(1) operations for each node.
- Therefore, the time complexity is O(n), where n is the number of nodes in the linked list.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space for the dummy nodes and pointers.
- Therefore, the space complexity is O(1).

Topic: Linked List
"""