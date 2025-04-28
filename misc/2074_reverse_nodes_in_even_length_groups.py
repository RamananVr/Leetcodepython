"""
LeetCode Question #2074: Reverse Nodes in Even Length Groups

Problem Statement:
You are given the head of a linked list.

The nodes in the linked list are sequentially assigned to groups whose lengths form the sequence of the natural numbers (1, 2, 3, ...). Specifically:
- The 1st node is assigned to the first group.
- The 2nd and the 3rd nodes are assigned to the second group.
- The 4th, 5th, 6th nodes are assigned to the third group, and so on.

You are tasked with reversing the nodes in each group with an even length.

Return the head of the modified linked list after reversing the nodes in the even-length groups.

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 1 <= Node.val <= 10^5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseEvenLengthGroups(head: ListNode) -> ListNode:
    """
    Reverse nodes in even-length groups in the linked list.
    """
    # Initialize pointers
    current = head
    group_size = 1

    while current:
        # Collect nodes in the current group
        group_nodes = []
        for _ in range(group_size):
            if current:
                group_nodes.append(current)
                current = current.next
            else:
                break

        # Reverse the group if its length is even
        if len(group_nodes) % 2 == 0:
            for i in range(len(group_nodes) - 1, 0, -1):
                group_nodes[i].next = group_nodes[i - 1]
            group_nodes[0].next = current
            if group_size == 1:
                head = group_nodes[-1]