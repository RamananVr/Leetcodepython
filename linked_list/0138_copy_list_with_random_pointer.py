"""
LeetCode Question #138: Copy List with Random Pointer

Problem Statement:
A linked list is given where each node contains an additional random pointer, which could point to any node in the list or null.

You need to create a deep copy of the list. The deep copy should consist of exactly the same nodes and the same structure as the original list. The new list's random pointer should point to the corresponding node in the new list, not the original list.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of `n` nodes, where each node is represented as a pair of `[val, random_index]`:
- `val`: an integer representing the value of the node.
- `random_index`: the index of the node (range from `0` to `n-1`) that the random pointer points to, or `null` if it does not point to any node.

Constraints:
- The number of nodes in the list is in the range `[0, 1000]`.
- `-10^4 <= Node.val <= 10^4`
- `Node.random` is `null` or points to a node in the linked list.

"""

# Definition for a Node.
class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head: 'Node') -> 'Node':
    """
    Creates a deep copy of a linked list with random pointers.
    """
    if not head:
        return None

    # Step 1: Create a copy of each node and insert it right after the original node
    current = head
    while current:
        new_node = Node(current.val, current.next)
        current.next = new_node
        current = new_node.next

    # Step 2: Assign random pointers for the copied nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Step 3: Separate the original list and the copied list
    original = head
    copy = head.next
    copy_head = copy
    while original:
        original.next = original.next.next
        if copy.next:
            copy.next = copy.next.next
        original = original.next
        copy = copy.next

    return copy_head

# Example Test Cases
def print_list(head: 'Node'):
    """
    Helper function to print the linked list for debugging.
    """
    result = []
    while head:
        random_val = head.random.val if head.random else None
        result.append((head.val, random_val))
        head = head.next
    return result

# Test Case 1: Example from the problem statement
node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node1.random = None
node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1

copied_list = copyRandomList(node1)
print("Original List:", print_list(node1))
print("Copied List:", print_list(copied_list))

# Test Case 2: Empty list
empty_list = None
copied_empty_list = copyRandomList(empty_list)
print("Original List:", print_list(empty_list))
print("Copied List:", print_list(copied_empty_list))

# Test Case 3: Single node with no random pointer
single_node = Node(42)
copied_single_node = copyRandomList(single_node)
print("Original List:", print_list(single_node))
print("Copied List:", print_list(copied_single_node))

# Time and Space Complexity Analysis
"""
Time Complexity:
- Step 1: O(n) to iterate through the list and create new nodes.
- Step 2: O(n) to assign random pointers.
- Step 3: O(n) to separate the original and copied lists.
Overall: O(n), where n is the number of nodes in the linked list.

Space Complexity:
- The algorithm uses O(1) additional space (in-place modification).
- However, the copied list itself requires O(n) space for the new nodes.
Overall: O(n).
"""

# Topic: Linked List