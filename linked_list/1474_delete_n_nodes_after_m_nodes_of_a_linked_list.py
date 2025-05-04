"""
LeetCode Question #1474: Delete N Nodes After M Nodes of a Linked List

Problem Statement:
Given the head of a linked list and two integers M and N. Traverse the linked list such that you retain the first M nodes, 
then delete the next N nodes. Continue the same process until the end of the linked list.

Return the head of the modified linked list.

Example 1:
Input: head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], M = 2, N = 3
Output: [1, 2, 6, 7, 10]

Example 2:
Input: head = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], M = 1, N = 1
Output: [1, 3, 5, 7, 9]

Constraints:
- The number of nodes in the list is in the range [1, 10^4].
- 1 <= Node.val <= 10^6
- 1 <= M, N <= 1000
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNodes(head: ListNode, m: int, n: int) -> ListNode:
    """
    Deletes N nodes after retaining M nodes in the linked list.
    """
    current = head
    
    while current:
        # Retain M nodes
        for _ in range(m - 1):
            if not current:
                return head
            current = current.next
        
        # Delete N nodes
        temp = current.next
        for _ in range(n):
            if not temp:
                break
            temp = temp.next
        
        # Connect the retained part to the remaining part
        if current:
            current.next = temp
            current = temp
    
    return head

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
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
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    m, n = 2, 3
    modified_head = deleteNodes(head, m, n)
    print(linked_list_to_list(modified_head))  # Output: [1, 2, 6, 7, 10]

    # Test Case 2
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    m, n = 1, 1
    modified_head = deleteNodes(head, m, n)
    print(linked_list_to_list(modified_head))  # Output: [1, 3, 5, 7, 9]

    # Test Case 3
    head = create_linked_list([1, 2, 3, 4, 5])
    m, n = 3, 2
    modified_head = deleteNodes(head, m, n)
    print(linked_list_to_list(modified_head))  # Output: [1, 2, 3]

# Time and Space Complexity Analysis:
# Time Complexity: O(n)
# - We traverse the entire linked list once, where n is the number of nodes in the list.
# - Retaining M nodes and deleting N nodes are both linear operations.

# Space Complexity: O(1)
# - The algorithm uses a constant amount of extra space, as it modifies the linked list in place.

# Topic: Linked List