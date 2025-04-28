"""
LeetCode Problem #708: Insert into a Sorted Circular Linked List

Problem Statement:
Given a node from a Circular Linked List, which is sorted in ascending order, write a function to insert a value into the list such that it remains a sorted circular list. You may assume that the initial list is non-empty and the given node is not a null pointer.

The Circular Linked List is represented as a single node. The node's `next` pointer points to the next node in the list, and the last node's `next` pointer points back to the first node.

You are given the `head` node and the integer `insertVal`. Return the same `head` node after insertion.

Constraints:
- The number of nodes in the list is in the range [1, 1000].
- -10^6 <= Node.val <= 10^6
- -10^6 <= insertVal <= 10^6

Example:
Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]

Explanation:
The new node with value 2 is inserted into the list, and the list remains sorted.
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def insert(head: Node, insertVal: int) -> Node:
    """
    Inserts a value into a sorted circular linked list.
    """
    new_node = Node(insertVal)
    
    # Case 1: If the list is empty, create a new circular list with the new node.
    if not head:
        new_node.next = new_node
        return new_node
    
    prev, curr = head, head.next
    while True:
        # Case 2: Insert between two nodes in sorted order.
        if prev.val <= insertVal <= curr.val:
            break
        
        # Case 3: Insert at the boundary of the largest and smallest values.
        if prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val):
            break
        
        prev = curr
        curr = curr.next
        
        # Case 4: If we've looped through the entire list, insert at the end.
        if prev == head:
            break
    
    # Insert the new node between prev and curr.
    prev.next = new_node
    new_node.next = curr
    return head

# Example Test Cases
def print_circular_linked_list(head: Node):
    """
    Helper function to print the circular linked list.
    """
    if not head:
        return "[]"
    
    result = []
    current = head
    while True:
        result.append(current.val)
        current = current.next
        if current == head:
            break
    return result

# Test Case 1
head = Node(3)
node2 = Node(4)
node3 = Node(1)
head.next = node2
node2.next = node3
node3.next = head
insertVal = 2
new_head = insert(head, insertVal)
print(print_circular_linked_list(new_head))  # Output: [3, 4, 1, 2]

# Test Case 2
head = Node(1)
head.next = head
insertVal = 0
new_head = insert(head, insertVal)
print(print_circular_linked_list(new_head))  # Output: [1, 0]

# Test Case 3
head = None
insertVal = 5
new_head = insert(head, insertVal)
print(print_circular_linked_list(new_head))  # Output: [5]

# Time and Space Complexity Analysis
# Time Complexity: O(n), where n is the number of nodes in the circular linked list.
# We may need to traverse the entire list to find the correct insertion point.
# Space Complexity: O(1), as we are only creating one new node and using constant extra space.

# Topic: Linked List