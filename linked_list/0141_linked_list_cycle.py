"""
LeetCode Question #141: Linked List Cycle

Problem Statement:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5

Follow up:
Can you solve it using O(1) (i.e., constant) memory?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    """
    Detects if a linked list has a cycle using Floyd's Tortoise and Hare algorithm.

    :param head: ListNode, the head of the linked list
    :return: bool, True if the linked list has a cycle, False otherwise
    """
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Linked list with a cycle
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates a cycle
    print(hasCycle(node1))  # Expected output: True

    # Test Case 2: Linked list without a cycle
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    print(hasCycle(node1))  # Expected output: False

    # Test Case 3: Single node without a cycle
    node1 = ListNode(1)
    print(hasCycle(node1))  # Expected output: False

    # Test Case 4: Empty linked list
    print(hasCycle(None))  # Expected output: False

"""
Time Complexity Analysis:
- The algorithm uses Floyd's Tortoise and Hare approach, where the slow pointer moves one step at a time, and the fast pointer moves two steps at a time.
- In the worst case, the fast pointer will traverse the entire list, so the time complexity is O(n), where n is the number of nodes in the linked list.

Space Complexity Analysis:
- The algorithm uses two pointers (slow and fast), and no additional data structures are used.
- Therefore, the space complexity is O(1) (constant space).

Topic: Linked List
"""