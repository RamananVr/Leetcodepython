"""
LeetCode Question #142: Linked List Cycle II

Problem Statement:
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: The node with value 2
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: The node with value 1
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: null
Explanation: There is no cycle in the linked list.

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked list.

Follow up: Can you solve it using O(1) (i.e., constant) memory?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head):
    """
    Detects the node where the cycle begins in a linked list.
    If there is no cycle, returns None.

    :param head: ListNode, the head of the linked list
    :return: ListNode or None
    """
    if not head or not head.next:
        return None

    # Step 1: Use Floyd's Tortoise and Hare algorithm to detect a cycle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # Cycle detected
            break
    else:
        # No cycle
        return None

    # Step 2: Find the start of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

# Example Test Cases
if __name__ == "__main__":
    # Helper function to create a linked list with a cycle
    def createLinkedListWithCycle(values, pos):
        nodes = [ListNode(val) for val in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        if pos != -1:
            nodes[-1].next = nodes[pos]
        return nodes[0]

    # Test Case 1
    head1 = createLinkedListWithCycle([3, 2, 0, -4], 1)
    print(detectCycle(head1).val)  # Output: 2

    # Test Case 2
    head2 = createLinkedListWithCycle([1, 2], 0)
    print(detectCycle(head2).val)  # Output: 1

    # Test Case 3
    head3 = createLinkedListWithCycle([1], -1)
    print(detectCycle(head3))  # Output: None

    # Test Case 4
    head4 = createLinkedListWithCycle([], -1)
    print(detectCycle(head4))  # Output: None

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm runs in O(n) time, where n is the number of nodes in the linked list.
- In the worst case, the fast pointer traverses the entire list to detect the cycle, and then both pointers traverse the list again to find the cycle's start.

Space Complexity:
- The algorithm uses O(1) space since it only uses two pointers (slow and fast) and does not require any additional data structures.

Topic: Linked List
"""