"""
LeetCode Question #382: Linked List Random Node

Problem Statement:
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:
- Solution(ListNode head): Initializes the object with the head of the singly-linked list.
- int getRandom(): Chooses a node randomly from the list and returns its value. All nodes should have an equal probability of being chosen.

Constraints:
- The number of nodes in the linked list is in the range [1, 10^4].
- -10^4 <= Node.val <= 10^4
- At most 10^4 calls will be made to getRandom.

Follow-up:
What if the linked list is extremely large and you don't have enough memory to store the entire list?

"""

import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head: ListNode):
        """
        Initializes the Solution object with the head of the linked list.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value from the linked list.
        Uses Reservoir Sampling to ensure equal probability for all nodes.
        """
        reservoir = -1
        current = self.head
        index = 0

        while current:
            # Reservoir Sampling: Replace the reservoir with the current node's value
            # with probability 1/(index + 1).
            if random.randint(0, index) == 0:
                reservoir = current.val
            current = current.next
            index += 1

        return reservoir


# Example Test Cases
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Initialize the Solution object
    solution = Solution(head)

    # Call getRandom multiple times to observe randomness
    print(solution.getRandom())  # Output: Random value from [1, 2, 3, 4, 5]
    print(solution.getRandom())  # Output: Random value from [1, 2, 3, 4, 5]
    print(solution.getRandom())  # Output: Random value from [1, 2, 3, 4, 5]

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The `getRandom` method traverses the linked list once, so its time complexity is O(n), 
     where n is the number of nodes in the linked list.

2. Space Complexity:
   - The solution uses O(1) extra space since it does not store the entire linked list in memory 
     and only uses a few variables for computation.

Topic: Linked List
"""