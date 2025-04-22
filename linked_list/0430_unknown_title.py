"""
LeetCode Problem #430: Flatten a Multilevel Doubly Linked List

Problem Statement:
You are given a doubly linked list, which in addition to the next and previous pointers, 
could have a child pointer, which may or may not point to a separate doubly linked list. 
These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, 
as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. 
You are given the head of the first level of the list.

Example:
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]

Explanation:
The multilevel linked list in the input is represented as follows:
1---2---3---4---5---6--NULL
        |
        7---8---9---10--NULL
            |
            11--12--NULL

After flattening, the linked list becomes:
1---2---3---7---8---11---12---9---10---4---5---6--NULL

Constraints:
- The number of Nodes in the doubly linked list is in the range [0, 1000].
- 1 <= Node.val <= 10^5
- The values of the nodes are unique.

Note:
- The child pointer of a node may point to null, indicating no child list.
- The next pointer of the last node in a multilevel doubly linked list must point to null when flattened.
"""

# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # Helper function to recursively flatten the list
        def flatten_dfs(prev, curr):
            if not curr:
                return prev
            
            curr.prev = prev
            prev.next = curr

            # Save the next node
            temp_next = curr.next

            # Recursively flatten the child list
            tail = flatten_dfs(curr, curr.child)
            curr.child = None  # Clear the child pointer

            # Continue with the next node
            return flatten_dfs(tail, temp_next)

        # Create a dummy node to simplify edge cases
        dummy = Node(0)
        flatten_dfs(dummy, head)
        dummy.next.prev = None  # Detach the dummy node
        return dummy.next

# Example Test Cases
def print_list(head):
    """Helper function to print the flattened list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test Case 1
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node11 = Node(11)
node12 = Node(12)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4
node5.next = node6
node6.prev = node5

node3.child = node7
node7.next = node8
node8.prev = node7
node8.child = node11
node11.next = node12
node12.prev = node11
node8.next = node9
node9.prev = node8
node9.next = node10
node10.prev = node9

solution = Solution()
flattened_head = solution.flatten(node1)
print(print_list(flattened_head))  # Output: [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]

# Test Case 2
node1 = Node(1)
node2 = Node(2)
node1.child = node2
flattened_head = solution.flatten(node1)
print(print_list(flattened_head))  # Output: [1, 2]

# Time and Space Complexity Analysis
# Time Complexity: O(N), where N is the total number of nodes in the multilevel doubly linked list.
#                  Each node is visited exactly once.
# Space Complexity: O(N) in the worst case due to the recursion stack when the list is deeply nested.

# Topic: Linked List